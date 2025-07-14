from fastapi import APIRouter, HTTPException
from app.models.task import Task
from app.models.user import User
from app.schemas.task import TaskCreate, TaskResponse
from typing import List

router = APIRouter()

@router.post("/tasks", response_model=TaskResponse)
async def create_task(task: TaskCreate, user_id: int = 1):
    user = await User.get_or_none(id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    new_task = await Task.create(
        title=task.title,
        description=task.description,
        completed=task.completed,
        owner=user
    )
    return new_task

@router.get("/tasks", response_model=List[TaskResponse])
async def get_tasks(user_id: int = 1):
    user = await User.get_or_none(id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return await Task.filter(owner=user).all()