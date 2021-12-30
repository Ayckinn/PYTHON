""" =============== DESCRIPTION ===================
    AUTHOR    : Ayckinn
    COPYRIGHT : ©2021
    LANGUAGE  : PYTHON
    LEVEL     : 01
    CHAPTER   : 02
    EXERCICE  : 10
    TITLE     : LE GRAND EVENEMENT
=============================================== """
from robot import *

for up in range(9):
    haut()
for right in range(9):
    droite()
for down in range(9):
    bas()

for move in range(4):
    gauche()
    for up in range(8):
        haut()
    gauche()
    for down in range(8):
        bas()

gauche()