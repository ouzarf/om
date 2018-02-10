# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 10:30:04 2018

@author: wiame
"""

# fonction
def somme(*args):
    resultat = 0
    for nombre in args:
        resultat += nombre
    return resultat