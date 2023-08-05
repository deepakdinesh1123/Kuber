# import asyncio

# async def run_command(command, input_data=None):
#     process = await asyncio.create_subprocess_shell(
#         command,
#         stdin=asyncio.subprocess.PIPE,
#         stdout=asyncio.subprocess.PIPE,
#         stderr=asyncio.subprocess.PIPE,
#     )
#     process.stdin.write(input_data.encode())
#     process.stdin.close()
#     # Write input_data to stdin if provided

#     while True:
#         # Read stdout and stderr in a non-blocking way
#         stdout_bytes, stderr_bytes = await process.communicate()
#         stdout = stdout_bytes.decode().strip()
#         stderr = stderr_bytes.decode().strip()

#         if stdout:
#             print(f"stdout: {stdout}")
#         if stderr:
#             print(f"stderr: {stderr}")

#         # Check if the process has finished
#         if process.returncode is not None:
#             break

#     return process.returncode

# async def main():
#     command =  # Replace this with the command you want to run
#     input_data = "lol"  # Replace this with the data you want to write to stdin

#     returncode = await run_command(command, input_data=input_data)
#     print(f"Command exited with return code: {returncode}")

# # Run the asyncio event loop
# if __name__ == "__main__":
#     asyncio.run(main())

import asyncio
import signal


async def main():
    proc = await asyncio.subprocess.create_subprocess_shell(
        "docker exec -i nerdy-fuchsia-spider ps -a",
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
    )
    # proc.stdin.write(b"bob\n")
    stdout, _ = await proc.communicate()
    print(stdout.decode())
    # proc.stdin.write(b"alice\n")
    await proc.wait()


asyncio.run(main())
