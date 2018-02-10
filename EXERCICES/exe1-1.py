""" 
exe1
. Affectez les variables temps et distance par les valeurs 6.892 et 19.7.
Calculez et affichez la valeur de la vitesse.
Améliorez l’affichage en imposant un chiffre après le point décimal.
"""
# -*- coding: UTF-8 -*-
"""La fonction print()."""
# fichier : cours1_05.py
# auteur : Bob Cordeau
# programme principal -----------------------------------------------
## affichage simple :
temps = 6.892
distance = 19.7
vitesse = distance/temps
print()
print("vitesse =", vitesse)
print()
## affichage formate :
print("{}".format("-"*80))
print("\n vitesse = {:.2f} m/s".format(vitesse)) # arrondi a 2 chiffres
print()
print("{}".format("*-"*40))