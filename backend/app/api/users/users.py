from fastapi import APIRouter, HTTPException, Path

from app.api.users import crud

from app.models.pydantic import( 
    UserPayLoadSchema,
    UserResponseSchema
)

from app.models.tortoise import UserSchema

router = APIRouter()

@router.post("/", response_model=UserResponseSchema, status_code=201)
async def create_user(payload: UserPayLoadSchema) -> UserResponseSchema:
    user_uuid = await crud.post(payload)

    response_object = {
        "uuid": user_uuid,
        "email": payload.email,
        "username": payload.username,
        "first_name": payload.first_name,
        "last_name": payload.last_name,
       
    }
    return response_object