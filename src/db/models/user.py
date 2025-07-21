# Импорт необходимых модулей из Tortoise ORM
from tortoise import fields
from tortoise.models import Model
from tortoise.validators import MinLengthValidator, RegexValidator

# Определение модели User
class User(Model):
    # Уникальный идентификатор пользователя
    id = fields.BigIntField(primary_key=True)
    # Уникальное имя пользователя, минимум 3 символа
    username = fields.CharField(max_length=50, unique=True, validators=[MinLengthValidator(3)])
    # Уникальный email, максимум 255 символов (валидация временно удалена)
    email = fields.CharField(max_length=255, unique=True)  # Временное удаление валидатора
    # Хэш пароля
    password_hash = fields.CharField(max_length=255)
    # Дата и время создания
    created_at = fields.DatetimeField(auto_now_add=True)
    # Дата и время последнего обновления
    updated_at = fields.DatetimeField(null=True)

    # Связь с проектами (обратная сторона)
    projects: fields.ReverseRelation["src.db.models.Project"]
    # Связь с задачами (обратная сторона)
    tasks: fields.ReverseRelation["src.db.models.Task"]
    # Связь с тегами (обратная сторона)
    tags: fields.ReverseRelation["src.db.models.Tag"]
    # Связь с логами (обратная сторона)
    logs: fields.ReverseRelation["src.db.models.Log"]

    class Meta:
        table = "users"
        schema = "todo"