# ==================================
# = Module for MacGyver management =
# ==================================

import pygame as pg
from game import constants as cst


class McGyver(object):

    def __init__(self, screen):
        self.bground = cst.BKG_PIC.convert_alpha()
        self.syringepic = cst.SYRINGE_PIC.convert_alpha()
        self.macpic = cst.MACGYVER_PIC.convert_alpha()
        self.macpos = (0, 0)

        self.screen = screen
        self.screen.master.blit(self.macpic, self.macpos)

        # -- MacGyver with arrow keys
        self.arrows = {pg.K_UP: (-1, 0),
                       pg.K_DOWN: (1, 0),
                       pg.K_LEFT: (0, -1),
                       pg.K_RIGHT: (0, 1)}

    # -------------------------------------------------------------------------
    def del_mac(self):
        macpos_y, macpos_x = self.macpos
        self.screen.master.blit(self.bground, (macpos_x * 50, macpos_y * 50),
                                (macpos_x * 50, macpos_y * 50, 50, 50))

    # -------------------------------------------------------------------------
    def update_mac(self, key, board):
        """ Get arrows direction and move MacGyver to the right position """
        macpos_y, macpos_x = self.macpos

        offset_y, offset_x = self.arrows.get(key, (50, 0))
        if (macpos_y + offset_y, macpos_x + offset_x) in board:
            self.macpos = (macpos_y + offset_y, macpos_x + offset_x)

    # -------------------------------------------------------------------------
    def show_mac(self):
        macpos_y, macpos_x = self.macpos
        self.screen.master.blit(self.macpic, (macpos_x * 50, macpos_y * 50))

    # -------------------------------------------------------------------------
    def pickup(self, board, counter):
        if self.macpos in board.itempos:
            for item, (imgpos_y, imgpos_x) in board.image_position_list:
                if self.macpos == (imgpos_y, imgpos_x):
                    counter.decrease()
                    board.itembar(item, counter)

            board.itempos.remove(self.macpos)
