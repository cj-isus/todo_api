from tortoise.models import Model
from tortoise import fields

class Task(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    description = fields.TextField()
    completed = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    owner = fields.ForeignKeyField("models.User", related_name="tasks")