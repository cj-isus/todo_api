# Импорт необходимых модулей
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
import os

# Загрузка переменных из .env
load_dotenv("C:\\Users\\Катя\\PycharmProjects\\todo_api\\.env")
print(f"Loaded environment variables: {dict(os.environ)}")  # Отладка

# Определение класса настроек
class Settings(BaseSettings):
    # URL базы данных, загружается из переменной окружения DATABASE_URL
    DATABASE_URL: str
    # Секретный ключ, загружается из переменной окружения SECRET_KEY
    SECRET_KEY: str

    # Конфигурация для загрузки из окружения
    model_config = SettingsConfigDict(
        env_file=None,
        env_file_encoding="utf-8",
        env_prefix="",
        case_sensitive=False
    )

# Создание экземпляра настроек
settings = Settings(_env_file=None)