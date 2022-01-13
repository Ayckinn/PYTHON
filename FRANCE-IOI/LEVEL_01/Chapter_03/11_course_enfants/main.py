""" =============== DESCRIPTION ===================
    AUTHOR    : Ayckinn
    COPYRIGHT : ©2022
    LANGUAGE  : PYTHON
    LEVEL     : 01
    CHAPTER   : 03
    EXERCICE  : 11
    TITLE     : COURSE AVEC LES ENFANTS
=============================================== """
from robot import *

move = 0

for loop in range(10):
    move += 1

    for loop in range(move):
        droite()
    ramasser()

    for loop in range(move):
        gauche();
    deposer()