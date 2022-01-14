""" =============== DESCRIPTION ===================
    AUTHOR    : Ayckinn
    COPYRIGHT : ©2022
    LANGUAGE  : PYTHON
    LEVEL     : 01
    CHAPTER   : 06
    EXERCICE  : 03
    TITLE     : ETAPE LA PLUS LONGUE
=============================================== """
max_distance = 0
days = int(input())

for loop in range(days):
    distance = int(input())

    if(distance > max_distance):
        max_distance = distance

print(max_distance)