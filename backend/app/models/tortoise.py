from tortoise import fields, models


class Event(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    description = fields.CharField(max_length=255)
    location = fields.CharField(max_length=255)
    date = fields.DateField()
    time = fields.TimeField()
    organization = fields.CharField(max_length=255)

    def __str__(self):
        return self.title