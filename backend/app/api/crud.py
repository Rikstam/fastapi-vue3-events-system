from app.models.pydantic import EventPayloadSchema
from app.models.tortoise import Event
from typing import Union, List

async def post(payload: EventPayloadSchema) -> int:
    event = Event(
       title=payload.title,
       description=payload.description,
       location=payload.location,
       date=payload.date,
       time=payload.time,
       organization=payload.organization
    )
    await event.save()
    return event.id

async def get(id: int) -> Union[dict, None]:
    event = await Event.filter(id=id).first().values()
    if event:
        return event
    return None

async def get_all() -> List:
    events = await Event.all().values()
    return events
