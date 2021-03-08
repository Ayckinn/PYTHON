# =================================
# = FILE CONTAINING ALL CONSTANTS =
# =================================

import pygame as pg

# -- Main window resolution - 7inch screen
WINWIDTH = 1024
WINHEIGHT = 600

# -- Elements
CLOCK_TITLE = "LISA Weather Station - v1.1 // © Ayckinn 2020"
BACKGROUND = pg.image.load('img/bg.png')
ICON = pg.image.load('img/icon.png')

# -- Weather pics
SUN = pg.image.load('img/sun.png')
MOON = pg.image.load('img/moon.png')
FEW_CLOUDY_SUN = pg.image.load('img/few_cloudy_sun.png')
FEW_CLOUDY_MOON = pg.image.load('img/few_cloudy_moon.png')
CLOUDY_DAY = pg.image.load('img/cloudy_day.png')
CLOUDY_NIGHT = pg.image.load('img/cloudy_night.png')
CLOUDY_SUN = pg.image.load('img/cloudy_sun.png')
CLOUDY_MOON = pg.image.load('img/cloudy_moon.png')
LIGHT_RAIN_DAY = pg.image.load('img/light_rain_day.png')
LIGHT_RAIN_NIGHT = pg.image.load('img/light_rain_night.png')
STORM_DAY = pg.image.load('img/storm_day.png')
STORM_NIGHT = pg.image.load('img/storm_night.png')

# -- Info pics
WIND_DAY = pg.image.load('img/wind_day.png')
HUMIDITY_DAY = pg.image.load('img/humidity_day.png')
PRESSURE_DAY = pg.image.load('img/pressure_day.png')
WIND_NIGHT = pg.image.load('img/wind_night.png')
HUMIDITY_NIGHT = pg.image.load('img/humidity_night.png')
PRESSURE_NIGHT = pg.image.load('img/pressure_night.png')

# -- Fonts colors
GREY = (35, 35, 35)
GREEN = (0, 255, 60)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)