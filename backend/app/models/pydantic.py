from pydantic import BaseModel
from datetime import time, date
class EventPayloadSchema(BaseModel):
    title: str
    description: str
    location: str
    date: date
    time: time
    organization: str

class EventResponseSchema(EventPayloadSchema):
    id: int

class EventUpdatePayloadSchema(EventPayloadSchema):
    pass
