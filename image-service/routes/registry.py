import io
import json
import os
from typing import Annotated

from docker_client import client
from dotenv import load_dotenv
from fastapi import APIRouter, File, Form, HTTPException
from pydantic import BaseModel, ValidationError

load_dotenv()

router = APIRouter()


class ImageDetails(BaseModel):
    image_name: str
    image_tag: str
    creator: str
    repo_name: str


@router.post("/push_image/")
def push_image(file: Annotated[bytes, File()], image_details: Annotated[str, Form()]):
    print(os.environ.get("DOCKER_HUB_USERNAME"))
    try:
        details = ImageDetails(**json.loads(image_details))
        details = details.dict()
        file_obj = io.BytesIO(file)
    except ValidationError:
        raise HTTPException(status_code=401, detail="Provided details are invalid")
    image_name = details["image_name"]
    image_tag = details["image_tag"]
    img, logs = client.images.build(
        fileobj=file_obj, tag=f"deepakdinesh/{image_name}:{image_tag}"
    )
    img.tag(f"deepakdinesh/{image_name}:{image_tag}")
    resp = client.images.push(
        repository=f"deepakdinesh/{image_name}:{image_tag}",
        auth_config={
            "username": os.environ.get("DOCKER_HUB_USERNAME"),
            "password": os.environ.get("DOCKER_HUB_PASSWORD"),
        },
    )
    return resp
