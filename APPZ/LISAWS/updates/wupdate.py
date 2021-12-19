# ============================
# = UPDATE MODULE MANAGEMENT =
# ============================

import pygame as pg
from time import sleep
from ui import mode
from updates import json_request


class WeatherUpdate:

    def __init__(self, screen):
        self.screen = screen
        self.json_rq = json_request.JSONRequest()
        self.display_mode = mode.DisplayMode(self.screen, self.json_rq)

    def full_update(self, counter):
        self.display_mode.time_slot()
        counter.loop_increase()

        if counter.get_loop_value() == 1200:  # -- 1200 = 10mn
            self.display_mode.update_temperature(self.json_rq)
            self.display_mode.update_condition(self.json_rq)
            self.display_mode.update_wind(self.json_rq)
            self.display_mode.update_humidity(self.json_rq)
            self.display_mode.update_pressure(self.json_rq)
            counter.loop_value = 0

        sleep(0.5)
