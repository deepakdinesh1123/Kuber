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

import docker

client = docker.from_env()
print(type(client))
