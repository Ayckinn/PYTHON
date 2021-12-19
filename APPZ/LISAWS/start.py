#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# ===================================================
# =    LISA WEATHER STATION                         =
# =      - Version  : 1.1                           =
# =      - Author   : Ayckinn                       =
# =      - Mail     : ayckinn@pm.me                 =
# =      - Release  : June 26' 2020                 =
# =      - Github   : https://github.com/Ayckinn    =
# ===================================================

import pygame as pg
from ui import screen
from updates import wupdate, loop

pg.init()

def main():
    mainwindow = screen.ClockBoard()
    lisawupd = wupdate.WeatherUpdate(mainwindow)
    lisaloop = loop.LoopStation()

    try:
        while True:
            lisawupd.full_update(lisaloop)
    except KeyboardInterrupt:
        print("\nStation shutdown...")


if __name__ == '__main__':
    main()
