from fastapi import FastAPI
from app.database import init_db
from app.api.v1.auth import router as auth_router

app = FastAPI()

app.include_router(auth_router, prefix="/api/v1/auth", tags=["auth"])

@app.on_event("startup")
async def startup_event():
    await init_db()

@app.get("/")
async def root():
    return {"message": "To-Do API"}