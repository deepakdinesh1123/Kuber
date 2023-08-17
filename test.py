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
# import asyncio


# async def main():
#     proc = await asyncio.subprocess.create_subprocess_shell(
#         "docker exec -i nerdy-fuchsia-spider sh inf.sh",
#         stdin=asyncio.subprocess.PIPE,
#         stdout=asyncio.subprocess.PIPE,
#     )
#     proc.stdin.write(b"bob\n")
#     # print(await proc.stdout.read(1024))
#     # proc.stdin.write(b"alice\n")
#     # print(await proc.stdout.read(1024))
#     # proc.stdin.write(b"quit\n")
#     await proc.wait()


# asyncio.run(main())

# import socket


# def find_unused_port():
#     # Create a socket object
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.bind(("localhost", 0))  # Bind to an available port on localhost
#     _, port = sock.getsockname()  # Get the allocated port
#     sock.close()  # Close the socket

#     return port


# if __name__ == "__main__":
#     unused_port = find_unused_port()
#     print(f"An available unused port: {unused_port}")

import asyncio

AWAIT_TIME = 5.0


async def expensive_function():
    """this is something which takes a lot of time"""
    await asyncio.sleep(10)
    result = 10

    return result


def callback(fut: asyncio.Future):
    """just prints result. Callback should be sync function"""
    if not fut.cancelled() and fut.done():
        print(fut.result())
    else:
        print("No results")


async def amain():
    """Main async func in the app"""
    # create task
    task = asyncio.create_task(expensive_function())
    task.add_done_callback(callback)
    # try to await the task
    try:
        r = await asyncio.wait_for(task, timeout=AWAIT_TIME)
    except asyncio.TimeoutError as ex:
        print(ex)
    else:
        print(f"All work done fine: {r}")
    finally:
        print("App finished!")


if __name__ == "__main__":
    asyncio.run(amain())
