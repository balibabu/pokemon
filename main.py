import asyncpg
from config import config
import requests
from fastapi import FastAPI
app = FastAPI()
pokemons=[]

async def save_pokemons_db(pokemons):
    conn = await asyncpg.connect(**config["database"])
    try:
        await conn.execute(
            """
            CREATE TABLE IF NOT EXISTS pokemons (
                id serial PRIMARY KEY,
                name VARCHAR(50) UNIQUE,
                image TEXT,
                type VARCHAR(50)
            )
            """
        )
        for pokemon in pokemons:
            try:
                await conn.execute(
                    """
                    INSERT INTO pokemons (name, image, type)
                    VALUES ($1, $2, $3)
                    """,
                    f"{pokemon['name']}",
                    f"{pokemon['image']}",
                    f"{pokemon['type']}"
                )
            except:
                pass
    except Exception as error:
        print(error)
    finally:
        await conn.close()

async def get_pokemon_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        pokemons = [(pokemon['name'],pokemon['url']) for pokemon in data['results']]
        names=[]
        types=[]
        imgs=[]
        for name,url in pokemons:
            names.append(name)
            nested_res=requests.get(url)
            nested_res.raise_for_status()
            nested_data=nested_res.json()
            imgs.append(nested_data['sprites']['back_default'])
            types.append(nested_data['types'][0]['type']['name'])
        pokemons=[{"name":_name,"type":_type,"image":img} for _name,_type,img in zip(names,types,imgs)]
        return pokemons
    except requests.exceptions.RequestException as e:
        return {"error": "Failed to fetch Pokémon data from PokeAPI"}

async def get_pokemons_from_DB():
    conn = await asyncpg.connect(**config["database"])
    try:
        records = await conn.fetch("SELECT * FROM pokemons")
        pokemons=[]
        for record in records:
            pokemons.append({"name":record['name'],"image":record['image'],"type":record['type']})
    finally:
        await conn.close()
    return pokemons

async def update_db():
    url='https://pokeapi.co/api/v1/pokemon/'
    pokemons=await get_pokemon_from_url(url)
    await save_pokemons_db(pokemons)

def filter_pokemons(pokemons, type=None, name=None):
  filtered_pokemons = []
  for pokemon in pokemons:
    if name is not None and pokemon["name"].lower() != name.lower():
      continue
    if type is not None and pokemon["type"] != type:
      continue
    filtered_pokemons.append(pokemon)
  return filtered_pokemons

@app.get("/api/v1/pokemons")
async def get_pokemons():
    pokemons=await get_pokemons_from_DB() 
    return pokemons

@app.get("/api/v1/pokemons/name={name}/type={_type}")
async def get_pokemons(name,_type):
    global pokemons
    if not pokemons:
        pokemons=await get_pokemons_from_DB()
    if _type=='none':
        _type=None
    if name=='none':
        name=None
    filtered_pok=filter_pokemons(pokemons,name=name,type=_type)
    return filtered_pok

@app.get("/")
def greet():
    return {"message":"Welcome"}

if __name__ == "__main__":
    import uvicorn, asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(update_db())
    uvicorn.run(app, host="localhost", port=8000)
