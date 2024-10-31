from fastapi import APIRouter, BackgroundTasks, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..services import ell_ai
from ..tasks.celery_tasks import execute_action

router = APIRouter()

@router.post("/execute")
async def execute_action_endpoint(
    action: dict,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    task = execute_action.delay(action)
    return {"task_id": task.id}

@router.get("/status/{task_id}")
async def get_action_status(task_id: str):
    task = execute_action.AsyncResult(task_id)
    return {"status": task.status, "result": task.result}