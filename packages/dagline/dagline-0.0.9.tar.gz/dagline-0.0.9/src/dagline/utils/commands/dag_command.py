from dagline.jobs.dag_processor import DagProcess
from dagline.models.dagbag import DagBag
from dagline.utils.logging_setup import LoggingMixin
from pyvis.network import Network
import os
import webbrowser

log = LoggingMixin.getLogger(__name__)
def dag_list_dags(args):
    pass
    
def dag_run(args):
    dagbag = DagBag(args.dag_files_home)
    dag = dagbag.get_dag(args.dag_id)
    if dag is not None and dag.is_valid:
        not_exist_tasks = set(args.start_with_task_ids) - set(dag.tasks.keys())
        if len(not_exist_tasks) == 0:
            if dag is not None and dag.is_valid:
                dag.run_from_tasks(args.start_with_task_ids)
                dp = DagProcess(dag)
                dp.start()
        else:
            log.error(f'''No task [{not_exist_tasks}] found in DAG [{dag.dag_id}]''')
    # conn = db.get_db_conn()
    # cur = conn.cursor()
    # cur.executemany("INSERT INTO dag VALUES(?, ?, ?)", new_dag)
    # conn.commit()
    
def task_run(args):
    dagbag = DagBag(args.dag_files_home)
    dag = dagbag.get_dag(args.dag_id)
    if dag is not None and dag.is_valid:
        if args.task_id in dag.tasks.keys():
            dag.run_task(args.task_id)
            dp = DagProcess(dag)
            dp.start()
        else:
            log.error(f'''No task [{args.task_id}] found in DAG [{dag.dag_id}]''')


def dag_show(args):
    dagbag = DagBag(args.dag_files_home)
    dag = dagbag.get_dag(args.dag_id)
    if dag is not None and dag.is_valid:
        html_page_path = os.path.join(args.dag_files_home,args.dag_id+".html")
        net = Network(directed=True)
        for child_task, parent_task_list in dag.tasks_flow.items():
            net.add_node(child_task.task_id)
            for parent_task in parent_task_list:
                net.add_node(parent_task.task_id)
                net.add_edge(parent_task.task_id, child_task.task_id)
        net.generate_html()
        with open(html_page_path, "w+") as out:
            out.write(net.html)
        webbrowser.open(html_page_path)


def dag_state(args):
    pass

def task_list(args):
    pass

def scheduler(args):
    pass