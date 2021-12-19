# =================================
# = TEMPERATURE MODULE MANAGEMENT =
# =================================

import pygame as pg
from ui import constants as cst


class LSTemp:

    def __init__(self, screen, json):
        self.screen = screen
        self.json_request = json

        self.t_font = pg.font.SysFont("", 150)

    def temperature_request(self):
        self.t_data = self.json_request['main']['temp']
        return self.t_data

    def temperature_display(self, color):
        self.t_degree = "°"
        self.t_current = int(self.temperature_request() - 273.15)
        self.display_temp = str(self.t_current) + self.t_degree

        self.show_t = self.t_font.render(self.display_temp, True, color)
        self.center_x = (256 + (256 / 2) - (self.show_t.get_width() / 2) + 20)
        self.center_y = 450 - (self.show_t.get_height() / 2)
        self.screen.master.blit(self.show_t, (self.center_x, self.center_y))
