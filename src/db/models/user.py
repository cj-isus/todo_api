# Импорт необходимых модулей из Tortoise ORM
from tortoise import fields
from tortoise.models import Model
from tortoise.validators import MinLengthValidator, RegexValidator

# Определение модели User
class User(Model):
    # Уникальный идентификатор пользователя
    id = fields.BigIntField(pk=True)
    # Уникальное имя пользователя, минимум 3 символа
    username = fields.CharField(max_length=50, unique=True, validators=[MinLengthValidator(3)])
    # Уникальный email, максимум 255 символов, с валидацией формата
    email = fields.CharField(max_length=255, unique=True, validators=[RegexValidator(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', 'Invalid email format')])
    # Хэш пароля
    password_hash = fields.CharField(max_length=255)
    # Дата и время создания
    created_at = fields.DatetimeField(auto_now_add=True)
    # Дата и время последнего обновления
    updated_at = fields.DatetimeField(null=True)

    # Связь с проектами (обратная сторона)
    projects: fields.ReverseRelation["Project"]
    # Связь с задачами (обратная сторона)
    tasks: fields.ReverseRelation["Task"]
    # Связь с тегами (обратная сторона)
    tags: fields.ReverseRelation["Tag"]
    # Связь с логами (обратная сторона)
    logs: fields.ReverseRelation["Log"]

    class Meta:
        table = "users"
        schema = "todo"

# Для предотвращения циклических импортов
import src.db.models.project
import src.db.models.task
import src.db.models.tag
import src.db.models.log