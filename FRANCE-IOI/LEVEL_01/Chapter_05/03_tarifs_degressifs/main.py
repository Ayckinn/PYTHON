""" =============== DESCRIPTION ===================
    AUTHOR    : Ayckinn
    COPYRIGHT : ©2022
    LANGUAGE  : PYTHON
    LEVEL     : 01
    CHAPTER   : 05
    EXERCICE  : 03
    TITLE     : TARIFS DEGRESSIFS
=============================================== """
room_price = 10;
tax = 5;
price_max = 53;

arrival_time = int(input())
price = (room_price + tax * arrival_time)

if(price > price_max):
    print(price_max)
else:
    print(price)