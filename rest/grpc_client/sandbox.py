import os
import traceback
from typing import Generator, Iterable, List

import grpc
from definitions import sandbox_pb2, sandbox_pb2_grpc
from grpc_client.channel import grpc_channel
from utils.logger import log_debug, log_error


def create_sandbox(
    name: str, tag: str, config: dict, images, files, env_type: str, projectName: str
) -> dict:
    log_debug([name, config, images, files])
    try:
        stub = sandbox_pb2_grpc.SandboxStub(grpc_channel)
        request = sandbox_pb2.SandboxRequest(
            name=name,
            tag=tag,
            config=str(config),
            images=[images],
            files=[files],
            env_type=env_type,
            project_name=projectName,
        )

        response = stub.create_sandbox(request)
        return response
    except Exception:
        log_error(traceback.format_exc())
    return {"message": "Sandbox could not be created", "success": False}
