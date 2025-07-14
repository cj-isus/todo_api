from tortoise.models import Model
from tortoise import fields

class Project(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    description = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    owner = fields.ForeignKeyField("models.User", related_name="projects")
    tasks = fields.ManyToManyField("models.Task", related_name="projects")