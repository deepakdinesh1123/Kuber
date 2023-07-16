import os
import traceback
from typing import Generator, Iterable, List

import grpc
from definitions import sandbox_pb2, sandbox_pb2_grpc
from grpc_client.channel import grpc_channel
from utils.logger import log_error


def create_sandbox(
    name: str, tag: str, config: dict, images, files, type: str, projectName: str
) -> Generator[str, None, None]:
    try:
        stub = sandbox_pb2_grpc.SandboxStub(grpc_channel)
        request = sandbox_pb2.SandboxRequest(
            name=name,
            tag=tag,
            config=config,
            images=images,
            files=files,
            type=type,
            project_name=projectName,
        )

        response = stub.create_sandbox(request)
        return response
    except Exception:
        log_error(traceback.format_exc())
    return {"message": "", "success": False}
