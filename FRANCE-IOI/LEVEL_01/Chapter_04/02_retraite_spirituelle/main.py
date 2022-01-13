""" =============== DESCRIPTION ===================
    AUTHOR    : Ayckinn
    COPYRIGHT : ©2022
    LANGUAGE  : PYTHON
    LEVEL     : 01
    CHAPTER   : 04
    EXERCICE  : 02
    TITLE     : RETRAITE SPIRITUELLE
=============================================== """
SEC_IN_MN = 60
MN_IN_HR = 60
DURATION_SPELL = 16
NB_SPELL = ((SEC_IN_MN * MN_IN_HR) * DURATION_SPELL)

duration_walk = int(input())
print(NB_SPELL * duration_walk)