from fastapi import HTTPException
import aiohttp
from decouple import config

async def getUser(token: str):
    
    url = config('URL_USER_INFO')
    headers = {
        'content-type': 'application/json',
        'Authorization': f'Bearer {token}',
        }
    
    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url=url) as response:
                data = await response.json()
                

    except Exception as error:
        raise HTTPException(status_code=500, detail=f'Erro requests: {error}')
    

    return data