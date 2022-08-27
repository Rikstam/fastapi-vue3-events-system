from typing import Union
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from app.api import ping
from app.api import events

def create_application() -> FastAPI:

    application = FastAPI()

    register_tortoise(
        application,
        db_url=os.environ.get("DATABASE_URL"),
        modules={"models": ["app.models.tortoise", "aerich.models"]},
        generate_schemas=False,
        add_exception_handlers=True,
    )

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


