from typing import Generator

from dockerclient import container


def execute_command(name: str, cmd: str, dir: str) -> Generator[str, None, None]:
    cont = container.get_container(name=name)
    exit_code, output = cont.exec_run(cmd, workdir=dir, stream=True, detach=True)
    return output
