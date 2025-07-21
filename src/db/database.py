# Импорт Tortoise ORM и настроек
from tortoise import Tortoise
from src.config.settings import settings

# Инициализация базы данных
async def init_db():
    print(f"Initializing database with URL: {settings.DATABASE_URL}")
    await Tortoise.init(
        db_url=settings.DATABASE_URL,
        modules={"models": ["src.db.models"]}
    )
    print("Generating schemas...")
    await Tortoise.generate_schemas(safe=True)
    print("Database initialized and schemas generated.")

# Закрытие соединения с базой данных
async def close_db():
    await Tortoise.close_connections()