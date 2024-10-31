from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..services import ell_ai

router = APIRouter()

@router.post("/create")
async def create_submind(
    config: dict,
    db: Session = Depends(get_db)
):
    return await ell_ai.create_submind(config)

@router.get("/list")
async def list_subminds(db: Session = Depends(get_db)):
    return await ell_ai.list_subminds()