import traceback

import definitions.execute_pb2 as exe_pb2
import definitions.execute_pb2_grpc as exe_grpc
from dockerclient import execute
from utils.logger import log_debug


class Execute(exe_grpc.ExecuteServicer):
    async def execute_command(self, request, context):
        try:
            res = execute.exec_cmd(
                name=request.container_name, cmd=request.command, dir=request.dir
            )
            for line in res.output:
                yield exe_pb2.ExecutionResponse(message=line)
        except Exception:
            pass

    def execute_test(self, request, context):
        res = execute.execute_test(
            container_name=request.container_name,
            test_cmd=request.test_cmd,
            test_dir=request.test_dir,
            test_script=request.test_script,
            test_script_name=request.test_script_name,
            test_script_path=request.test_script_dir,
        )
        if res != 0:
            return exe_pb2.TestResult(result="Unsuccessful", success=False)
        return exe_pb2.TestResult(result="successful", success=True)
