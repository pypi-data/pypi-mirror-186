from dagline.models.task import Task
class WinbatOperator(Task):
    def __init__(
        self,
        task_id: str,
        bat_command: str
    ) -> None:
        super().__init__(task_id)
        self.bat_command = bat_command
