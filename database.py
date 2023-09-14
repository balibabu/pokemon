import asyncpg
from config import config
from pokemon_api import get_pokemon_from_url
from typing import List, Dict

async def save_pokemons_db(pokemons:List[Dict[str, str]])-> None:
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

async def get_pokemons_from_DB()-> List[Dict[str, str]]:
    conn = await asyncpg.connect(**config["database"])
    try:
        records = await conn.fetch("SELECT * FROM pokemons")
        pokemons=[]
        for record in records:
            pokemons.append({"name":record['name'],"image":record['image'],"type":record['type']})
    finally:
        await conn.close()
    return pokemons

async def update_db()-> None:
    url='https://pokeapi.co/api/v1/pokemon/'
    pokemons=await get_pokemon_from_url(url)
    await save_pokemons_db(pokemons)
