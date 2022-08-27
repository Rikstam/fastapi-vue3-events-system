from pydantic import BaseModel

class EventPayloadSchema(BaseModel):
    title: str

class EventResponseSchema(EventPayloadSchema):
    id: int