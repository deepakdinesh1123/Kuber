from pathlib import Path
from typing import Optional

from dockerclient.files import (
    create_folder,
    delete_file,
    delete_folder,
    get_file,
    get_folder,
    upsert_file,
)
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/sandbox")


class FileSystemItem(BaseModel):
    name: Optional[str] = None
    path: str
    content: Optional[str] = None


@router.get("/{sandbox_id}/container/{container_id}/file")
def get_file_from_container(sandbox_id, container_id, file: FileSystemItem):
    rfile = get_file(container_id, file_name=file.name, path=file.path)
    return {"success": True, "file": rfile}


@router.put("/{sandbox_id}/container/{container_id}/file")
async def upsert_file_into_container(sandbox_id, container_id, file: FileSystemItem):
    res = await upsert_file(
        container_id=container_id,
        file_name=file.name,
        path=file.path,
        file_content=file.content,
    )
    if res:
        return {"success": True}
    return {"success": False}


@router.post("/{sandbox_id}/container/{container_id}/file")
def delete_file_in_container(sandbox_id, container_id, file: FileSystemItem):
    res = delete_file(container_id, file.name, file.path)
    if res:
        return {"success": True}
    return {"sucess": False}


@router.post("/{sandbox_id}/container/{container_id}/folder")
def get_folder_from_container(sandbox_id, container_id, folder: FileSystemItem):
    res = get_folder(container_id, folder.path)
    if res:
        return {"success": True, "contents": res}


@router.put("/{sandbox_id}/container/{container_id}/folder")
def create_folder_in_container(sandbox_id, container_id, folder: FileSystemItem):
    res = create_folder(container_id, folder_name=folder.name, path=folder.path)
    if res:
        return {"success": True}
    return {"sucess": False}


@router.delete("/{sandbox_id}/container/{container_id}/folder")
def delete_folder_in_container(sandbox_id, container_id, folder: FileSystemItem):
    res = delete_folder(container_id, path=folder.path)
    if res:
        return {"success": True}
    return {"sucess": False}
