""" =============== DESCRIPTION ===================
    AUTHOR    : Ayckinn
    COPYRIGHT : ©2022
    LANGUAGE  : PYTHON
    LEVEL     : 01
    CHAPTER   : 06
    EXERCICE  : 08
    TITLE     : LE JUSTE PRIX
=============================================== """
pancakes = 1000*1000
pos = 0
pos_max = 0

dealers = int(input())

for loop in range(dealers):
    pos += 1
    price = int(input())

    if(price <= pancakes):
        pancakes = price
    if(price == pancakes):
        pos_max = pos

print(pos_max)