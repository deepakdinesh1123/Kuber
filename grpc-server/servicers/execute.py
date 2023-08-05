import asyncio
import traceback

import definitions.execute_pb2 as exe_pb2
import definitions.execute_pb2_grpc as exe_grpc
from dockerclient.execute import execute_command as exec_cmd
from utils.logger import log_debug


class Execute(exe_grpc.ExecuteServicer):
    async def execute_command(self, request_iterator, context):
        async for request in request_iterator:
            yield exe_pb2.ExecutionResponse(message=request.container_name)
