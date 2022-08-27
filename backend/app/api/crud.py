from app.models.pydantic import EventPayloadSchema
from app.models.tortoise import Event


async def post(payload: EventPayloadSchema) -> int:
    event = Event(
       title=payload.title,
       description="dummy description",
       location="dunmmy location",
       date="2022-12-24",
       time="10:00",
       organization="dummy organization"
    )
    await event.save()
    return event.id