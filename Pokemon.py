from Pokedex import *

class Pokemon(Pokedex):
    def __init__(self, nom):
        Pokedex.__init__(self, nom)
        self.niveau = 1
    
    def suicide(self):
        print(self.pv)
        self.pv -= self.pv
        print(f"Le combat été vraiment trop difficile, le pokemon {self.nom}, a décidé de se suicider ")
