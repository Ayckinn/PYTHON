""" =============== DESCRIPTION ===================
    AUTHOR    : Ayckinn
    COPYRIGHT : ©2022
    LANGUAGE  : PYTHON
    LEVEL     : 01
    CHAPTER   : 06
    EXERCICE  : 04
    TITLE     : CALCUL DES DENIVELEES
=============================================== """
up = 0
down = 0
up_n_down = int(input())

for loop in range(up_n_down):
    variations = int(input())

    if(variations < 0):
        down += variations
    else:
        up += variations

if(down < 0):
    down = -down

print(up)
print(down)