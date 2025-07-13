from fastapi import APIRouter, HTTPException
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import get_password_hash

router = APIRouter()

@router.post("/register", response_model=dict)
async def register(user: UserCreate):
    existing_user = await User.get_or_none(username=user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    hashed_password = get_password_hash(user.password)
    new_user = await User.create(username=user.username, password_hash=hashed_password)
    return {"id": new_user.id, "username": new_user.username}