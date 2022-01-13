""" =============== DESCRIPTION ===================
    AUTHOR    : Ayckinn
    COPYRIGHT : ©2022
    LANGUAGE  : PYTHON
    LEVEL     : 01
    CHAPTER   : 05
    EXERCICE  : 01
    TITLE     : TRANSPORT DES BAGAGES
=============================================== """
bags   = int(input())
weight = int(input())

result = (bags * weight)
limit_weight = 105

if(result > limit_weight):
    print("Surcharge !")