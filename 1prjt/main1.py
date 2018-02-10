# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 19:34:26 2018

@author: wiame
"""
from func import *

# programme principal -----------------------------------------------
rayon = float(input("Rayon : "))

print("\nVolume de la sphere de rayon {:.1f} : {:.3f}".format(rayon, volumeSphere(rayon)))
