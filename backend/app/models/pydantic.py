from pydantic import UUID4,BaseModel
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

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class UserPayLoadSchema(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str

class UserResponseSchema(BaseModel):
    uuid: UUID4
    username: str
    email: str
    first_name: str
    last_name: str