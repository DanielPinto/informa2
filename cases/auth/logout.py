from fastapi import HTTPException,status
import aiohttp
from decouple import config


async def getLogout(token: str, refresh_token:str):
    
    url = config('URL_LOGOUT')
    client_id = config('CLIENT_ID')
    client_secret = config('CLIENT_SECRET')
    grant_type = config('GRANT_TYPE_REFRESH_TOKEN')
    
    body = {
        'refresh_token': refresh_token,
        'client_id': client_id,
        'client_secret':client_secret,
        'grant_type': grant_type
        }
    
    headers = {
        'content-type': 'application/json',
        'Authorization': f'Bearer {token}'
        }
    

    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.post(url=url,data=body) as response:
                data = await response.read()
                if response.status == status.HTTP_200_OK:
                    return 'OK'

    except Exception as error:
        raise HTTPException(status_code=500, detail=f'Internal error on alpha vantange requests: {error}')
    
    
    return data
    
    