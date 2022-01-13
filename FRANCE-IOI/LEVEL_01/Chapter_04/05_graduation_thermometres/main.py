""" =============== DESCRIPTION ===================
    AUTHOR    : Ayckinn
    COPYRIGHT : ©2022
    LANGUAGE  : PYTHON
    LEVEL     : 01
    CHAPTER   : 04
    EXERCICE  : 05
    TITLE     : GRADUATION DE THERMOMETRES
=============================================== """
temp_min = int(input())
temp_max = int(input())

interval = (temp_max - temp_min)

for loop in range(interval):
    print(temp_min)
    temp_min += 1

print(temp_max)