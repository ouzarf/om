""" 
exe2. Saisir un nom et un âge en utilisant l’instruction input(). Les afficher.
Refaire la saisie du nom, mais avec l’instruction raw_input(). 
"""
# -*- coding: UTF-8 -*-
"""Les instructions input."""
# fichier : cours1_10.py
# auteur : Bob Cordeau
# programme principal -----------------------------------------------
## instruction input :
nom = input("ton nom ? ")
age = input("age ? ")
age = float(age)
print()
## affichage formate :
print("{}".format("-"*60))
print("\t Nom :", nom, "\t Age :", age)
## bonnes pratiques :
nom = input("ton nom ? ") # pour une chaine
age = float(input("age ? ")) # sinon : transtyper explicitement
print()
## affichage formate :

print("{}\n\t Nom : {}\t Age : {}".format("-"*60, nom, age))