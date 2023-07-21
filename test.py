# from pydantic import BaseModel
# from typing import List
# import json

# class User(BaseModel):
#     image_name: str
#     image_tag: str
#     creator: str
#     repo_name: str

# user_dict = """
# {
# 	"image_name": "test",
# 	"image_tag": "latest",
# 	"creator": "lol",
# 	"repo_name": " something"
# }
# """

# user = User(**json.loads(user_dict))

# print(user.dict())

# import io

# import docker

# client = docker.from_env()

# fil = io.BytesIO(b"FROM python:3.10")
# client.images.build(fileobj=fil, tag="kuber-test")
# import grpc
# from rest.definitions import sandbox_pb2, sandbox_pb2_grpc


# def create_sandbox_client():
#     # Create a gRPC channel to connect to the server
#     channel = grpc.insecure_channel(
#         "localhost:50051"
#     )  # Replace with the appropriate server address and port

#     # Create a stub (client) using the generated code
#     stub = sandbox_pb2_grpc.SandboxStub(channel)

#     # Prepare the request message with sample data
#     request = sandbox_pb2.SandboxRequest(
#         name="My Sandbox",
#         tag="v1.0",
#         config="{}",
#         images=["image1", "image2"],
#         files=["file1", "file2"],
#         type="sandbox_type",
#         project_name="My Project",
#     )

#     # Call the create_sandbox RPC
#     response = stub.create_sandbox(request)

#     # Process the response
#     if response.success:
#         print("Sandbox created successfully!")
#         print("Containers:", response.containers)
#     else:
#         print("Sandbox creation failed.")
#     print("Message:", response.message)


# if __name__ == "__main__":
#     create_sandbox_client()
