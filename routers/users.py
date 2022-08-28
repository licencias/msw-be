from fastapi import APIRouter
from repository import users
from config.config import session

router = APIRouter(tags=["brokers"], prefix="/users")

@router.get("/all")
async def users_all():
    r = users.get_users(session)
    return {"users": r}
