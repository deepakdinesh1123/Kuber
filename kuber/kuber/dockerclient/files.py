import asyncio
import io
import shlex
import tarfile
from typing import Generator

from docker.errors import NotFound
from docker.models.containers import ExecResult
from dockerclient.client import cli
from utils.exceptions import FileNotFound


def get_file(container_id: str, file_name: str, path: str) -> ExecResult:
    cont = cli.containers.get(container_id)
    res = cont.exec_run(f"cat {file_name}", workdir=path)
    if res.exit_code == 1:
        raise FileNotFound
    return res.output


async def upsert_file(
    container_id: str, file_name: str, path: str, file_content: bytes
) -> bool:
    cont = cli.containers.get(container_id)
    dir_check = cont.exec_run(f"test -d {path}")
    if dir_check.exit_code == 1:
        cont.exec_run(f"mkdir {path}")
    res = await asyncio.subprocess.create_subprocess_shell(
        f"docker exec -i {container_id} sh -c 'cd {path} && echo {file_content} >> {file_name}'"
    )
    out, _ = await res.communicate()
    return True


def delete_file(container_id: str, file_name: str, path: str):
    cont = cli.containers.get(container_id)
    cont.exec_run(f"rm {file_name}", workdir=path)
    return True


def get_folder(container_id: str, path: str) -> str | None:
    cont = cli.containers.get(container_id)
    dir_check = cont.exec_run(f"test -d {path}")
    if dir_check.exit_code == 1:
        return None
    exit_code, out = cont.exec_run(f"ls {path}")
    return out


def create_folder(container_id: str, path: str, folder_name: str):
    cont = cli.containers.get(container_id)
    res = cont.exec_run(f"mkdir {folder_name}", workdir=path)
    if res.exit_code == 0:
        return True
    return False


def delete_folder(container_id: str, path: str) -> bool:
    cont = cli.containers.get(container_id)
    dir_check = cont.exec_run(f"test -d {path}")
    if dir_check.exit_code == 1:
        return False
    res = cont.exec_run(f"rm -rf {path}")
    if res.exit_code == 1:
        return False
    return True
