from tortoise import fields
from tortoise.models import Model
from tortoise.validators import MinLengthValidator

class Project(Model):
    id = fields.BigIntField(primary_key=True)
    title = fields.CharField(max_length=255, validators=[MinLengthValidator(1)])
    description = fields.TextField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(null=True)
    user_id = fields.BigIntField()
    user: fields.ForeignKeyRelation["src.db.models.User"] = fields.ForeignKeyField("models.User", related_name="projects")
    tasks: fields.ManyToManyRelation["src.db.models.Task"] = fields.ManyToManyField("models.Task", through="task_project", related_name="projects")
    class Meta:
        table = "projects"
        schema = "todo"
