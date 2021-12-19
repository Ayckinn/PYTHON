# =================================================
# = File containing all the constants of the Game =
# =================================================

import pygame as pg

# -- GAME WINDOW SETTINGS
NB_SPRITES = 15
SPRITE_SIZE = 50
WINSIZE = NB_SPRITES * SPRITE_SIZE
GAME_TITLE = "MacGyver Labyrinth - v2.0"

# -- GAME PICS
BKG_PIC = pg.image.load('img/background.png')
FULLWALL_PIC = pg.image.load('img/fullwall.png')
WALL_PIC = pg.image.load('img/wall.png')
MACGYVER_PIC = pg.image.load('img/macgyver.png')
GUARDIAN_PIC = pg.image.load('img/guardian.png')
NEEDLE_PIC = pg.image.load('img/needle.png')
PIPE_PIC = pg.image.load('img/pipe.png')
ETHER_PIC = pg.image.load('img/ether.png')
SYRINGE_PIC = pg.image.load('img/syringe.png')
YOUWIN_PIC = pg.image.load('img/youwin.png')
GAMEOVER_PIC = pg.image.load('img/gameover.png')
