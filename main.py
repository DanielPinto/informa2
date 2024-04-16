from fastapi import FastAPI
#from pydantic import BaseModel
#from decouple import config
#from app.models import Item
#from app.cases.auth.login import getToken
from app.cases.user.user import getUser
from app.routers.auth.auth_routers import router as routers_auth
from app.routers.user.user_routers import router as routers_user


app = FastAPI()

app.include_router(routers_auth)

app.include_router(routers_user)



"""
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
                print(f'TOKEN: {data}')

    except Exception as error:
        raise HTTPException(status_code=500, detail=f'Internal error on alpha vantange requests: {error}')
    
    if "error" in data:
        token=''
    else:
        token = data["access_token"]
    
    return token
    
    
    
    
    
app.post("/login")
async def getUser(item:Item):
    
    token = await getToken(item=item)
    
    url = config('URL_USER_INFO')
    headers = {
        'content-type': 'application/json',
        'Authorization': f'Bearer {token}',
        }
    
    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url=url) as response:
                resp = await response.read()
                data = resp #json.loads(resp)
                

    except Exception as error:
        raise HTTPException(status_code=500, detail=f'Erro requests: {error}')
    

    return {'user': data,'token': token}
    

@app.get('/')
def hello():
    return 'Hello word'



@app.post("/login")
async def login(item:Item):
    
    token = await getToken(item=item)
    
    return token
    

@app.get("/user")
async def user(token:str):
    
    user = await getUser(token)
    
    return user
    
    
"""

