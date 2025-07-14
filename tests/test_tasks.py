import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_create_task():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/api/v1/tasks", json={
            "title": "Test Task",
            "description": "This is a test task",
            "completed": False
        }, params={"user_id": 1})
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "Test Task"
        assert data["description"] == "This is a test task"
        assert data["completed"] is False
        assert data["owner_id"] == 1

@pytest.mark.asyncio
async def test_get_tasks():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/api/v1/tasks", params={"user_id": 1})
        assert response.status_code == 200
        assert isinstance(response.json(), list)