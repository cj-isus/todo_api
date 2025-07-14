from fastapi import APIRouter, HTTPException
from app.models.project import Project
from app.models.user import User
from app.schemas.project import ProjectCreate, ProjectResponse
from typing import List

router = APIRouter()

@router.post("/projects", response_model=ProjectResponse)
async def create_project(project: ProjectCreate, user_id: int = 1):
    user = await User.get_or_none(id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    new_project = await Project.create(
        name=project.name,
        description=project.description,
        owner=user
    )
    return new_project

@router.get("/projects", response_model=List[ProjectResponse])
async def get_projects(user_id: int = 1):
    user = await User.get_or_none(id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return await Project.filter(owner=user).all()