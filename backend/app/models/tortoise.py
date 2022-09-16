from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator  # new

class Event(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    description = fields.CharField(max_length=255)
    location = fields.CharField(max_length=255)
    date = fields.DateField()
    time = fields.TimeField()
    organization = fields.CharField(max_length=255)
   # category = fields.CharField(max_length=255)

    def __str__(self):
        return self.title

EventSchema = pydantic_model_creator(Event)

class User(models.Model):
    uuid = fields.UUIDField(pk=True)
    username = fields.CharField(max_length=255, unique=True)
    first_name = fields.CharField(max_length=255)
    last_name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255, unique=True)
    disabled = fields.BooleanField(default=False)
    hashed_password = fields.CharField(max_length=255)

    def __str__(self):
        return self.username

UserSchema = pydantic_model_creator(User)
