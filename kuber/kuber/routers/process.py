import asyncio
from asyncio.exceptions import TimeoutError

from dockerclient.process import Process
from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter(prefix="/sandbox")


@router.websocket("/process")
async def start_process(ws: WebSocket):
    await ws.accept()
    try:
        data = await ws.receive_json()
        proc = Process(
            container_name=data["container_name"],
            command=data["command"],
            dir=data["dir"],
        )
        await proc.start()
        await proc.get_pid()
        await ws.send_json({"status": "process started", "pid": proc.pid})
        while True:
            data = await ws.receive_json()
            if data["action"] == "stdin":
                proc.write_input(data["input"].encode("utf-8"))
            elif data["action"] == "kill":
                await proc.proc_kill()
            elif data["action"] == "read":
                if not await proc.is_alive():
                    out = await proc.get_full_output()
                    await ws.send_json({"out": out.decode()})
                    proc.kill()
                    await ws.close()
                    return
                out = await proc.readline()
                # if out == b"" and not await proc.is_alive():
                #     proc.kill()
                #     await ws.close()
                #     return
                # if out == "":
                #     pass
                await ws.send_json({"out": out.decode()})
    except WebSocketDisconnect:
        await proc.proc_kill()
        proc.kill()
