""" =============== DESCRIPTION ===================
    AUTHOR    : Ayckinn
    COPYRIGHT : ©2021
    LANGUAGE  : PYTHON
    LEVEL     : 01
    CHAPTER   : 02
    EXERCICE  : 09
    TITLE     : VENDANGES
=============================================== """
from robot import *

for move in range(20):
    ramasser()
    for x in range(15):
        droite()

    deposer()
    for x in range(15):
        gauche()