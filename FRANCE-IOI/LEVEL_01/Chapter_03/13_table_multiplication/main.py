""" =============== DESCRIPTION ===================
    AUTHOR    : Ayckinn
    COPYRIGHT : ©2022
    LANGUAGE  : PYTHON
    LEVEL     : 01
    CHAPTER   : 03
    EXERCICE  : 13
    TITLE     : TABLE DE MULTIPLICATION
=============================================== """
column = 1
line = 1

for loop in range(20):
    for loop in range(20):
        print(column * line, end = " ")
        column += 1

    print()
    line += 1
    column = 1