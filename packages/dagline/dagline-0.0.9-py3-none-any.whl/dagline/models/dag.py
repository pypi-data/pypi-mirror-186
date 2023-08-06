from typing import Dict, List
from dagline.models.operators.winbat import WinbatOperator
from dagline.models.operators.python import PythonOperator
from graphlib import TopologicalSorter
from dagline.utils.logging_setup import LoggingMixin
import copy

class DAG(LoggingMixin):

    def __init__(self, dag_id: str, logfile: str, tasks_flow: Dict):
        self.dag_id = dag_id
        self.logfile = logfile
        '''Each DAG can include the same task instances, we use deepcopy on the tasks
           Make sure each DAG can have its own unique tasks
        '''
        self.tasks_flow = copy.deepcopy(tasks_flow)
        self.sate : str = None
        self._validate_tasks()
        if self.is_valid is True:
            self._collect_tasks()
        else:
            self.log.error(f'''Invaild DAG [{self.dag_id}]''')

    def _validate_tasks(self) -> None:

        '''Need to validate if the tasks_flow can be a DAG graph'''
        try:
            topological_sorter = TopologicalSorter(self.tasks_flow)
            topological_sorter.prepare()
            self.is_valid = True
        except Exception as e:
            self.is_valid = False


    def _collect_tasks(self) -> None:
        self.tasks: Dict = {}
        for child_task, p_task_list in self.tasks_flow.items():
            self.tasks[child_task.task_id] = child_task
            child_task.upstream = p_task_list
            for parent_task in p_task_list:
                self.tasks[parent_task.task_id] = parent_task
                parent_task.downstream.append(child_task)
         
    '''For running the DAG from some specified tasks, then need to call this function and pass a list of task id'''
    def run_from_tasks(self, task_ids : List) -> None:
        self.task_ids_to_start_with : List = copy.copy(task_ids)
        self.run_from_tasks_flow : Dict = {}
        
        for task_id in self.task_ids_to_start_with:
            task = self.tasks[task_id]
            if len(task.downstream) == 0 and task not in self.run_from_tasks_flow:
                self.run_from_tasks_flow[task] = []
            else:
                self.update_tasks_flow(task_id)
        
        if len(self.run_from_tasks_flow) > 0:
            self.tasks_flow = self.run_from_tasks_flow


    def update_tasks_flow(self, parent_task_id : str):
        parent_task = self.tasks[parent_task_id]
        for child_task in parent_task.downstream:
            if child_task not in self.run_from_tasks_flow:
                self.run_from_tasks_flow[child_task] = []

            self.run_from_tasks_flow[child_task].append(parent_task)
            self.update_tasks_flow(child_task.task_id)

    '''for running a specified task in a DAG, call this function and pass the task id'''
    def run_task(self, task_id : str):
        run_task_flow : Dict = {}
        task = self.tasks[task_id]
        run_task_flow[task] = []
        self.tasks_flow = run_task_flow
        

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

