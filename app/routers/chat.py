from fastapi import APIRouter, WebSocket, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..services import ell_ai
from ..core.security import verify_api_key

router = APIRouter()

@router.websocket("/ws")
async def websocket_endpoint(
    websocket: WebSocket,
    db: Session = Depends(get_db)
):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            response = await ell_ai.process_message(data["message"])
            await websocket.send_json(response)
    except Exception as e:
        await websocket.close(code=1000)

@router.post("/message")
async def send_message(
    message: str,
    db: Session = Depends(get_db)
):
    return await ell_ai.process_message(message)