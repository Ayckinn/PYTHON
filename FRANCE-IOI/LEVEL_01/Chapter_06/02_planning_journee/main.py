""" =============== DESCRIPTION ===================
    AUTHOR    : Ayckinn
    COPYRIGHT : ©2022
    LANGUAGE  : PYTHON
    LEVEL     : 01
    CHAPTER   : 06
    EXERCICE  : 02
    TITLE     : PLANNING DE LA JOURNEE
=============================================== """
current_pos = int(input())
cities = int(input())

total = 0

for loop in range(cities):
    cities_pos = int(input())

    if(cities_pos >= (current_pos - 50) and cities_pos <= (current_pos + 50)):
        total += 1

print(total)