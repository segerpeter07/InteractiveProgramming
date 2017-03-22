"""
This is a simple tic tac toe game that is meant to be implemented
as a multiplayer game.
It is the mega tic tac toe version that has nine game boards in
a master game board.

@Author: Peter Seger
"""
import pygame
import time


class Board():
    def __init__(self, pieces, focus, height=300, width=300, color='Grey'):
        self.focus = focus
        self.height = height
        self.width = width
        self.color = color
        self.pieces = pieces


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


class Piece:
    def __init__(self, color, height=20, width=20, x=0, y=0):
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


class Game():
    """
    This class contains all the pieces on the game board as well as information
    for the focus of the board, which shows which sub-game is being played
    """
    def __init__(self, pieces=[], focus=0):
        self.pieces = pieces    # List of game pieces
        self.focus = focus  # Focus used to determine if the game is active


def readin_data(data):
    """
    This function takes a list of nested lists and does the following:
    -unzips unto each game
    -makes board objects for each game
        -makes pieces objects for each board

    Returns all the pieces with the correct x and y values
    """
    width = 900  # This can be changed
    height = 900    # This can be changed

    row1 = data[0]
    row2 = data[1]
    row3 = data[2]

    game1 = row1[0]
    game2 = row1[1]
    game3 = row1[2]
    game4 = row2[0]
    game5 = row2[1]
    game6 = row2[2]
    game7 = row3[0]
    game8 = row3[1]
    game9 = row3[2]

    game_colors = [game1, game2, game3, game4, game5, game6, game7, game8, game9]
    game_objs = []
    # build a list of pieces for each game with [0] being the focus value
    j = 0
    for game in game_colors:
        gametemp = Game()
        pieces = []
        gametemp.focus = game[0]
        for i in range(1, 10):
            piece = Piece('Green')
            piece.color = game[i]
            piece.x = 0  # Set default x value
            piece.y = 0  # Set default y value
            piece.width = 20    # Set defualt square width
            piece.height = 20   # Set default squre height
            pieces.append(piece)
        gametemp.pieces = pieces
        game_objs.append(gametemp)
        j += 1

    print(game_objs[2].pieces[7].y)

    # Send list of game objs to get assigned x and y positions
    # comes back as a list of game objs
    coordinated_pieces = coordinate_pieces(game_objs, width, height)
    return coordinated_pieces


def coordinate_pieces(game_objs, width, height):
    """
    This function takes a list of game objects, the width & hieght of the board
    Returns the same list of game objects, except with x, y, and color
    """
    for row in range(9):
        for collumn in range(9):
            if row == 0 and collumn == 0:
                game_objs[row].pieces[collumn].x = 20
                game_objs[row].pieces[collumn].y = 20
            elif collumn == 0 and row != 0:
                game_objs[row].pieces[collumn].x = row * (height + 40) / 9 + 20
                game_objs[row].pieces[collumn].y = 20
            elif collumn != 0 and row == 0:
                game_objs[row].pieces[collumn].x = 20
                game_objs[row].pieces[collumn].y = collumn * (width + 40) / 9 + 20
            else:
                game_objs[row].pieces[collumn].x = row * (height + 40) / 9 + 20
                game_objs[row].pieces[collumn].y = collumn * (width + 40) / 9 + 20
    return game_objs


class Coordiated_Piece():
    """
    This class builds a model by placing the pieces in their locations
    Takes: list of game objects and creates a model to be used
    """
    def __init__(self, games=[], width=0, height=0):
        self.games = games
        self.width = width
        self.height = height
        # Assign location values for each piece according to its number

        for row in range(8):
            for collumn in range(8):
                if row == 0 or collumn == 0:
                    if collumn == 0 and row != 0:
                        self.games[row].pieces[collumn].x = 0
                        self.games[row].pieces[collumn].y = height - 9 * (height / row)
                    elif row == 0 and collumn != 0:
                        self.games[row].pieces[collumn].x = width - 9 * (height / collumn)
                        self.games[row].pieces[collumn].y = 0
                    else:
                        self.games[row].pieces[collumn].x = 0
                        self.games[row].pieces[collumn].y = 0
                else:
                    self.games[row].pieces[collumn].x = width - 9 * (width / collumn)
                    self.games[row].pieces[collumn].y = height - 9 * (height / row)

        # Set colors for each point
        for i in range(8):
            for j in range(8):
                self.games[i].pieces[j].color = self.games[i].pieces[j]


class View_Setup():
    """
    This class sets up the board correctly and draws the pieces in their place
    """
    def __init__(self, model, screen):
        self.model = model
        self.screen = screen

    def draw(self):
        self.screen.fill(pygame.Color(25, 25, 25))
        # Draw vertical division lines
        pygame.draw.line(self.screen, pygame.Color(125, 125, 125), (900 / 3, 0), (900 / 3, 900), 5)
        pygame.draw.line(self.screen, pygame.Color(125, 125, 125), (2*900/3, 0), (2*900/3, 900), 5)

        # Draw horizontal division lines
        pygame.draw.line(self.screen, pygame.Color(125, 125, 125), (0, 900/3), (900, 900/3), 5)
        pygame.draw.line(self.screen, pygame.Color(125, 125, 125), (0, 2*900/3), (900, 2*900/3), 5)

        for game in self.model:
            for piece in game.pieces:
                pygame.draw.rect(self.screen, pygame.Color(piece.color),
                                 pygame.Rect(piece.x, piece.y,
                                             piece.width, piece.height))
        pygame.display.update()


if __name__ == '__main__':
    pygame.init()

    size = (900, 900)
    screen = pygame.display.set_mode(size)

    data = [[[0,"Purple","Green","Green","Green","Green","Green","Green","Green","Green"],[0,"Green","Green","Green","Green","Green","Green","Green","Green","Green"],[0,"Purple","Green","Green","Green","Green","Green","Green","Green","Green"]],[[0,"Green","Green","Green","Green","Green","Green","Green","Green","Green"],[0,"Green","Green","Green","Green","Green","Green","Green","Green","Green"],[0,"Purple","Green","Green","Green","Green","Green","Green","Green","Green"]],[[0,"Green","Green","Green","Green","Green","Green","Green","Green","Green"],[0,"Green","Green","Green","Green","Green","Green","Green","Green","Green"],[0,"Green","Green","Green","Green","Green","Green","Green","Green","Green"]]]
    model = readin_data(data)
    view = View_Setup(model, screen)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        view.draw()

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for boards in model.boards:
                    for pieces in boards.pieces:
                        if pieces.collision(x, y):
                            if pieces.color == 'Green':
                                pieces.set_color(player1.color)
                            elif pieces.color == player1.color:
                                pieces.set_color('Green')
        # view.draw()
        time.sleep(.001)

    pygame.quit()
