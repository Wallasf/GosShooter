#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Menu import Menu


class Game:
    def __init__(self):
        self.window = pygame.display.set_mode(size=(600, 480))
        pygame.init()


    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass



            # check for all events
            # for event in pygame.event.get():
            #   if event.type == pygame.QUIT:  # close window
            #       pygame.quit()
            #       quit()  # end pygame


from pygame.examples.go_over_there import screen
