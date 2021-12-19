# ==========================
# = CITY MODULE MANAGEMENT =
# ==========================

import pygame as pg


class LSCity:

    def __init__(self, screen, json):
        self.screen = screen
        self.json_request = json

        self.city_font = pg.font.SysFont("", 30)

    def city_request(self):
        self.y_data = self.json_request['name']
        return self.y_data.upper()

    def city_display(self, color):
        self.city_name = self.city_request()

        self.show_city = self.city_font.render(self.city_name, True, color)
        self.center_x = (256 + (256 / 2) - (self.show_city.get_width() / 2))
        self.center_y = 450 - (self.show_city.get_height() / 2)
        self.screen.master.blit(self.show_city, (self.center_x, 330))