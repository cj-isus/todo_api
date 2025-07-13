from tortoise import Tortoise
from app.core.config import settings

async def init_db():
    await Tortoise.init(
        db_url=settings.DATABASE_URL,
        modules={"models": ["app.models.user", "app.models.task", "app.models.project"]}
    )
    await Tortoise.generate_schemas()