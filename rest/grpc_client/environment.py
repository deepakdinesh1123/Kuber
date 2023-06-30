import os
import traceback
from typing import Generator, Iterable, List

import grpc
from definitions import environment_pb2, environment_pb2_grpc
from grpc_client.channel import grpc_channel
from utils.logger import log_error


def create_environment(
    name: str, tag: str, config: dict, images, files, type: str, projectName: str
) -> Generator[str, None, None]:
    try:
        stub = environment_pb2_grpc.environmentStub(grpc_channel)
        request = environment_pb2.EnvironmentRequest(
            name=name,
            tag=tag,
            config=config,
            images=images,
            files=files,
            type=type,
            project_name=projectName,
        )

        response_stream = stub.createEnvironment(request)
        return response_stream
    except Exception:
        log_error(traceback.format_exc())
    return None
