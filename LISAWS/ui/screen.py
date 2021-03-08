# ===========================
# = BOARD MODULE MANAGEMENT =
# ===========================

import pygame as pg
from ui import constants as cst


class ClockBoard:

    def __init__(self):
        # -- Fullscreen mode
        #  self.master = pg.display.set_mode((cst.WINWIDTH, cst.WINHEIGHT), pg.FULLSCREEN)
        # -- Not resizable screen mode
        self.master = pg.display.set_mode((cst.WINWIDTH, cst.WINHEIGHT))
        # -- Resizable screen mode
        # self.master = pg.display.set_mode((cst.WINWIDTH, cst.WINHEIGHT), pg.RESIZABLE)
        self.tilte = pg.display.set_caption(cst.CLOCK_TITLE)
        self.icon = pg.display.set_icon(cst.ICON)
        pg.mouse.set_visible(False)
