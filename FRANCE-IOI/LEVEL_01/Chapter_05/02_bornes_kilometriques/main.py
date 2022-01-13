""" =============== DESCRIPTION ===================
    AUTHOR    : Ayckinn
    COPYRIGHT : ©2022
    LANGUAGE  : PYTHON
    LEVEL     : 01
    CHAPTER   : 05
    EXERCICE  : 02
    TITLE     : BORNES KILOMETRIQUES
=============================================== """
checkpoint_a = int(input())
checkpoint_b = int(input())

if(checkpoint_a < checkpoint_b):
    print(checkpoint_b - checkpoint_a)
else:
    print(checkpoint_a - checkpoint_b)