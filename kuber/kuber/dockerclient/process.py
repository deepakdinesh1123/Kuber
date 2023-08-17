import asyncio
import traceback

from docker.models.containers import ExecResult
from dockerclient import container


def execute_command(name: str, cmd: str, dir: str) -> ExecResult:
    try:
        cont = container.get_container(name=name)
        output = cont.exec_run(cmd, workdir=dir, stream=True)
    except Exception:
        pass
    return output


class Process:
    def __init__(self, container_name, command, dir) -> None:
        self.container_name = container_name
        self.command = command
        self.dir = dir
        self.proc = None
        self.pid = None

    async def start(self):
        try:
            self.proc = await asyncio.subprocess.create_subprocess_shell(
                f"docker exec -i {self.container_name} {self.command}",
                cwd=self.dir,
                stdin=asyncio.subprocess.PIPE,
                stdout=asyncio.subprocess.PIPE,
            )
        except Exception as e:
            print(str(e))

    async def get_pid(self):
        tproc = await asyncio.subprocess.create_subprocess_shell(
            f"docker exec -i {self.container_name} pgrep -a .",
            stdout=asyncio.subprocess.PIPE,
        )
        stdout, _ = await tproc.communicate()
        lines = stdout.decode().split("\n")
        for line in lines:
            if line != "":
                details = line.split()
                pid = details[0]
                cmd = " ".join(details[1:])
                if cmd == self.command:
                    self.pid = pid
                    break

    async def is_alive(self) -> bool:
        if not self.pid:
            return False
        tproc = await asyncio.subprocess.create_subprocess_shell(
            f"docker exec -i {self.container_name} ps -q {self.pid} -o state --no-headers",
            stdout=asyncio.subprocess.PIPE,
        )
        stdout, err = await tproc.communicate()
        lines = stdout.decode().split("\n")
        print(f"lines - {lines}", err)
        if err:
            return False
        return True

    async def readline(self) -> str:
        try:
            line = await asyncio.wait_for(self.proc.stdout.readline(), timeout=1)
        except TimeoutError:
            return ""
        return line

    async def proc_kill(self) -> bool:
        tproc = await asyncio.subprocess.create_subprocess_shell(
            f"docker exec -i {self.container_name} kill {self.pid}",
            stdout=asyncio.subprocess.PIPE,
        )
        out = await tproc.wait()
        if out == 0:
            return True
        return False

    def write_input(self, input: str) -> bool:
        try:
            self.proc.stdin.write(f"{input}\n".encode("utf-8"))
            self.proc.stdin.write(b"\n")
            return True
        except Exception:
            return False

    def kill(self):
        try:
            self.proc.kill()
        except Exception:
            pass

    async def get_full_output(self):
        stdout, err = await self.proc.communicate()
        if not err:
            return stdout
        return err
