from app.models.pydantic import EventPayloadSchema
from app.models.tortoise import Event


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