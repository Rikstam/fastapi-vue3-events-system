from typing import Union
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import ping
from app.api import events
from app.db import init_db

log = logging.getLogger("uvicorn")

def create_application() -> FastAPI:

    application = FastAPI()
    application.include_router(ping.router)
    application.include_router(events.router)

    origins = [
        "http://localhost",
        "http://localhost:8003",
    ]

    application.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return application

app = create_application()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")