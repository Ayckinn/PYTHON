""" =============== DESCRIPTION ===================
    AUTHOR    : Ayckinn
    COPYRIGHT : ©2022
    LANGUAGE  : PYTHON
    LEVEL     : 01
    CHAPTER   : 05
    EXERCICE  : 06
    TITLE     : TRAVERSEE DU PONT
=============================================== """
dice_a = int(input())
dice_b = int(input())

dice_sum = 0;
tax = 36;
dice_sum = dice_a + dice_b

if(dice_sum >= 10):
    print("Taxe spéciale !")
    print(tax)
else:
    print("Taxe régulière")
    print(dice_sum * 2)