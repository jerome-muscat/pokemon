import random, time
from Combat import *

def verif_pokemon(pokedex_dict, nom_pokemon):
    if nom_pokemon in pokedex_dict:
        return True
    else:
        return False
    
def saisi_pokemon(pokedex_dict):
    while True:
        nom_pokemon = input("Avec quel Pokémon voulez-vous jouer ?\n")
        verif = verif_pokemon(pokedex_dict, nom_pokemon)
        if verif:
            return nom_pokemon

def barre_de_vie(pokedex_dict, pokemon):
    pokemon_pv_max = pokedex_dict[pokemon.nom]["HP"]
    pokemon_pv = pokemon.pv

    pv_pourcent = pokemon_pv / pokemon_pv_max * 100

    long_barre = 20 
    remplissement_barre = int(long_barre * pv_pourcent / 100)
    
    barre_vide = long_barre - remplissement_barre 
    
    remplissement_barre = "#" * remplissement_barre
    barre_vide = " " * barre_vide

    barre = f"{pokemon.nom}: [{ remplissement_barre}{barre_vide}] {pokemon_pv} / {pokemon_pv_max} pv"

    print(barre)

def boucle_de_jeu(nom_pokemon, pokedex_dict):

    joueur = Combat(nom_pokemon)
    adversaire = Combat(random.choice(list(pokedex_dict.keys())))
    
    print(f"Vous jouez avec {joueur.nom}, qui a {joueur.pv} points de vie.")
    print(f"Votre adversaire est {adversaire.nom}, qui a {adversaire.pv} points de vie.")
    
    while True:
        
        print("---------------------------------------------")
        time.sleep(3)
        if joueur.verifie():
            joueur.renvoie(adversaire)
            break

        if adversaire.verifie():
            adversaire.renvoie(joueur)
            break

        if joueur.verifie() == False and adversaire.verifie() == False:
            joueur.attaque(adversaire)
            barre_de_vie(pokedex_dict, joueur)
            
            adversaire.attaque(joueur)
            barre_de_vie(pokedex_dict, adversaire)