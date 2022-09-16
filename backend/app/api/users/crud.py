from app.models.pydantic import UserPayLoadSchema
from app.models.tortoise import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

async def post(payload: UserPayLoadSchema) -> str:
    user = User(
       email=payload.email,
       username=payload.username,
       first_name=payload.first_name,
       last_name=payload.first_name,
       hashed_password=hash_password(payload.password)
    )
    await user.save()
    return user.uuid