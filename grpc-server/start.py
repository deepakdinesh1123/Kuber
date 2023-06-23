import os
import time
from subprocess import Popen

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

# Define the gRPC server startup command
SERVER_COMMAND = ["python", "main.py"]

# Define the directory to monitor for changes
DIRECTORY_TO_WATCH = "."

# Define the cooldown period in seconds
RESTART_COOLDOWN = 5


# Define the event handler for file changes
class FileChangeHandler(FileSystemEventHandler):
    def __init__(self):
        self.last_restart_time = 0

    def on_modified(self, event):
        current_time = time.time()
        if current_time - self.last_restart_time > RESTART_COOLDOWN:
            # Restart the gRPC server
            restart_grpc_server()
            self.last_restart_time = current_time


# Start the gRPC server
def start_grpc_server():
    global server_process
    server_process = Popen(SERVER_COMMAND)


# Restart the gRPC server
def restart_grpc_server():
    global server_process
    server_process.terminate()
    server_process.wait()
    start_grpc_server()
    print("res")


# Initialize the file change handler and observer
event_handler = FileChangeHandler()
observer = Observer()
observer.schedule(event_handler, path=DIRECTORY_TO_WATCH, recursive=True)

# Start the gRPC server initially
start_grpc_server()

try:
    # Start the file monitoring loop
    observer.start()

    while True:
        time.sleep(1)

except KeyboardInterrupt:
    observer.stop()

observer.join()
