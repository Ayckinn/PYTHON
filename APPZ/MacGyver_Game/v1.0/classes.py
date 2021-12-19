# ================================================
# = CLASSES FILE FOR THE MACGYVER LABYRINTH GAME =
# ================================================

import pygame
import random
import constantes as cst


class GameBoard:
    """ Class for creating the labyrinth using a file"""

    def __init__(self, file):
        self.file = file
        self.game_design = False

    # -------------------------------------------------------------------------
    def generate_board(self):
        """ Recover labyrinth design in several list for sprite management """
        with open(self.file, 'r') as file:
            general_list = []

            for line in file:
                sprite_list = []
                for sprite in line:
                    if sprite != "\n":
                        sprite_list.append(sprite)

                general_list.append(sprite_list)
            self.game_design = general_list

    # -------------------------------------------------------------------------
    def display_board(self, game_zone):
        """ Display the labyrinth with the generate_board() function """
        wall = pygame.image.load(cst.WALL_PIC).convert_alpha()
        guard = pygame.image.load(cst.GUARDIAN_PIC).convert_alpha()

        nb_lines = 0
        for line in self.game_design:
            nb_cell = 0
            for sprite in line:
                # Calculate the size of cells
                cell_x = nb_cell * cst.SPRITE_SIZE
                cell_y = nb_lines * cst.SPRITE_SIZE

                # Positioning walls and guardian and items :
                # 1 = walls - G = Guardian
                if sprite == "1":
                    game_zone.blit(wall, [cell_x, cell_y])
                elif sprite == "G":
                    game_zone.blit(guard, [cell_x, cell_y])

                # When the cell has been calculated and checked,
                # we go to the next
                nb_cell += 1
            # When the line is over, we go to the next
            nb_lines += 1


# /////////////////////////////////////////////////////////////////////////////
class Hero:
    """ Class for generating MacGyver and his moves """
    def __init__(self, mac_pic, game_zone):
        self.mac_pic = pygame.image.load(mac_pic).convert_alpha()

        # MacGyver initial position in the left top
        self.cell_x = 0
        self.cell_y = 0
        self.mac_pos_x = 0
        self.mac_pos_y = 0

        # Game zone
        self.game_zone = game_zone

    # -------------------------------------------------------------------------
    def mac_direction(self, direction):
        """ Function for manage MacGyver's moves """

        #  Move to right
        if direction == 'RIGHT':
            # Border window limit
            if self.cell_x < (cst.NB_SPRITES - 1):
                # Check destination cell is not a wall
                if self.game_zone.game_design[self.cell_y][self.cell_x + 1]\
                                                                        != "1":
                    # MacGyver can moves by one step to the right
                    self.cell_x += 1
                    # Calculate current position
                    self.mac_pos_x = self.cell_x * cst.SPRITE_SIZE

        if direction == 'DOWN':
            if self.cell_y < (cst.NB_SPRITES - 1):
                if self.game_zone.game_design[self.cell_y + 1][self.cell_x]\
                                                                        != "1":
                    self.cell_y += 1
                    self.mac_pos_y = self.cell_y * cst.SPRITE_SIZE

        if direction == 'UP':
            if self.cell_y > 0:
                if self.game_zone.game_design[self.cell_y - 1][self.cell_x]\
                                                                        != "1":
                    self.cell_y -= 1
                    self.mac_pos_y = self.cell_y * cst.SPRITE_SIZE

        if direction == 'LEFT':
            if self.cell_x > 0:
                if self.game_zone.game_design[self.cell_y][self.cell_x - 1]\
                                                                        != "1":
                    self.cell_x -= 1
                    self.mac_pos_x = self.cell_x * cst.SPRITE_SIZE


# /////////////////////////////////////////////////////////////////////////////
class Items:
    """ Clas for managing items, display and random position """
    def __init__(self, item_pic, game_zone):
        """ Function for initialize items and their random positions """
        self.item_pic = pygame.image.load(item_pic).convert_alpha()

        self.cell_x = 0
        self.cell_y = 0
        self.item_pos_x = 0
        self.item_pos_y = 0

        self.game_zone = game_zone

    # -------------------------------------------------------------------------
    def display_random(self, item_pic, game_zone):
        """ Generate the random position """
        self.get_item_loop = True
        while self.get_item_loop:
            # Randomize X and Y cells (15 sprites)
            self.cell_x = random.randint(0, 14)
            self.cell_y = random.randint(0, 14)

            # Check if the cell is empty, positioning and display item
            if self.game_zone.game_design[self.cell_y][self.cell_x] == "0":
                self.item_pos_x = self.cell_x * cst.SPRITE_SIZE
                self.item_pos_y = self.cell_y * cst.SPRITE_SIZE
                # After check, break the loop
                self.get_item_loop = False
