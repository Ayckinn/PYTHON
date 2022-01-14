""" =============== DESCRIPTION ===================
    AUTHOR    : Ayckinn
    COPYRIGHT : ©2022
    LANGUAGE  : PYTHON
    LEVEL     : 01
    CHAPTER   : 06
    EXERCICE  : 01
    TITLE     : VILLES ET VILLAGES
=============================================== """
city = int(input())

MAX_PEOPLE = 10000
total = 0

for loop in range(city):
    people = int(input())

    if(people > MAX_PEOPLE):
        total += 1

print(total)