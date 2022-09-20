from typing import List
from fastapi import APIRouter, HTTPException, Path
from app.api import crud
from app.models.pydantic import (
    EventPayloadSchema,
    EventResponseSchema,
    EventUpdatePayloadSchema
)
from app.models.tortoise import EventSchema

router = APIRouter()

@router.post("/", response_model=EventResponseSchema, status_code=201)
async def create_event(payload: EventPayloadSchema) -> EventResponseSchema:
    event_id = await crud.post(payload)

    response_object = {
        "id": event_id,
        "title": payload.title,
        "description": payload.description,
        "location": payload.location,
        "date": payload.date,
        "time": payload.time,
        "organization": payload.organization,
        "category": payload.category,
        "user_id": payload.user_id
    }
    return response_object

@router.get("/{id}/", response_model=EventResponseSchema)
async def read_event(id: int = Path(..., gt=0)) -> EventResponseSchema:
    event = await crud.get(id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    return event

@router.delete("/{id}/", response_model=EventResponseSchema)
async def delete_event(id: int) -> EventResponseSchema:
    event = await crud.get(id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    await crud.delete(id)

    return event

@router.get("/", response_model=List[EventResponseSchema])
async def read_all_events() -> List[EventResponseSchema]:
    return await crud.get_all()

@router.put("/{id}/", response_model=EventSchema)
async def update_event(id: int, payload: EventUpdatePayloadSchema) -> EventSchema:
    event = await crud.put(id, payload)
    if not event:
        raise HTTPException(status_code=404, detail="event not found")

    return event
