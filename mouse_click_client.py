from com_client import client
import pygame
import sys
import time

BLUE = (0, 0, 255)

width = 500
pygame.init()
# pygame.display.set_mode((1000, 1000))
screen = pygame.display.set_mode((width, width))

c = client()
c.check_messages()


def check_mouse():
    # ERROR: CANT CLOSE WINDOW
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            return pygame.mouse.get_pos()


def draw():
    screen.fill((255, 255, 255))
    pygame.draw.lines(screen, BLUE, False, [[0, width / 3], [width, width/3],
                                            [0, 2/3 * width], [width, 2/3 * width],
                                            [width / 3, 0], [width / 3, width],
                                            [2/3 * width, 0], [2/3 * width, width]], 5)

    pygame.display.flip()


while(1):
    draw()
    c.check_messages()
    temp = check_mouse()
    if temp is not None:
        send = '[' + str(temp[0] / width) + ', ' + str(temp[1] / width) + ']'
        print(send)
        c.send_message(str(send))
    c.send_message('hb')
    time.sleep(.01)
