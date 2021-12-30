""" =============== DESCRIPTION ===================
    AUTHOR    : Ayckinn
    COPYRIGHT : ©2021
    LANGUAGE  : PYTHON
    LEVEL     : 01
    CHAPTER   : 02
    EXERCICE  : 08
    TITLE     : MONT KAILASH
=============================================== """
from robot import *

for move in range(108):
    for up in range(13):
        haut()
    for right in range(13):
        droite()
    for down in range(13):
        bas()
    for left in range(13):
        gauche()