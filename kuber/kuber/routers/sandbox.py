from typing import List

from dockerclient import sandbox
from fastapi import APIRouter
from pydantic import BaseModel, Json

router = APIRouter(prefix="/sandbox")


class Sandbox(BaseModel):
    name: str
    tag: str
    config: Json
    images: List[str] | None
    files: List[str]
    env_type: str
    project_name: str


@router.post("/")
def create_sandbox(sand: Sandbox):
    created, sandbox_name = sandbox.create_sandbox(
        name=sand.name,
        config=sand.config,
        files=sand.files,
        env_type=sand.env_type,
        project_name=sand.project_name,
        tag=sand.project_name,
        images=sand.images,
    )
    if created:
        return {"success": True, "sanboxes": sandbox_name}


@router.delete("/{sandbox_id}")
def delete_sandbox():
    pass


@router.post("/{sandbox_id}")
def stop_sandbox():
    pass


@router.post("/{sandbox_id}/container/{container_id}")
def stop_container():
    pass


@router.get("/{sandbox_id}/container_id/{container_id}/logs")
def get_container_logs():
    pass
