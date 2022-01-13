""" =============== DESCRIPTION ===================
    AUTHOR    : Ayckinn
    COPYRIGHT : ©2022
    LANGUAGE  : PYTHON
    LEVEL     : 01
    CHAPTER   : 05
    EXERCICE  : 07
    TITLE     : CONCOURS DE TIR A LA CORDE
=============================================== """
members = int(input())

total_a = 0
total_b = 0

for loop in range(members):
    weight_a = int(input())
    weight_b = int(input())

    total_a = (total_a + weight_a)
    total_b = (total_b + weight_b)

if(total_a > total_b):
    print("L'équipe 1 a un avantage")
else:
    print("L'équipe 2 a un avantage")

print("Poids total pour l'équipe 1 : " + str(total_a))
print("Poids total pour l'équipe 2 : " + str(total_b))