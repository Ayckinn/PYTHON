""" =============== DESCRIPTION ===================
    AUTHOR    : Ayckinn
    COPYRIGHT : ©2022
    LANGUAGE  : PYTHON
    LEVEL     : 01
    CHAPTER   : 04
    EXERCICE  : 07
    TITLE     : LA GRANDE BRADERIE
=============================================== """
position = int(input())
location = int(input())
sellers  = int(input())

for loop in range(sellers + 1):
    print(position)
    position = (position + location)