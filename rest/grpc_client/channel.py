import os

import grpc

GRPC_HOST = os.getenv("GRPC_HOST")
GRPC_PORT = os.getenv("GRPC_PORT")

grpc_channel = grpc.insecure_channel(f"{GRPC_HOST}:{GRPC_PORT}")
