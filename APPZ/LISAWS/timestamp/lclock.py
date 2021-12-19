# ===========================
# = CLOCK MODULE MANAGEMENT =
# ===========================

import pygame as pg
from ui import constants as cst


class LSClock:

    def __init__(self, screen):
        self.screen = screen
        self.hrmn_lbl = pg.font.SysFont("", 300)

    def centering(self, current_time, color):
        self.show_hour = self.hrmn_lbl.render(current_time, True, color)
        self.center_hour = (cst.WINWIDTH / 2) - (self.show_hour.get_width() / 2)
        self.screen.master.blit(self.show_hour, (self.center_hour, 10))
