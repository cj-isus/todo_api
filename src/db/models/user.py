from tortoise import fields
from tortoise.models import Model
from tortoise.validators import MinLengthValidator, RegexValidator
from .task import Task

class User(Model):
    id = fields.BigIntField(primary_key=True)
    username = fields.CharField(max_length=50, unique=True, validators=[MinLengthValidator(3)])
    email = fields.CharField(
        max_length=255,
        unique=True,
        validators=[RegexValidator(
            pattern=r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$',
            flags=0
        )]
    )
    password_hash = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(null=True)

    tasks: fields.ReverseRelation["Task"]

    class Meta:
        table = "users"
        schema = "todo"