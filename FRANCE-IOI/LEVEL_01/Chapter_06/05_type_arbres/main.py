""" =============== DESCRIPTION ===================
    AUTHOR    : Ayckinn
    COPYRIGHT : ©2022
    LANGUAGE  : PYTHON
    LEVEL     : 01
    CHAPTER   : 06
    EXERCICE  : 05
    TITLE     : TYPE D'ARBRES
=============================================== """
height = int(input())
folioles = int(input())

if(height <= 8):
    if(folioles >= 8):
        print("Tinuviel")
    else:
        print("Falarion")

elif(height >= 10):
    if(folioles >= 10):
        print("Calaelen")
    else:
        print("Dorthonion")