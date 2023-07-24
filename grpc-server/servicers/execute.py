import traceback

import definitions.execute_pb2 as exe_pb2
import definitions.execute_pb2_grpc as exe_grpc
from dockerclient.execute import execute_command as exec_cmd
from utils.logger import log_debug


class Execute(exe_grpc.ExecuteServicer):
    async def execute_command(self, request, context):
        try:
            res = exec_cmd(
                name=request.container_name, cmd=request.command, dir=request.dir
            )
            for line in res.output:
                yield exe_pb2.ExecutionResponse(message=line)
        except Exception:
            pass
