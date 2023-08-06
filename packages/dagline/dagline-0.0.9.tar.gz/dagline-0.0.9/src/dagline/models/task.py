class Task:

    def __init__(self, task_id: str):
        self.task_id = task_id
        self.upstream : List = []
        self.downstream: List = []
        self.state : str = None
        self.exec_ouput : str = None
