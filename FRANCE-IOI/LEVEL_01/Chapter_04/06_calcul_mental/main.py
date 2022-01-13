""" =============== DESCRIPTION ===================
    AUTHOR    : Ayckinn
    COPYRIGHT : ©2022
    LANGUAGE  : PYTHON
    LEVEL     : 01
    CHAPTER   : 04
    EXERCICE  : 06
    TITLE     : JEU DE CALCUL MENTAL
=============================================== """
number = 66
multiply = 2

turn = int(input())

for loop in range(turn):
    print(number)
    number = (number * multiply)
    multiply += 1