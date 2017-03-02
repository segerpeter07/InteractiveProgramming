from com_client import client
import pygame
import sys
import time

pygame.init()
pygame.display.set_mode((100, 100))

c = client()
c.check_messages()

# here we define which button moves to which direction
controller_map = {pygame.K_LEFT: 0,
                  pygame.K_RIGHT: 1,
                  pygame.K_UP: 2,
                  pygame.K_DOWN: 3,
                  pygame.K_SPACE: 4}


def check_keys():
    # ERROR: CANT CLOSE WINDOW
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()

    # get all pressed keys
    pressed = pygame.key.get_pressed()
    # get all directions the ship should move
    return [controller_map[key] for key in controller_map if pressed[key]]


control_variable = 10
while(1):
    c.check_messages()
    temp = check_keys()
    # print(temp)
    if len(temp) != 0:
        # print(temp)
        c.send_message(str(temp))
    c.send_message('hb')
    time.sleep(.01)
