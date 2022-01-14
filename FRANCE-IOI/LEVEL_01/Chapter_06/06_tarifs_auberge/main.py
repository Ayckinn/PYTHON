""" =============== DESCRIPTION ===================
    AUTHOR    : Ayckinn
    COPYRIGHT : ©2022
    LANGUAGE  : PYTHON
    LEVEL     : 01
    CHAPTER   : 06
    EXERCICE  : 06
    TITLE     : TARIFS DE L'AUBERGE
=============================================== """
age = int(input())
bag_weight = int(input())

if(age < 10):
    print(5)
else:
    if(age == 60):
        print(0)
    else:
        if(bag_weight >= 20):
            print(40)
        else:
            print(30)