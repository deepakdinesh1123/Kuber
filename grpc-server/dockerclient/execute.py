import traceback
from typing import Generator

from dockerclient import container
from utils.logger import log_debug


def execute_command(name: str, cmd: str, dir: str) -> Generator[str, None, None]:
    try:
        cont = container.get_container(name=name)
        log_debug(cont)
        output = cont.exec_run(cmd, workdir=dir, stream=True)
    except Exception:
        log_debug(traceback.format_exc())
    return output
