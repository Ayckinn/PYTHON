# ==========================
# = WIND MODULE MANAGEMENT =
# ==========================

import pygame as pg
from ui import constants as cst


class LSWind:

    def __init__(self, screen, json):
        self.screen = screen
        self.json_request = json

        self.w_font = pg.font.SysFont("", 60)

    def wind_request(self):
        self.w_data = self.json_request['wind']['speed']
        return self.w_data

    def wind_display(self, mode, color):
        self.km_text = " Km/h"
        self.speed_km = int(self.wind_request() * 3600 / 1000)
        self.display_speed = str(self.speed_km) + self.km_text

        self.screen.master.blit(mode, (630, 310))
        self.show_w = self.w_font.render(self.display_speed, True, color)
        self.center_y = (350 - (self.show_w.get_height() / 2) + 5)
        self.screen.master.blit(self.show_w, (730, self.center_y))
