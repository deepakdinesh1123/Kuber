import os
import re
import subprocess
import sys

import jwt


def remove_migrations():
    folders = os.listdir("./rest")
    for folder in folders:
        if os.path.exists(f"./rest/{folder}/migrations"):
            for obj in os.listdir(f"./rest/{folder}/migrations"):
                if (
                    os.path.isfile(f"./rest/{folder}/migrations/{obj}")
                    and obj != "__init__.py"
                ):
                    os.remove(f"./rest/{folder}/migrations/{obj}")


def generate_jwt(user_id):
    payload = {"user_id": user_id}
    secret_key = """MIIBVAIBADANBgkqhkiG9w0BAQEFAASCAT4wggE6AgEAAkEAwyBbW8AG8GvDakJj
GkA5A4TV3B+2BX2CD8rZtso3XBFVXgTfghQm+imXxqSYH0rCEWNVdFDrM0tCVLpu
eZIk3wIDAQABAkATJ+5xDnJ9bs69ROUg/RxiBclw3IkSmUQ4ZBn6B3j+kMS4zET1
x/NM5t5D4Ei9b+L+uqGY1twz1ybGzOSDPNEBAiEA2ZDRdoLayWkTh0US/ZQXEnfj
Hc2Ook0Xj3/YyHHsOekCIQCYA9fY9B9lTtjXwNf0NE9K/2NTmr/FtTV3/mfttA+X
mQIgc6vTh68eT07ITG0i6xCz/8tbeobvouIUPvpMgZ1QpB0CIQCGao34NcKbcV8B
JvsDT7xX2lgX35Mywd22MXvFFhiEBwIgCcJcE62EBT7jE7sGLdYK4xWDWl0WY4iH
/pV5nO/BqVE="""
    token = jwt.encode(payload, secret_key, algorithm="HS256")
    return token


def print_payload(token):
    secret_key = """MIIBVAIBADANBgkqhkiG9w0BAQEFAASCAT4wggE6AgEAAkEAwyBbW8AG8GvDakJj
GkA5A4TV3B+2BX2CD8rZtso3XBFVXgTfghQm+imXxqSYH0rCEWNVdFDrM0tCVLpu
eZIk3wIDAQABAkATJ+5xDnJ9bs69ROUg/RxiBclw3IkSmUQ4ZBn6B3j+kMS4zET1
x/NM5t5D4Ei9b+L+uqGY1twz1ybGzOSDPNEBAiEA2ZDRdoLayWkTh0US/ZQXEnfj
Hc2Ook0Xj3/YyHHsOekCIQCYA9fY9B9lTtjXwNf0NE9K/2NTmr/FtTV3/mfttA+X
mQIgc6vTh68eT07ITG0i6xCz/8tbeobvouIUPvpMgZ1QpB0CIQCGao34NcKbcV8B
JvsDT7xX2lgX35Mywd22MXvFFhiEBwIgCcJcE62EBT7jE7sGLdYK4xWDWl0WY4iH
/pV5nO/BqVE="""
    print(jwt.decode(token, secret_key, algorithms=["HS256"]))


def remove_images_with_prefix(prefix):
    try:
        # Get a list of Docker images and their information
        images_info = subprocess.check_output(
            ["docker", "images", "--format", "{{.Repository}}:{{.Tag}}"]
        )

        # Split the output into lines
        image_lines = images_info.decode().strip().split("\n")

        # Iterate through the image lines
        for line in image_lines:
            image_name, image_tag = line.split(":")

            # Check if the image name starts with the specified prefix
            if image_name.startswith(prefix):
                # Remove the image
                subprocess.call(["docker", "rmi", f"{image_name}:{image_tag}"])

        print(f"Removed Docker images with prefix: {prefix}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


def stop_and_remove_containers(image_name):
    # Get a list of all running containers with the specified image
    cmd_list = ["docker", "ps", "-a"]
    result = subprocess.run(
        cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )

    if result.returncode != 0:
        print("Error listing containers:", result.stderr)
        return

    containers = result.stdout.strip().split("\n")

    # Stop and remove each container
    for container_id in containers:
        print(f"Stopping and removing container: {container_id}")

        # Stop the container
        cmd_stop = ["docker", "stop", container_id]
        subprocess.run(cmd_stop)

        # Remove the container
        cmd_remove = ["docker", "rm", container_id]
        subprocess.run(cmd_remove)


if __name__ == "__main__":
    # action = sys.argv[1]
    # remove_migrations()
    print(generate_jwt("131f1f1e-129e-450f-9196-cb427834e7ff"))
    # print_payload("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMTMxZjFmMWUtMTI5ZS00NTBmLTkxOTYtY2I0Mjc4MzRlN2ZmIn0.p8Cj2fzhcl1VK_DDw6b1EeAeHYivKajoVVZ7_yIQXP4")
    stop_and_remove_containers("kuber-test")
    remove_images_with_prefix("kuber-test")
