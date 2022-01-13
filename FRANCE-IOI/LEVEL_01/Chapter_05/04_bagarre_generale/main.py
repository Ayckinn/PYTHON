""" =============== DESCRIPTION ===================
    AUTHOR    : Ayckinn
    COPYRIGHT : ©2022
    LANGUAGE  : PYTHON
    LEVEL     : 01
    CHAPTER   : 05
    EXERCICE  : 04
    TITLE     : BAGARRE GENERALE
=============================================== """
arignon_area = int(input())
evaran_area  = int(input())

if(arignon_area - evaran_area > 10):
    print("La famille Arignon a un champ trop grand")
elif(evaran_area - arignon_area > 10):
    print("La famille Evaran a un champ trop grand")