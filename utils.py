import os
import re
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


if __name__ == "__main__":
    # action = sys.argv[1]
    # remove_migrations()
    print(generate_jwt("49438dd1-c87b-4d7e-a9db-a1d93e72554c"))
