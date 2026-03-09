import pygame
from pygame.examples.go_over_there import screen

print("Setup Start")
pygame.init()

window = pygame.display.set_mode(size=(600, 480))

print("Setup End")

print("Loop Start")
while true:
    pass
    # check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # close window
            print("quitinn")
            pygame.quit()
            quit()  # end pygame
