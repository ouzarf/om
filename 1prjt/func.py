# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 19:32:59 2018

@author: wiame
"""

# import
from math import pi
# fonctions
def cube(x):
    """Calcule le cube de l'argument."""
    return x**3
def volumeSphere(r):
    """Calcule le volume d'une sphere de rayon <r>."""
    return 4 * pi * cube(r) / 3


