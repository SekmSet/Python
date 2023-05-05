# Sujet : Pokédex avec la PokeAPI https://pokeapi.co/
# Ecrire un programme qui permet les actions suivantes :
# Lister les Pokémon de couleur jaune
# "list all yellow pokemon" doit renvoyer au minimum :
# → Sabelette, Miaouss, Psykokwak, Coconfort, Dardargnan, Pikachu, …
# Lister tous les Pokémon jusqu’à un id donné
# "list all pokemon until 151" doit renvoyer au minimum :
# → … , Mewtwo, Mew
# Bonus : avec une interface graphique

# Imports
import requests
import json

# Variables
url_poke_api = 'https://pokeapi.co/api/v2/'

# Functions
def get_pokemon_by_color():
    print("--- POKE API GET POKEMON BY COLOR ---")

    url = url_poke_api + "pokemon-color/yellow"
    result = requests.get(url)
    data = result.json()
    dataAsString = json.loads(result.text)
    print(dataAsString)

def get_pokemon_limit_result():
    print("--- POKE API GET POKEMON WITH LIMIT ---")

    url = url_poke_api + "pokemon?limit=151"
    result = requests.get(url)
    data = result.json()
    dataAsString = json.loads(result.text)
    print(dataAsString)


get_pokemon_by_color()
get_pokemon_limit_result()
