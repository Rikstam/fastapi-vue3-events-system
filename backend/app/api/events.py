from fastapi import APIRouter, HTTPException
from app.data.events import events
from app.api import crud
from app.models.pydantic import EventPayloadSchema, EventResponseSchema

router = APIRouter()

@router.post("/", response_model=EventResponseSchema, status_code=201)
async def create_summary(payload: EventPayloadSchema) -> EventResponseSchema:
    event_id = await crud.post(payload)

    response_object = {
        "id": event_id,
        "title": payload.title
    }
    return response_object


@router.get("/events")
def read_events():
    return events