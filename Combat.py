import json, random
from Pokemon import *

class Combat(Pokemon):
    def __init__(self, nom):
        Pokemon.__init__(self, nom)
        self.maj_attaque = 1
        self.maj_def = 1
    
    def attaque(self, pokemon):
        if self.verifie() == False:
            with open("type.json", "r", encoding='utf-8') as f:
                type_pokemon = json.load(f)
            
            coup = int(random.choice((0,1)))
            degat_attaque = None

            match pokemon.type1:
                case type1_efficace if type1_efficace in type_pokemon[self.type1]["Efficace"]:
                    degat_attaque =  type_pokemon[self.type1]["Efficace"][pokemon.type1]
                case _:
                    degat_attaque = 1
                    
            if self.type2 != "" and self.type2 in type_pokemon and "Efficace" in type_pokemon[self.type2]:
                match pokemon.type1:
                    case type2_efficace if type2_efficace in type_pokemon[self.type2]["Efficace"]:
                        match type_pokemon[self.type2]["Efficace"][pokemon.type1]:
                            case degat_attaque:
                                degat_attaque *= type_pokemon[self.type2]["Efficace"][pokemon.type1]
                    
            match pokemon.type1:
                case type1_resistant if type1_resistant in type_pokemon[self.type1]["Résistance"]:
                    degat_defense = type_pokemon[self.type1]["Résistance"][pokemon.type1]
                
                case _:
                    degat_defense = 1
                    
            degat = int(((((self.niveau * 0.4 + 2) * self.point_attaque / pokemon.point_defense) / 50) + 2) * degat_attaque  * degat_defense  * coup)
            pokemon.pv -= degat

            if coup == 1:
                print(f"L'attaque vers {pokemon.nom} a réussi, elle lui a infligé {degat} dégats, il lui reste {pokemon.pv} pv.")
            
            else:
                print(f"L'attaque vers {pokemon.nom} a echoué")

        else:
            print(f"{self.nom} a perdu")
    
    def verifie(self):
        if self.pv <= 0:
            return True
        else:
            return False
    
    def renvoie(self, pokemon):
        if self.pv < pokemon.pv and self.pv <= 0:
            print(f"Le vainceur est {pokemon.nom}, le perdant est {self.nom}")
            return pokemon.nom
        
        elif self.pv > pokemon.pv and pokemon.pv <= 0:
            print(f"Le vainceur est {self.nom}, le perdant est {pokemon.nom}")
            return self.nom