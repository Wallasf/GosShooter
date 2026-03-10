#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame


class Game:
    def __init__(self):
        pygame.init()
        window = pygame.display.set_mode(size=(600, 480))

    def run(self, ):
        while true:
            # check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # close window
                    pygame.quit()
                    quit()  # end pygame


from pygame.examples.go_over_there import screen
