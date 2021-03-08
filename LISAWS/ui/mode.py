# ==================================
# = DISPLAY MODE MODULE MANAGEMENT =
# ==================================

import pygame as pg
from time import strftime
from ui import constants as cst
from timestamp import lclock, ldate
from weather import wind, city, temperature
from weather import conditions, humidity, pressure
from updates import json_request


class DisplayMode:

    def __init__(self, screen, rq):
        self.screen = screen
        self.json_rq = rq

        self.lisaclock = lclock.LSClock(self.screen)
        self.lisadate = ldate.LSDate(self.screen)
        self.lisacity = city.LSCity(self.screen, self.json_rq.update_json_file())
        self.lisatemp = temperature.LSTemp(self.screen , self.json_rq.update_json_file())
        self.lisacondition = conditions.LSCondition(self.screen, self.json_rq.update_json_file())
        self.lisawind = wind.LSWind(self.screen, self.json_rq.update_json_file())
        self.lisahumidity = humidity.LSHumidity(self.screen, self.json_rq.update_json_file())
        self.lisapressure = pressure.LSPressure(self.screen, self.json_rq.update_json_file())
      
    def time_slot(self):
        self.hour = strftime("%H")
        self.mn = strftime("%M")
        self.current_time = strftime("%H:%M")
        self.screen.master.blit(cst.BACKGROUND, (0, 0))

        if "09" <= self.hour <= "21":
            self.light()
        else:
            self.dark()

        pg.display.flip()

    def light(self):
        self.lisaclock.centering(self.current_time, cst.GREEN)
        self.lisadate.centering(cst.CYAN)
        self.lisacity.city_display(cst.WHITE)
        self.lisatemp.temperature_display(cst.WHITE)
        self.lisacondition.condition_light()
        self.lisawind.wind_display(cst.WIND_DAY, cst.WHITE)
        self.lisahumidity.humidity_display(cst.HUMIDITY_DAY, cst.WHITE)
        self.lisapressure.pressure_display(cst.PRESSURE_DAY, cst.WHITE)

    def dark(self):
        self.lisaclock.centering(self.current_time, cst.GREY)
        self.lisadate.centering(cst.GREY)
        self.lisacity.city_display(cst.GREY)
        self.lisatemp.temperature_display(cst.GREY)
        self.lisacondition.condition_dark()
        self.lisawind.wind_display(cst.WIND_NIGHT, cst.GREY)
        self.lisahumidity.humidity_display(cst.HUMIDITY_NIGHT, cst.GREY)
        self.lisapressure.pressure_display(cst.PRESSURE_NIGHT, cst.GREY)

    def update_temperature(self, rq):
        self.lisatemp = temperature.LSTemp(self.screen, rq.update_json_file())

    def update_condition(self, rq):
        self.lisacondition = conditions.LSCondition(self.screen, rq.update_json_file())

    def update_wind(self, rq):
        self.lisawind = wind.LSWind(self.screen, rq.update_json_file())

    def update_humidity(self, rq):
        self.lisahumidity = humidity.LSHumidity(self.screen, rq.update_json_file())

    def update_pressure(self, rq):
        self.lisapressure = pressure.LSPressure(self.screen, rq.update_json_file())
