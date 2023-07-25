import io
import tarfile
from typing import Generator

from docker.errors import APIError, NotFound
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
) -> bool:
    cont = cli.containers.get(container_name)
    dir_check = cont.exec_run(f"test -d {path}")
    if dir_check.exit_code == 1:
        cont.exec_run(f"mkdir {path}")
    tar_stream = io.BytesIO()
    with tarfile.open(fileobj=tar_stream, mode="w") as tar_data:
        # Add the file to the archive
        tarinfo = tarfile.TarInfo(name=file_name)
        tarinfo.size = len(file_content)
        tar_data.addfile(tarinfo, io.BytesIO(file_content.encode("utf-8")))

    try:
        res = cont.put_archive(path, tar_stream.getvalue())
        return True
    except NotFound:
        res = cont.exec_run(f"touch {file_name}", workdir=path)  # noqa
        res = cont.put_archive(path, tar_stream.getvalue())  # noqa
        return True
    except APIError as e:
        print(f"Error upserting file to container: {e}")
        return False


def delete_file(container_name: str, file_name: str, path: str):
    cont = cli.containers.get(container_name)
    cont.exec_run(f"rm {file_name}", workdir=path)
    return True
