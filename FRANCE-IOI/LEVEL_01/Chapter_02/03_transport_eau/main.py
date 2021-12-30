""" =============== DESCRIPTION ===================
    AUTHOR    : Ayckinn
    COPYRIGHT : ©2021
    LANGUAGE  : PYTHON
    LEVEL     : 01
    CHAPTER   : 02
    EXERCICE  : 03
    TITLE     : TRANSPORT D'EAU
=============================================== """
from robot import *

for move in range(2):
    gauche()

print("Bonjour, laissez-moi vous aider")
ramasser()

for move in range(32):
    droite()
deposer()