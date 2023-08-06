import io
import tarfile
from typing import Generator

from docker.errors import NotFound
from docker.models.containers import ExecResult
from dockerclient.client import cli
from utils.exceptions import FileNotFound


def get_file(container_name: str, file_name: str, path: str) -> ExecResult:
    cont = cli.containers.get(container_name)
    res = cont.exec_run(f"cat {file_name}", workdir=path, stream=True)
    if res.exit_code == 1:
        raise FileNotFound
    return res


def upsert_file(
    container_name: str, file_name: str, path: str, file_content: bytes
) -> ExecResult:
    cont = cli.containers.get(container_name)
    dir_check = cont.exec_run(f"test -d {path}")
    if dir_check.exit_code == 1:
        cont.exec_run(f"mkdir {path}")
    filobj = io.BytesIO(file_content.encode("utf-8"))
    tar_data = tarfile.open(fileobj=filobj, mode="w")
    tar_data.close()
    try:
        res = cont.put_archive(path, tar_data)
        print(f"result {res}")
        return True
    except NotFound:
        res = cont.exec_run(f"touch {file_name}", workdir=path)
        res = cont.put_archive(path, file_content)
    return True


def delete_file(container_name: str, file_name: str, path: str):
    cont = cli.containers.get(container_name)
    cont.exec_run(f"rm {file_name}", workdir=path)
    return True
