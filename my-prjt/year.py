# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 00:02:05 2018

@author: wiame
"""

from m1 import julian_leap

year  = input("year=? ")
year = int(year)

if julian_leap(year):
    print( year, "is leap")
else:
    print (year, "is not leap")   