#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

# ==========================================================================
# =                  MACGYVER LABYRINTH GAME USING PYGAME                  =
# =                       OPENCLASSROOMS - PROJECT 03                      =
# =                                                                        =
# =  Help MacGyver to get out of the labyrinth.                            =
# =  He must get all items before he puts the guard to sleep and get out.  =
# =  Use direction arrows for MacGyver's moves                             =
# ==========================================================================

import os
import pygame
import classes as cl
import constantes as cst

os.system('clear')

pygame.init()

# //////////////////////// GAME WINDOWS INITIALISATION ///////////////////////
game_window = pygame.display.set_mode(
    (cst.WINDOW_RESOLUTION, cst.WINDOW_RESOLUTION + 55))
game_title = pygame.display.set_caption(cst.GAME_TITLE)
game_icon = pygame.image.load(cst.MACGYVER_PIC)
pygame.display.set_icon(game_icon)
pygame.display.flip()

# ///////////////////////////////// MAIN LOOP ////////////////////////////////

# Display items by default
show_needle = True
show_pipe = True
show_ether = True

# Initialize items count
count_item = 3

# Repeat move while arrow key is pressed
pygame.key.set_repeat(200, 200)

# Generate labyrinth by the file
show_game = cl.GameBoard('labyrinth')
show_game.generate_board()
show_game.display_board(game_window)
pygame.display.flip()

# Generate MacGyver and items
MAC = cl.Hero(cst.MACGYVER_PIC, show_game)          # Create MacGyver
NEEDLE = cl.Items(cst.NEEDLE_PIC, show_game)        # Create Item
NEEDLE.display_random(cst.NEEDLE_PIC, game_window)  # Init random position
PIPE = cl.Items(cst.PIPE_PIC, show_game)
PIPE.display_random(cst.PIPE_PIC, game_window)
ETHER = cl.Items(cst.ETHER_PIC, show_game)
ETHER.display_random(cst.ETHER_PIC, game_window)
SYRINGUE = cl.Items(cst.SYRINGUE_PIC, show_game)

run_window_loop = True
while run_window_loop:

    # 30 FPS limit
    pygame.time.Clock().tick(30)

    window_background = pygame.image.load(cst.BKG_PIC).convert_alpha()
    game_window.blit(window_background, [30, 30])

    # Close the game window by the CROSS button or press ESCAPE key
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and \
           event.key == pygame.K_ESCAPE:
            run_window_loop = False

        # MacGyver moves when directional arrows are pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                MAC.mac_direction('RIGHT')
            elif event.key == pygame.K_DOWN:
                MAC.mac_direction('DOWN')
            elif event.key == pygame.K_UP:
                MAC.mac_direction('UP')
            elif event.key == pygame.K_LEFT:
                MAC.mac_direction('LEFT')

    # Refresh new MacGyver position
    game_window.blit(window_background, [0, 0])
    show_game.display_board(game_window)
    game_window.blit(MAC.mac_pic, [MAC.mac_pos_x, MAC.mac_pos_y])

    # Display item at random position and
    # update count item if MacGyver picks up it
    if show_needle:
        game_window.blit(NEEDLE.item_pic,
                         [NEEDLE.item_pos_x, NEEDLE.item_pos_y])
        # If MacGyver position == Item position,
        # item dissapears and update count item
        if (MAC.mac_pos_x, MAC.mac_pos_y) == \
           (NEEDLE.item_pos_x, NEEDLE.item_pos_y):
            show_needle = False
            count_item -= 1
    # If item have been picked up, move it inside item bar at bootom of window
    else:
        game_window.blit(NEEDLE.item_pic, [0, 752])
    if show_pipe:
        game_window.blit(PIPE.item_pic, [PIPE.item_pos_x, PIPE.item_pos_y])
        if (MAC.mac_pos_x, MAC.mac_pos_y) == \
           (PIPE.item_pos_x, PIPE.item_pos_y):
            show_pipe = False
            count_item -= 1
    else:
        game_window.blit(PIPE.item_pic, [50, 752])
    if show_ether:
        game_window.blit(ETHER.item_pic, [ETHER.item_pos_x, ETHER.item_pos_y])
        if (MAC.mac_pos_x, MAC.mac_pos_y) == \
           (ETHER.item_pos_x, ETHER.item_pos_y):
            show_ether = False
            count_item -= 1
    else:
        game_window.blit(ETHER.item_pic, [100, 752])

    # When all items have been picked up,
    # MacGyver can go to the guardian and get out the labyrinth
    if show_needle is False and show_pipe is False and show_ether is False:
        game_window.blit(SYRINGUE.item_pic, [390, 752])

    # When MacGyver arrives in front of the guardian
    if show_game.game_design[MAC.cell_y][MAC.cell_x] == "G":
        if count_item == 0:
            # If MacGyver picked up all items, he wins
            game_window = pygame.display.set_mode(
                (cst.WINDOW_RESOLUTION, cst.WINDOW_RESOLUTION))
            game_window.blit(window_background, [0, 0])
            win_pic = pygame.image.load(cst.YOUWIN_PIC).convert_alpha()
            game_window.blit(win_pic, [0, 0])
        else:
            # Else, he loses
            game_window = pygame.display.set_mode(
                (cst.WINDOW_RESOLUTION, cst.WINDOW_RESOLUTION))
            game_window.blit(window_background, [0, 0])
            win_pic = pygame.image.load(cst.GAMEOVER_PIC).convert_alpha()
            game_window.blit(win_pic, [0, 0])

    pygame.display.flip()
