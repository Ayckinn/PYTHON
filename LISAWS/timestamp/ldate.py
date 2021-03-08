# ==========================
# = DATE MODULE MANAGEMENT =
# ==========================

import pygame as pg
from datetime import datetime
from ui import constants as cst
# -- Import and command for display date in French
import locale
locale.setlocale(locale.LC_TIME, '')


class LSDate:

    def __init__(self, screen):
        self.screen = screen
        self.date_lbl = pg.font.SysFont("", 60)

    def centering(self, colour):
        self.current_date = datetime.now()
        self.display_date = self.current_date.strftime("%A %d %B %Y").upper()

        self.show_date = self.date_lbl.render(self.display_date, True, colour)
        self.center_date = (cst.WINWIDTH / 2) - (self.show_date.get_width() / 2)
        self.screen.master.blit(self.show_date, (self.center_date, 235))
