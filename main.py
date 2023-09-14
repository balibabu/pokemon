from fastapi import FastAPI
from database import get_pokemons_from_DB, update_db
from pokemons import filter_pokemons
import uvicorn
import asyncio

app = FastAPI()
pokemons=[]

@app.get("/")
def greet()-> dict:
    return {"message":"Welcome"}

@app.get("/api/v1/pokemons")
async def get_pokemons()-> list[dict]:
    pokemons=await get_pokemons_from_DB() 
    return pokemons

@app.get("/api/v1/pokemons/name={name}/type={_type}")
async def get_pokemons(name:str,_type:str)-> list[dict]:
    global pokemons
    if not pokemons:
        pokemons=await get_pokemons_from_DB()
    if _type=='none':
        _type=None
    if name=='none':
        name=None
    filtered_pok=filter_pokemons(pokemons,name=name,type=_type)
    return filtered_pok

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(update_db())
    uvicorn.run(app, host="localhost", port=8000)
