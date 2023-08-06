import multiprocessing
from multiprocessing import Process
import subprocess
from dagline.models.dag import DAG
from dagline.models.operators.python import PythonOperator
from dagline.models.operators.winbat import WinbatOperator
from graphlib import TopologicalSorter
from typing import Callable
from dagline.models.dagbag import DagBag
from dagline.utils.state import State
from dagline.utils.logging_setup import LoggingMixin
from contextlib import redirect_stdout
import io

def execute_python_task(task, task_done_queue):
    try:
        '''To capture stdout output from a Python function call'''
        with redirect_stdout(io.StringIO()) as f:
            task.python_callable()
        
        task_ouput = f.getvalue()
        task.exec_ouput = task_ouput
        task.state = State.SUCCESS
    except Exception as e:
        task.exec_ouput = task_ouput
        task.state = State.FAILED
        
    task_done_queue.put(task)

def execute_winbat_task(task, task_done_queue):
    try:
        #subprocess.check_call(task.bat_command)
        cp = subprocess.run(task.bat_command, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        task.exec_ouput = cp.stdout
        task.state = State.SUCCESS
    except Exception as e:
        task.exec_ouput = e.stdout
        task.state = State.FAILED
        
        
    task_done_queue.put(task)
    
    
class DagProcess(Process, LoggingMixin):

    def __init__(self, dag:DAG):
        super().__init__()
        self.dag = dag
        self.logfile = dag.logfile


    def run(self):
        self.log.info(f'''Starting DAG [{self.dag.dag_id}]''')
        dag_tasks = self.dag.tasks
        dag_tasks_flow = self.dag.tasks_flow
        
        task_done_queue = multiprocessing.Queue()
        
        # keep track of active multiprocessing Process instances
        running_processes = {}
            
        topological_sorter = TopologicalSorter(dag_tasks_flow)
        topological_sorter.prepare()
        while topological_sorter.is_active():
            ready_tasks = topological_sorter.get_ready()
            for task in ready_tasks:
                task_func : Callable
                
                '''Check the task type'''
                if isinstance(task, WinbatOperator):
                    task_func = execute_winbat_task
                elif isinstance(task, PythonOperator):
                    task_func = execute_python_task
                else:
                    pass

                sub_p = multiprocessing.Process(
                target=task_func,
                args=(task, task_done_queue,)
                )
                sub_p.start()
                running_processes[task.task_id] = sub_p
                self.log.info(f'''Executing task [{task.task_id}]''')
            
            '''Make sure we can jump out of the loop if there are some tasks failed
               Cause TopologicalSorter need to iterate all the nodes of the DAG
               If running_processes is empty, that means no nodes of the DAG will be processed any more
            '''
            if len(running_processes) == 0:
                break
                
            # wait for any running task to finish
            finished_task = task_done_queue.get()
            finished_task_id = finished_task.task_id
            finished_task_state = finished_task.state
            finished_task_exec_output = finished_task.exec_ouput
            
            running_processes.pop(finished_task_id).join()
            dag_finished_task = dag_tasks[finished_task_id]
            dag_finished_task.state = finished_task_state
            dag_finished_task.exec_ouput = finished_task_exec_output
            
            

            if finished_task_state == State.SUCCESS:
                '''
                Here we can't use the object from task_done_queue.get() cause the address of the object has been changed 
                after pass the object to process, it is not the same as the original one
                '''
                topological_sorter.done(dag_finished_task)
                
                '''Log the output of the task'''
                self.log.info(f'''Output---From---Task [{dag_finished_task.task_id}]\n{dag_finished_task.exec_ouput}''')
            else:
                self.log.error(f'''Output---From---Task [{dag_finished_task.task_id}]\n{dag_finished_task.exec_ouput}''')

            self.log.info(f'''Finished task [{dag_finished_task.task_id}] (result=[{dag_finished_task.state}])''')
            
        for task in dag_tasks.values():
            if task.state == None:
                task.state = State.SKIPPED
                self.log.info(f'''Finished task [{task.task_id}] (result=[{task.state}])''')

        '''If the state of any tasks in the DAG is failed, the the state of the DAG is failed'''
        if len(list(filter(lambda tk:(tk.state == State.FAILED), dag_tasks.values()))) == 0:
            self.dag.state = State.SUCCESS
            self.log.info(f'''Finished DAG [{self.dag.dag_id}] (result=[{State.SUCCESS:}])''')
        else:
            self.dag.state = State.FAILED
            self.log.info(f'''Finished DAG [{self.dag.dag_id}] (result=[{State.FAILED:}])''')
        
