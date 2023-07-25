import traceback

from docker.models.containers import ExecResult
from dockerclient import container
from utils.logger import log_debug


def execute_command(name: str, cmd: str, dir: str) -> ExecResult:
    try:
        cont = container.get_container(name=name)
        output = cont.exec_run(cmd, workdir=dir, stream=True)
    except Exception:
        log_debug(traceback.format_exc())
    return output
