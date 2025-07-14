import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_create_project():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/api/v1/projects", json={
            "name": "Test Project",
            "description": "This is a test project"
        }, params={"user_id": 1})
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == "Test Project"
        assert data["description"] == "This is a test project"
        assert data["owner_id"] == 1

@pytest.mark.asyncio
async def test_get_projects():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/api/v1/projects", params={"user_id": 1})
        assert response.status_code == 200
        assert isinstance(response.json(), list)