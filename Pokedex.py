import json
class Pokedex:
    def __init__(self, nom):
        with open("pokedex.json", "r", encoding='utf-8') as f:
            self.pokedex_dict = json.load(f)

        self.nom = nom
        self.pv = self.pokedex_dict[nom]["HP"]
        self.point_attaque = self.pokedex_dict[nom]["Attack"]
        self.point_defense = self.pokedex_dict[nom]["Defense"]
        self.type1 = self.pokedex_dict[nom]["Type 1"]
        self.type2 = self.pokedex_dict[nom]["Type 2"]