from typing import List, Dict
def filter_pokemons(pokemons:List[Dict[str, str]], type:str = None, name:str = None)->List[Dict[str, str]]:
  filtered_pokemons = []
  for pokemon in pokemons:
    if name is not None and pokemon["name"].lower() != name.lower():
      continue
    if type is not None and pokemon["type"] != type:
      continue
    filtered_pokemons.append(pokemon)
  return filtered_pokemons
