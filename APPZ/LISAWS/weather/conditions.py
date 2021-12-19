# =================================
# = CONDITIONS ELEMENT MANAGEMENT =
# =================================

import pygame as pg
import requests
from ui import constants as cst


class LSCondition:

    def __init__(self, screen, json):
        self.screen = screen
        self.json_request = json

        self.c_font = pg.font.SysFont("", 30)

    def condition_request(self):
        self.c_data = self.json_request['weather'][0]['description']
        return self.c_data.upper()

    def condition_display(self, color):
        self.show_c = self.c_font.render(self.condition_request(), True, color)
        self.center_x = (256 + (256 / 2)) - (self.show_c.get_width() / 2)
        self.screen.master.blit(self.show_c, (self.center_x, 540))

    def condition_light(self):
        self.condition_display(cst.WHITE)
        self.condition_pics(cst.SUN, cst.FEW_CLOUDY_SUN, cst.CLOUDY_SUN,
                            cst.CLOUDY_DAY, cst.LIGHT_RAIN_DAY, cst.STORM_DAY)

    def condition_dark(self):
        self.condition_display(cst.GREY)
        self.condition_pics(cst.MOON, cst.FEW_CLOUDY_MOON, cst.CLOUDY_MOON,
                            cst.CLOUDY_NIGHT, cst.LIGHT_RAIN_NIGHT, cst.STORM_NIGHT)

    def condition_pics(self, mode1, mode2, mode3, mode4, mode5, mode6):
        if self.condition_request() == "CIEL DÉGAGÉ":
            self.screen.master.blit(mode1, (5, 320))
        if self.condition_request() == "PEU NUAGEUX":
            self.screen.master.blit(mode2, (5, 320))
        if self.condition_request() == "PARTIELLEMENT NUAGEUX":
            self.screen.master.blit(mode2, (5, 320))
        if self.condition_request() == "COUVERT":
            self.screen.master.blit(mode3, (5, 320))
        if self.condition_request() == "NUAGEUX":
            self.screen.master.blit(mode4, (5, 320))
        if self.condition_request() == "LÉGÈRE PLUIE":
            self.screen.master.blit(mode5, (5, 320))
        if self.condition_request() == "ORAGE":
            self.screen.master.blit(mode6, (5, 320))