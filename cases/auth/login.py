from fastapi import HTTPException
import aiohttp
from decouple import config
from app.models import Item


async def getToken(item:Item):
    
    url = config('URL_TOKEN')
    grant_type = config('GRANT_TYPE')
    client_id = config('CLIENT_ID')
    client_secret = config('CLIENT_SECRET')
    scope = config('SCOPE')
    
    body = {
        'username': item.username,
        'password': item.password,
        'grant_type': grant_type,
        'client_id': client_id,
        'client_secret':client_secret,
        'scope': scope
    }
    

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url=url,data=body) as response:
                data = await response.json()

    except Exception as error:
        raise HTTPException(status_code=500, detail=f'Internal error on alpha vantange requests: {error}')
    
    
    return data