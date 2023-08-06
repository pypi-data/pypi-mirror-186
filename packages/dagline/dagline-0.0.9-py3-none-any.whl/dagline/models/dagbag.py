import importlib.util
import os
import sys
from dagline.models.dag import DAG
from dagline.utils.logging_setup import LoggingMixin

class DagBag(LoggingMixin):
    def __init__(
    self,
    dag_files_home: str
    ):
        self.dags: dict[str, DAG] = {}
        self.mods = []
        file_paths = self.find_py_file_paths(dag_files_home)
        for file_path in file_paths:
            self.collect_dags_from_file(file_path)
        
        for m in self.mods:
            for o in m.__dict__.values():
                if isinstance(o, DAG):
                    if o.dag_id in self.dags:
                        self.log.error(f'''More than one DAG have the same dag_id [{o.dag_id}], make sure the dag_id is unique''')
                        self.dags[o.dag_id] = None
                    else:
                        self.dags[o.dag_id] = o
                    

    def collect_dags_from_file(self, file_path: str) -> None:
        module_name = os.path.splitext(os.path.split(file_path)[-1])[0]
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        self.mods.append(module)


    def find_py_file_paths(self, dag_files_home:str) -> list[str]:
        file_paths = []
        '''Add path of the DAG folder to sys path'''
        sys.path.append(dag_files_home)
        for root, dirs, files in os.walk(dag_files_home):
            for f in files:
                file_path = os.path.join(root, f)
                _, file_ext = os.path.splitext(os.path.split(file_path)[-1])
                if file_ext == ".py":
                    file_paths.append(file_path)
        return file_paths


    def get_dag(self, dag_id : str) -> DAG:
        dag = self.dags.get(dag_id, None)
        if dag is None:
            self.log.error(f'''No DAG [{dag_id}] found in dag_bag''')
        return dag
        
