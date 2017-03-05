"""
This is a simple tic tac toe game that is meant to be implemented
as a multiplayer game.
I can be modified to play with the computer, however the default is
with another player

@Author: Peter Seger
"""
import pygame
import time


class Board():
    def __init__(self, height=300, width=300):
        self.height = height
        self.width = width


class Player():
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def set_color(self, color):
        self.color = color

    def set_name(self, name='Player'):
        self.name = name

    def print_info(self):
        return 'Player name: ' + self.name + ' Player color: ' + self.color


class TicTacToeModel:
    """ Encodes the game state """
    def __init__(self):
        self.piece = []
        x_pos = [100, 400, 700]
        y_pos = [100, 400, 700]
        for x in x_pos:
            for y in y_pos:
                piece = Piece('Purple', 20, 20, x, y)
                piece.set_color()
                self.piece.append(piece)


class Piece:
    def __init__(self, color, height, width, x, y):
        self.color = color
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    def set_color(self, color='Green'):
        self.color = color

    def get_color(self):
        return 'hello' + self.color

    def collision(self, x, y):
        x_range = range(self.x, self.x + 20)
        y_range = range(self.y, self.y + 20)
        if x in x_range and y in y_range:
            return True
        else:
            return False


class PyGameWindowView:
    def __init__(self, model, screen):
        self.model = model
        self.screen = screen

    def draw(self):
        self.screen.fill(pygame.Color(0, 0, 0))
        for pieces in self.model.piece:
            pygame.draw.rect(self.screen, pygame.Color(pieces.color), pygame.Rect(pieces.x, pieces.y, pieces.width, pieces.height))
        pygame.display.update()


if __name__ == '__main__':
    pygame.init()

    size = (840, 840)
    screen = pygame.display.set_mode(size)

    model = TicTacToeModel()
    view = PyGameWindowView(model, screen)
    # controller = PyGameMouseController(model)

    running = True

    """Prompt user to select color"""
    name = input("What you want your name to be? ")
    color = input("What do you want your color to be? ")
    player1 = Player(name, color)

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for pieces in model.piece:
                    if pieces.collision(x, y):
                        # print("collision at: " + str(pieces.x) + ' ' + str(pieces.y))
                        if pieces.color == 'Green':
                            pieces.set_color(player1.color)
                        elif pieces.color == player1.color:
                            pieces.set_color('Green')
        view.draw()
        time.sleep(.001)

    pygame.quit()
