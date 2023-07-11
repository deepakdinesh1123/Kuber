import definitions.logs_pb2 as logs_pb2
import definitions.logs_pb2_grpc as log_pb2_grpc
from dockerclient import logs


class Logs(log_pb2_grpc.LogsServicer):
    async def getDockerLogs(self, request, context):
        container_logs = logs.get_container_logs(request.container_name)
        for line in container_logs:
            yield logs_pb2.ContainerLogs(message=line)
