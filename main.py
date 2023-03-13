import json
from fonctions import saisi_pokemon, boucle_de_jeu

with open("pokedex.json", "r", encoding='utf-8') as f:
        pokedex_dict = json.load(f)

nom_pokemon = saisi_pokemon(pokedex_dict)

boucle_de_jeu(nom_pokemon, pokedex_dict)