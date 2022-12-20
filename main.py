"""
Programme fait par Alexander Precup
Groupe: 402
Description: Objets orientées
Exercise 2 - Écrire une classe Rectangle
"""


class Rectangle:
    def __init__(self, largeur, longueur):
        self.largeur = largeur
        self.longueur = longueur
        self.aire = 0

    def calculer_aire(self):
        return self.largeur * self.longueur

    def afficher_infos(self):
        print(f"Longueur rectangle : {self.longueur}")
        print(f"Largeur rectangle : {self.largeur}")


r = Rectangle(12, 20)
r_aire = r.calculer_aire()
r.afficher_infos()
print(f"Aire rectangle : {r_aire}")
