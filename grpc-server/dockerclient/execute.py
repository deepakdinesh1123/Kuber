import traceback

from docker.models.containers import ExecResult
from dockerclient import container, files
from utils.logger import log_debug


def execute_command(name: str, cmd: str, dir: str) -> ExecResult:
    try:
        cont = container.get_container(name=name)
        output = cont.exec_run(cmd, workdir=dir, stream=True)
    except Exception:
        log_debug(traceback.format_exc())
    return output


def execute_test(
    container_name: str,
    test_cmd: str,
    test_dir: str,
    test_script: str,
    test_script_name: str,
    test_script_path: str,
) -> bool:
    if not files.upsert_file(
        container_name, test_script_name, test_script_path, test_script
    ):
        return False
    try:
        cont = container.get_container(name=container_name)
        exit_code, output = cont.exec_run(test_cmd, workdir=test_dir)
    except Exception:
        log_debug(traceback.format_exc())
    files.delete_file(container_name, test_script_name, test_script_path)
    return exit_code
