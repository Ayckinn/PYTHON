# ==============================
# = HUMIDITY MODULE MANAGEMENT =
# ==============================

import pygame as pg
from ui import constants as cst


class LSHumidity:

    def __init__(self, screen, json):
        self.screen = screen
        self.json_request = json

        self.h_font = pg.font.SysFont("", 60)

    def humidity_request(self):
        self.h_data = self.json_request['main']['humidity']
        return self.h_data

    def humidity_display(self, mode, color):
        self.h_percent = "%"
        self.h_display = str(self.humidity_request()) + self.h_percent

        self.screen.master.blit(mode, (630, 410))
        self.show_h = self.h_font.render(self.h_display, True, color)
        # -- centering formule [400 + (pic size/2) + 5 - (text size / 2)]
        self.center_y = (450 - (self.show_h.get_height() / 2))
        self.screen.master.blit(self.show_h, (730, self.center_y))
