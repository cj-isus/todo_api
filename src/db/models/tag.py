from tortoise import fields
from tortoise.models import Model
from tortoise.validators import MinLengthValidator

class Tag(Model):
    id = fields.BigIntField(primary_key=True)
    name = fields.CharField(max_length=50, validators=[MinLengthValidator(1)])
    description = fields.TextField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(null=True)
    user_id = fields.BigIntField()
    user: fields.ForeignKeyRelation["src.db.models.User"] = fields.ForeignKeyField("models.User", related_name="tags")
    tasks: fields.ManyToManyRelation["src.db.models.Task"] = fields.ManyToManyField("models.Task", through="task_tag", related_name="tags")
    class Meta:
        table = "tags"
        schema = "todo"
