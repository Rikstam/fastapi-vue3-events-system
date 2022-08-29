from fastapi import APIRouter, HTTPException
from app.data.events import events
from app.api import crud
from app.models.pydantic import EventPayloadSchema, EventResponseSchema
from app.models.tortoise import EventSchema

router = APIRouter()

@router.post("/", response_model=EventResponseSchema, status_code=201)
async def create_summary(payload: EventPayloadSchema) -> EventResponseSchema:
    event_id = await crud.post(payload)

    response_object = {
        "id": event_id,
        "title": payload.title,
        "description": payload.description,
        "location": payload.location,
        "date": payload.date,
        "time": payload.time,
        "organization": payload.organization
    }
    return response_object

@router.get("/{id}/", response_model=EventSchema)
async def read_summary(id: int) -> EventSchema:
    event = await crud.get(id)

    return event


@router.get("/events")
def read_events():
    return events