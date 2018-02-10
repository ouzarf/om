"""
1. Saisissez un flottant. S’il est positif ou nul, affichez sa racine, sinon affichez un message
d’erreur.
"""
# -*- coding: UTF-8 -*-
"""Les instructions de choix."""
# fichier : cours2_05.py
# auteur : Bob Cordeau
# import
from math import sqrt
# programme principal -----------------------------------------------
x = float(input("x ? "))
if x >= 0:
	y = sqrt(x)
	print("La racine de {:.2f} est {:.3f}".format(x, y))
else:
	print("On ne peut pas prendre la racine d'un reel negatf !")
print("\nAu revoir")