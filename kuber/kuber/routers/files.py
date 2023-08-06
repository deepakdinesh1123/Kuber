from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/sandbox")


@router.websocket("/files")
def files():
    pass
