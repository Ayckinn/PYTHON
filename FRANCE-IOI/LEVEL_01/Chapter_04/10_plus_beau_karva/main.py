""" =============== DESCRIPTION ===================
    AUTHOR    : Ayckinn
    COPYRIGHT : ©2022
    LANGUAGE  : PYTHON
    LEVEL     : 01
    CHAPTER   : 04
    EXERCICE  : 10
    TITLE     : LE PLUS BEAU KARVA
=============================================== """
nb_karva = int(input())

for loop in range(nb_karva):
    weight = int(input())
    age = int(input())
    horns = int(input())
    withers = int(input())

    print(horns * withers + weight)