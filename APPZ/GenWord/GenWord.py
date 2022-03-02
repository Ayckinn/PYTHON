#! usr/bin/env python3
# -*- coding: UTF-8 -*-

# ==================================================
# =                GENWORD - V1.0                  =
# = Generate all possibles combinations for a word =
# =               ©2020 - Ayckinn                  =
# ==================================================

from os import system
from itertools import permutations

system('clear')

# ============================================================================
user_word = input("\nPlease choose a word : ")
len_word = len(user_word)

# ----------------------------------------------------------------------------
def random_word():
    word_list = [''.join(x) for x in permutations(user_word, len_word)]

    counter = 0
    for word in word_list:
        counter += 1

    print()
    print('\n'.join(word_list))
    print("\nThere are \033[1;31m{}\033[1;m letters in your word and"
          " \033[1;32m{}\033[1;m combinations\n".format(len_word, counter))

# ============================================================================
random_word()
