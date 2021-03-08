#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

# ==========================================================================
# =                  MACGYVER LABYRINTH GAME USING PYGAME                  =
# =                       OPENCLASSROOMS - PROJECT 03                      =
# =                                                                        =
# =  Help MacGyver to get out of the labyrinth.                            =
# =  He must get all items before he puts the guard to sleep and get out.  =
# =  Use direction arrows for MacGyver's moves                             =
# ==========================================================================

# -- Import Python modules
import pygame as pg
from os import environ
# -- Import personnal modules
from game import maze, itemcounter, constants as cst
from player import player

# -- Force center screen and init Pygame
environ['SDL_VIDEO_CENTERED'] = '1'
pg.init()


# ============================================================================
def main():
    screen = maze.GameBoard()
    board = screen.lab_struct()
    screen.draw_objects()
    hero = player.McGyver(screen)
    counter = itemcounter.ItemCounter()

    pg.display.flip()

    # ------------------------------------------------------------------------
    while True:
        ev = pg.event.wait()
        key_pressed = pg.key.get_pressed()
        # -- Close the window game by the CROSS button or ESCAPE key
        if ev.type == pg.QUIT or key_pressed[pg.K_ESCAPE]:
            break
        elif ev.type == pg.KEYDOWN:
            hero.del_mac()
            hero.update_mac(ev.key, board)
            hero.show_mac()
            hero.pickup(board, counter)
            screen.win_loose(hero, counter)

        pg.display.flip()
