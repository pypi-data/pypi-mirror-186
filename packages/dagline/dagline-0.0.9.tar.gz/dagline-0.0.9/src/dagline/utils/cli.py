from typing import Union, NamedTuple, Callable, Iterable
import argparse
from argparse import RawTextHelpFormatter
from importlib import import_module
    

def load_module_func(import_path: str) -> Callable:
    '''import_path -> eg. dagline.utils.commands.dag_command.dag_list_dags'''
    module_path, class_name = import_path.rsplit(".", 1)
    #To programmatically import a module
    module = import_module(module_path)
    return getattr(module, class_name)


class Arg:
    """Argument for per command line."""

    def __init__(
        self,
        flags : object(),
        help : object(),
        nargs : object() = None,
        default : object() = None
    ):
        self.flags = flags
        self.options = {}
        '''Assgin the optional arguments to a dic'''
        for k, v in locals().items():
            if k in ("self", "flags"):
                continue
            self.options[k] = v
            
    def add_to_parser(self, parser: argparse.ArgumentParser):
        """Add this argument to an ArgumentParser."""
        parser.add_argument(*self.flags, **self.options)


class ActionCommand(NamedTuple):
    """Single CLI command."""
    name: str
    help: str
    func: Callable
    args: Iterable[Arg]

    
class GroupCommand(NamedTuple):
    """ClI command with subcommands."""
    name: str
    help: str
    subcommands: Iterable


CLICommand = Union[ActionCommand, GroupCommand]

ARG_DAG_FILES_HOME = Arg(("dag_files_home",), help="The folder of the DAG files")
ARG_DAG_ID = Arg(("dag_id",), help="The id of the dag")
ARG_TASK_ID = Arg(("task_id",), help="The id of the task")
ARG_START_WITH_TASK_IDS = Arg(("--start_with_task_ids",), help="A list of the task ids", nargs='+', default=[])
# ARG_SUBDIR = Arg(
    # ("-S", "--subdir"),
    # help=(
        # "File location or directory from which to look for the dag. "
    # )
# )
# ARG_DAEMON = Arg(
    # ("-D", "--daemon"), help="Daemonize instead of running in the foreground"
# )
# ARG_STDERR = Arg(("--stderr",), help="Redirect stderr to this file")
# ARG_STDOUT = Arg(("--stdout",), help="Redirect stdout to this file")
# ARG_LOG_FILE = Arg(("-l", "--log-file"), help="Location of the log file")



DAGS_COMMANDS = (
    # ActionCommand(
        # name="list",
        # help="List all the DAGs",
        # func=load_module_func("dagline.utils.commands.dag_command.dag_list_dags"),
        # args=(ARG_SUBDIR,),
    # ),
    ActionCommand(
        name="show",
        help="Visualize the DAG in html page",
        func=load_module_func("dagline.utils.commands.dag_command.dag_show"),
        args=(ARG_DAG_FILES_HOME, ARG_DAG_ID, ),
    ),
    ActionCommand(
        name="run",
        help="Run a single DAG or run a single DAG from the specified tasks",
        func=load_module_func("dagline.utils.commands.dag_command.dag_run"),
        args=(ARG_DAG_FILES_HOME, ARG_DAG_ID, ARG_START_WITH_TASK_IDS),
    ),
)

TASKS_COMMANDS = (
    # ActionCommand(
        # name="list",
        # help="List the tasks within a DAG",
        # func=load_module_func("dagline.utils.commands.dag_command.task_list"),
        # args=(ARG_DAG_ID,),
    # ),
    ActionCommand(
        name="run",
        help="Run a single task instance",
        func=load_module_func("dagline.utils.commands.dag_command.task_run"),
        args=(
            ARG_DAG_FILES_HOME,
            ARG_DAG_ID,
            ARG_TASK_ID
        ),
    ),
)


dagline_commands: list[CLICommand] = [
    GroupCommand(
        name="dags",
        help="Manage DAGs",
        subcommands=DAGS_COMMANDS,
    ),
    GroupCommand(
        name="tasks",
        help="Manage tasks",
        subcommands=TASKS_COMMANDS,
    ),
    # ActionCommand(
        # name="scheduler",
        # help="Start a scheduler instance",
        # func=load_module_func("dagline.utils.commands.dag_command.scheduler"),
        # args=(
            # ARG_DAEMON,
            # ARG_STDOUT,
            # ARG_STDERR,
            # ARG_LOG_FILE
        # )
    # )
]


ALL_COMMANDS_DICT: dict[str, CLICommand] = {dc.name: dc for dc in dagline_commands}


def get_parser(dag_parser: bool = False) -> argparse.ArgumentParser:
    """Creates and returns command line argument parser.
       parser
            subparsers for ActionCommand
                sub_subparsers for GroupCommand
    """
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    subparsers.required = True

    command_dict = ALL_COMMANDS_DICT
    cmd_name_list = command_dict.keys()
    cmd_name: str
    for cmd_name in (cmd_name_list):
        cmd_obj: CLICommand = command_dict[cmd_name]
        _add_command(subparsers, cmd_obj)
    return parser


def _add_command(subparsers: argparse._SubParsersAction, cmd_obj: CLICommand) -> None:
    ''' add_parser for each one of commands'''
    sub_parser = subparsers.add_parser(
        cmd_obj.name, help=cmd_obj.help
    )
    sub_parser.formatter_class = RawTextHelpFormatter

    if isinstance(cmd_obj, GroupCommand):
        _add_group_command(cmd_obj, sub_parser)
    elif isinstance(cmd_obj, ActionCommand):
        _add_action_command(cmd_obj, sub_parser)
    else:
        pass


def _add_group_command(cmd_obj: GroupCommand, subparsers: argparse.ArgumentParser) -> None:
    subcommands = cmd_obj.subcommands
    sub_subparsers = subparsers.add_subparsers()
    sub_subparsers.required = True

    for command in subcommands:
        _add_command(sub_subparsers, command)
        
        
def _add_action_command(cmd_obj: ActionCommand, subparsers: argparse.ArgumentParser) -> None:
    for arg in (cmd_obj.args):
        arg.add_to_parser(subparsers)
    subparsers.set_defaults(func=cmd_obj.func)
    