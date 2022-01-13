""" =============== DESCRIPTION ===================
    AUTHOR    : Ayckinn
    COPYRIGHT : ©2022
    LANGUAGE  : PYTHON
    LEVEL     : 01
    CHAPTER   : 04
    EXERCICE  : 09
    TITLE     : SOCLES POUR STATUES
=============================================== """
top = int(input())
ground = int(input())

top_width = 0
interval = (top - ground)

for loop in range(interval + 1):
    top_width = (top_width + (top * top))
    top -= 1

print(top_width)