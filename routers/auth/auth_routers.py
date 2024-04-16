from fastapi import APIRouter
from app.cases.auth.login import getToken
from app.cases.auth.logout import getLogout


from app.models import Item


router = APIRouter()

@router.post("/login")
async def login(item:Item): 
    token = await getToken(item=item)
    return token



@router.post("/logout")
async def logout(token: str, refresh_token: str):
    response = await getLogout(token=token, refresh_token=refresh_token)
    return response