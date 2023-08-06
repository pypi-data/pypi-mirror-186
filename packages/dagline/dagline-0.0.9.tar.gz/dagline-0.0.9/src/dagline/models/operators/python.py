from typing import Callable
from dagline.models.task import Task

class PythonOperator(Task):
    def __init__(
        self,
        task_id: str,
        python_callable: Callable
    ) -> None:
        super().__init__(task_id)
        self.python_callable = python_callable
