from fastapi import APIRouter
from app.cases.user.user import getUser


router = APIRouter()

@router.get("/user")
async def user(token:str):
    
    user = await getUser(token)
    
    return user