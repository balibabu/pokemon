import requests
from typing import List, Dict

async def get_pokemon_from_url(url:str) -> List[Dict[str, str]]:
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
