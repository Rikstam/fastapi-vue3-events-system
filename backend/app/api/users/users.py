import os
from datetime import timedelta

from jose import JWTError
from fastapi import APIRouter,Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from typing import Union, List

from app.models.pydantic import( 
    UserPayLoadSchema,
    UserResponseSchema,
    Token,
    TokenData,
    EventResponseSchema
)
from app.models.tortoise import User, Event
from app.api.users import auth
router = APIRouter()

ACCESS_TOKEN_EXPIRE_MINUTES = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_user(username: str) -> Union[dict, None]:
    """Get a user by username"""
    user = await User.filter(username=username).first()
    if user:
        return user
    return None

async def authenticate_user(username: str, password: str):
    """Authenticate a user via username and password"""
    user = await get_user(username)
    if not user:
        return False
    if not auth.verify_password(password, user.hashed_password):
        return False
    return user

async def get_current_user(token: str = Depends(oauth2_scheme)):
    """After receiving a token, try to return a corresponding user"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = auth.decode_token(token)
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError as e:
        print(e)
        raise credentials_exception
    user = await get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@router.post("/", response_model=UserResponseSchema, status_code=201)
async def create_user(payload: UserPayLoadSchema) -> UserResponseSchema:
    user = User(
       email=payload.email,
       username=payload.username,
       first_name=payload.first_name,
       last_name=payload.first_name,
       hashed_password=auth.hash_password(payload.password)
    )
    await user.save()
  
    response_object = {
        "uuid": user.uuid,
        "email": payload.email,
        "username": payload.username,
        "first_name": payload.first_name,
        "last_name": payload.last_name,
    }
    return response_object

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """After authentication, obtain the JWT token"""
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    access_token = auth.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {
        "access_token": access_token,
        "token_type": "bearer",
        }

@router.get("/me", response_model=UserResponseSchema)
async def read_users_me(current_user: UserResponseSchema = Depends(get_current_active_user)):
    return current_user

@router.get("/me/events")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    user_events = await Event.filter(user_id=current_user.uuid)
    return user_events

@router.get("/{uuid}")
async def get_user_by_uuid(uuid: str):
    user = await User.filter(uuid=uuid).first()
    user_events = await Event.filter(user_id=user.uuid)
    if user:
        return [{"user": user, "events": user_events}]
    return None