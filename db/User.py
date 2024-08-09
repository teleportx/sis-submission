from tortoise import fields
from tortoise.models import Model


class User(Model):
    uid = fields.BigIntField(pk=True, unique=True)
    subscription = fields.CharField(max_length=64, null=True, default=None)