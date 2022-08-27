from fastapi import APIRouter
from app.data.events import events

router = APIRouter()

@router.get("/events")
def read_events():
    return events