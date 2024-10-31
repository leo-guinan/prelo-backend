from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from google.oauth2 import id_token
from google.auth.transport import requests
from ..core.config import settings
from ..database import get_db
from ..models.user import User
from ..services import magic_link

router = APIRouter()

@router.post("/google")
async def google_login(token: str, db: Session = Depends(get_db)):
    try:
        idinfo = id_token.verify_oauth2_token(
            token, requests.Request(), settings.GOOGLE_CLIENT_ID
        )
        return await create_or_get_user(db, idinfo)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid token")

@router.post("/magic-link")
async def request_magic_link(email: str, db: Session = Depends(get_db)):
    return await magic_link.send_login_link(email)

@router.post("/verify-magic-link")
async def verify_magic_link(token: str, db: Session = Depends(get_db)):
    email = magic_link.verify_token(token)
    if not email:
        raise HTTPException(status_code=400, detail="Invalid token")
    return await create_or_get_user(db, {"email": email})