""" =============== DESCRIPTION ===================
    AUTHOR    : Ayckinn
    COPYRIGHT : ©2022
    LANGUAGE  : PYTHON
    LEVEL     : 01
    CHAPTER   : 06
    EXERCICE  : 07
    TITLE     : PROTECTION DU VILLAGE
=============================================== """
xMax = 0
yMax = 0
xMin = 1000 * 1000
yMin = 1000 * 1000

house = int(input())

for loop in range(house):
    xAxe = int(input())
    yAxe = int(input())

    if(xAxe < xMin):
        xMin = xAxe
    if(xAxe > xMax):
        xMax = xAxe
    if(yAxe < yMin):
        yMin = yAxe
    if(yAxe > yMax):
        yMax = yAxe

xInterval = (xMax - xMin)
yInterval = (yMax - yMin)
perimeter = ((xInterval + yInterval) * 2)

print(perimeter)