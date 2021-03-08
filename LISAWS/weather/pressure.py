# ===============================
# = BAROMETER MODULE MANAGEMENT =
# ===============================

import pygame as pg
from ui import constants as cst


class LSPressure:

    def __init__(self, screen, json):
        self.screen = screen
        self.json_request = json

        self.p_font = pg.font.SysFont("", 60)

    def pressure_request(self):
        self.p_data = self.json_request['main']['pressure']
        return self.p_data

    def pressure_display(self, mode, color):
        self.p_hecto = " hPa"
        self.p_display = str(self.pressure_request()) + self.p_hecto

        self.screen.master.blit(mode, (630, 510))
        self.show_p = self.p_font.render(self.p_display, True, color)
        self.center_y = (550 - (self.show_p.get_height() / 2))
        self.screen.master.blit(self.show_p, (730, self.center_y))
