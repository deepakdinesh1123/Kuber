from time import sleep

import definitions.uptime_pb2 as up_pb2
import definitions.uptime_pb2_grpc as up_pb2_grpc
from dockerclient.container import is_container_running


class UptimeServicer(up_pb2_grpc.ContainerUptimeServicer):
    def get_container_status(self, request, context):
        while is_container_running(request.name):
            yield up_pb2.Response(success=True)
            sleep(5)  # Add a short delay to avoid busy-waiting and reduce CPU usage

        return up_pb2.Response(success=False)
