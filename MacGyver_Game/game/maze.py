# ==============================================
# = Module for labyrinth design and management =
# ==============================================

import pygame as pg
from random import sample
from game import constants as cst


class GameBoard(list):

    def __init__(self):
        # -- Init game window
        self.master = pg.display.set_mode((cst.WINSIZE, cst.WINSIZE + 55))
        self.title = pg.display.set_caption(cst.GAME_TITLE)
        self.icon = cst.MACGYVER_PIC
        pg.display.set_icon(self.icon)

        # -- Init game pictures
        self.wallpic = cst.FULLWALL_PIC.convert_alpha()
        self.guardpic = cst.GUARDIAN_PIC.convert_alpha()
        self.bground = cst.BKG_PIC.convert_alpha()
        self.syringepic = cst.SYRINGE_PIC.convert_alpha()
        self.win = cst.YOUWIN_PIC.convert_alpha()
        self.loose = cst.GAMEOVER_PIC.convert_alpha()
        self.itempic = (cst.NEEDLE_PIC.convert_alpha(),
                        cst.PIPE_PIC.convert_alpha(),
                        cst.ETHER_PIC.convert_alpha())
        # -- List for storing pics and their positions
        self.image_position_list = []
        # -- Repeat the moves when the arrow keys are held down.
        pg.key.set_repeat(50, 100)

    # ------------------------------------------------------------------------
    def lab_struct(self):
        # -- Init structure of the labyrinth
        with open('game/labyrinth') as maze:
            maze = ''.join(maze.read().splitlines())
            # -- Init empty sprites positions
            self.extend([divmod(idx, 15) for idx, value in enumerate(maze)
                        if value == '0'])
            # -- Init guardian position
            self.guardpos = divmod(maze.find('G'), 15)
            # -- Init the 3 items random positions
            self.itempos = sample(self[1:], 3)

            return self

    # -------------------------------------------------------------------------
    def draw_objects(self):
        # -- Display walls as background
        self.master.blit(self.wallpic, (0, 0))
        # -- Draw the empty path
        for emptypos_y, emptypos_x in self:
            self.master.blit(self.bground, (emptypos_x * 50, emptypos_y * 50),
                             (emptypos_x * 50, emptypos_y * 50, 50, 50))
        # -- Display and positioning guardian
        guardpos_y, guardpos_x = self.guardpos
        self.master.blit(self.bground, (guardpos_x * 50, guardpos_y * 50),
                         (guardpos_x * 50, guardpos_y * 50, 50, 50))
        self.master.blit(self.guardpic, (guardpos_x * 50, guardpos_y * 50))
        # -- Without it, MacGyver can't get into the same cell with the guard
        self.extend([self.guardpos])
        # -- Display and positioning items
        for item, (pos_y, pos_x) in zip(self.itempic, self.itempos):
            self.master.blit(item, (pos_x * 50, pos_y * 50))
            # -- Add item and their position in tuple in list
            self.image_position_list.append((item, (pos_y, pos_x)))

    # -------------------------------------------------------------------------
    def itembar(self, item, counter):
        # -- Decrease counter
        if counter.get_counter_value() == 2:
            # -- Positioning the item in itembar
            self.master.blit(item, (0, 752))
        if counter.get_counter_value() == 1:
            self.master.blit(item, (50, 752))
        if counter.get_counter_value() == 0:
            self.master.blit(item, (100, 752))
            self.master.blit(self.syringepic, (390, 752))

    # -------------------------------------------------------------------------
    def win_loose(self, player, counter):
        if self.guardpos == player.macpos:
            if counter.get_counter_value() == 0:
                self.endgame = pg.display.set_mode((cst.WINSIZE, cst.WINSIZE))
                self.endgame.blit(self.win, (0, 0))
            else:
                self.endgame = pg.display.set_mode((cst.WINSIZE, cst.WINSIZE))
                self.endgame.blit(self.loose, (0, 0))
