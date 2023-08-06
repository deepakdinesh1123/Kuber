from typing import List

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
def create_sandbox(sandbox: Sandbox):
    pass


@router.delete("/{sandbox_id}")
def delete_sandbox():
    pass


@router.post("/{sandbox_id}")
def stop_sandbox():
    pass


@router.post("/{sandbox_id}/{container}")
def stop_container():
    pass


@router.get("/{sandbox_id}/{container}/logs")
def get_container_logs():
    pass
