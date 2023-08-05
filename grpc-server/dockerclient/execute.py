import asyncio
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


class Process:
    def __init__(self, container_name, command, dir) -> None:
        self.container_name = container_name
        self.command = command
        self.dir = dir
        self.proc = None
        self.pid = None

    async def start(self):
        self.proc = await asyncio.subprocess.create_subprocess_shell(
            f"docker exec -it {self.container_name} {self.command}", cwd=self.dir
        )

    async def get_pid(self):
        tproc = await asyncio.subprocess.create_subprocess_shell(
            f"docker exec -it {self.container_name} pgrep -a ."
        )
        stdout, _ = tproc.communicate()
        lines = stdout.decode().split("\n")
        for line in lines:
            details = line.split()
            pid = details[1]
            cmd = " ".join(details[1:])
            if cmd == self.command:
                self.pid = pid
                break

    async def is_alive(self) -> bool:
        tproc = await asyncio.subprocess.create_subprocess_shell(
            f"docker exec -it {self.container_name} ps -p {self.pid}"
        )
        stdout, _ = tproc.communicate()
        lines = stdout.decode().split("\n")
        if len(lines) == 1:
            return False
        return True

    async def readline(self) -> str:
        line = await self.proc.stdout.readline()
        return line

    def write_input(self, input: str) -> bool:
        try:
            self.proc.stdin.write(input)
            return True
        except Exception:
            return False

    def kill(self):
        try:
            self.proc.kill()
        except Exception:
            pass
