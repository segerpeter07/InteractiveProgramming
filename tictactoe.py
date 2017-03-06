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


class TicTacToeModel:
    """ Encodes the game state """
    def __init__(self):
        self.piece = []
        x_pos = list(range(0, 900, 105))
        y_pos = list(range(0, 900, 105))
        self.boards = []
        numboard = 9
        for i in range(numboard):
            pieces = []
            for x in x_pos:
                for y in y_pos:
                    piece = Piece('Purple', 20, 20, x, y)
                    piece.set_color()
                    self.piece.append(piece)
                    pieces.append(piece)
            self.boards.append(board)


class Piece:
    def __init__(self, color, height=20, width=20, counter, x=0, y=0):
        self.color = color
        self.height = height
        self.width = width
        self.counter = counter
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
        self.screen.fill(pygame.Color(25, 25, 25))
        # Draw vertical division lines
        pygame.draw.line(self.screen, pygame.Color(125, 125, 125), (300, 0), (300, 900), 5)
        pygame.draw.line(self.screen, pygame.Color(125, 125, 125), (600, 0), (600, 900), 5)

        # Draw horizontal division lines
        pygame.draw.line(self.screen, pygame.Color(125, 125, 125), (0, 300), (900, 300), 5)
        pygame.draw.line(self.screen, pygame.Color(125, 125, 125), (0, 600), (900, 600), 5)

        for pieces in self.model.piece:
            pygame.draw.rect(self.screen, pygame.Color(pieces.color), pygame.Rect(pieces.x, pieces.y, pieces.width, pieces.height))
        pygame.display.update()


"""********************"""


class WholeGame():
    def __init__(self, games):
        pygame.init()
        self.games = games
        self.size = (900, 900)
        self.screen = pygame.display.set_mode(self.size)
        self.model = Build_Model(self.games)
        self.view = View_Setup(self.model, self.screen)


class Game():
    def __init__(self, pieces, counter):
        self.pieces = pieces    # List of game pieces
        self.counter = counter


def readin_data(data):
    """
    This function takes a list of nested lists and does the following:
    -unzips unto each game
    -makes board objects for each game
        -makes pieces objects for each board

    Returns all the pieces with the correct x and y values
    """
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
    game9 = row3[4]

    games = [game1, game2, game3, game4, game5, game6, game7, game8, game9]
    game_objs = []
    # build a list of pieces for each game with [0] being the focus value
    game_counter = 0
    for counts in games:
        piece_counter = 0
        pieces = []
        for pieces in counts:
            if pieces == 0 or pieces == 1:
                pieces.append(i)
            else:
                piece = Piece(i, piece_coutner)
            counter += 1
            piece.append(piece)
        game = Game(pieces, game_counter)
        game_objs.append(game)
        game_counter += 1
    coordinated_pieces = Coordiated_Piece(game_objs)
    return coordinated_pieces


class Coordiated_Piece():
    """
    This class builds a model by placing the pieces in their locations
    Takes: list of game objects and creates a model to be used
    """
    def __init__(self, games):
        self.games = games
        # Assign location values for each piece according to its number

        # Game 1
        self.games[0].pieces[0].x = 20
        self.games[0].pieces[0].y = 20
        self.games[0].pieces[1].x = 60
        self.games[0].pieces[1].y = 20
        self.games[0].pieces[2].x = 100
        self.games[0].pieces[2].y = 20
        self.games[0].pieces[3].x = 20
        self.games[0].pieces[3].y = 60
        self.games[0].pieces[4].x = 60
        self.games[0].pieces[4].y = 60
        self.games[0].pieces[5].x = 100
        self.games[0].pieces[5].y = 60
        self.games[0].pieces[6].x = 20
        self.games[0].pieces[6].y = 100
        self.games[0].pieces[7].x = 60
        self.games[0].pieces[7].y = 100
        self.games[0].pieces[8].x = 100
        self.games[0].pieces[8].y = 100

        # Game 2
        self.games[1].pieces[0].x = 140
        self.games[1].pieces[0].y = 20
        self.games[1].pieces[1].x = 180
        self.games[1].pieces[1].y = 20
        self.games[1].pieces[2].x = 220
        self.games[1].pieces[2].y = 20
        self.games[1].pieces[3].x = 140
        self.games[1].pieces[3].y = 60
        self.games[1].pieces[4].x = 180
        self.games[1].pieces[4].y = 60
        self.games[1].pieces[5].x = 220
        self.games[1].pieces[5].y = 60
        self.games[1].pieces[6].x = 140
        self.games[1].pieces[6].y = 100
        self.games[1].pieces[7].x = 180
        self.games[1].pieces[7].y = 100
        self.games[1].pieces[8].x = 220
        self.games[1].pieces[8].y = 100

        # Game 3
        self.games[2].pieces[0].x = 260
        self.games[2].pieces[0].y = 20
        self.games[2].pieces[1].x = 300
        self.games[2].pieces[1].y = 20
        self.games[2].pieces[2].x = 340
        self.games[2].pieces[2].y = 20
        self.games[2].pieces[3].x = 260
        self.games[2].pieces[3].y = 40
        self.games[2].pieces[4].x = 300
        self.games[2].pieces[4].y = 40
        self.games[2].pieces[5].x = 340
        self.games[2].pieces[5].y = 40
        self.games[2].pieces[6].x = 260
        self.games[2].pieces[6].y = 100
        self.games[2].pieces[7].x = 300
        self.games[2].pieces[7].y = 100
        self.games[2].pieces[8].x = 340
        self.games[2].pieces[8].y = 100

        # Game 4
        self.games[3].pieces[0].x = 20
        self.games[3].pieces[0].y = 140
        self.games[3].pieces[1].x = 60
        self.games[3].pieces[1].y = 140
        self.games[3].pieces[2].x = 100
        self.games[3].pieces[2].y = 140
        self.games[3].pieces[3].x = 20
        self.games[3].pieces[3].y = 200
        self.games[3].pieces[4].x = 60
        self.games[3].pieces[4].y = 200
        self.games[3].pieces[5].x = 100
        self.games[3].pieces[5].y = 200
        self.games[3].pieces[6].x = 20
        self.games[3].pieces[6].y = 240
        self.games[3].pieces[7].x = 60
        self.games[3].pieces[7].y = 240
        self.games[3].pieces[8].x = 100
        self.games[3].pieces[8].y = 240

        # Game 5
        self.games[4].pieces[0].x = 140
        self.games[4].pieces[0].y = 140
        self.games[4].pieces[1].x = 180
        self.games[4].pieces[1].y = 140
        self.games[4].pieces[2].x = 220
        self.games[4].pieces[2].y = 140
        self.games[4].pieces[3].x = 140
        self.games[4].pieces[3].y = 200
        self.games[4].pieces[4].x = 180
        self.games[4].pieces[4].y = 200
        self.games[4].pieces[5].x = 220
        self.games[4].pieces[5].y = 200
        self.games[4].pieces[6].x = 140
        self.games[4].pieces[6].y = 240
        self.games[4].pieces[7].x = 180
        self.games[4].pieces[7].y = 240
        self.games[4].pieces[8].x = 220
        self.games[4].pieces[8].y = 240

        # Game 6
        self.games[5].pieces[0].x = 260
        self.games[5].pieces[0].y = 140
        self.games[5].pieces[1].x = 300
        self.games[5].pieces[1].y = 140
        self.games[5].pieces[2].x = 340
        self.games[5].pieces[2].y = 140
        self.games[5].pieces[3].x = 260
        self.games[5].pieces[3].y = 200
        self.games[5].pieces[4].x = 300
        self.games[5].pieces[4].y = 200
        self.games[5].pieces[5].x = 340
        self.games[5].pieces[5].y = 200
        self.games[5].pieces[6].x = 260
        self.games[5].pieces[6].y = 240
        self.games[5].pieces[7].x = 300
        self.games[5].pieces[7].y = 240
        self.games[5].pieces[8].x = 340
        self.games[5].pieces[8].y = 240

        # Game 7
        self.games[6].pieces[0].x = 20
        self.games[6].pieces[0].y = 300
        self.games[6].pieces[1].x = 60
        self.games[6].pieces[1].y = 300
        self.games[6].pieces[2].x = 100
        self.games[6].pieces[2].y = 300
        self.games[6].pieces[3].x = 20
        self.games[6].pieces[3].y = 340
        self.games[6].pieces[4].x = 60
        self.games[6].pieces[4].y = 340
        self.games[6].pieces[5].x = 100
        self.games[6].pieces[5].y = 340
        self.games[6].pieces[6].x = 20
        self.games[6].pieces[6].y = 380
        self.games[6].pieces[7].x = 60
        self.games[6].pieces[7].y = 380
        self.games[6].pieces[8].x = 100
        self.games[6].pieces[8].y = 380

        # Game 8
        self.games[7].pieces[0].x = 140
        self.games[7].pieces[0].y = 300
        self.games[7].pieces[1].x = 180
        self.games[7].pieces[1].y = 300
        self.games[7].pieces[2].x = 220
        self.games[7].pieces[2].y = 300
        self.games[7].pieces[3].x = 140
        self.games[7].pieces[3].y = 340
        self.games[7].pieces[4].x = 180
        self.games[7].pieces[4].y = 340
        self.games[7].pieces[5].x = 220
        self.games[7].pieces[5].y = 340
        self.games[7].pieces[6].x = 140
        self.games[7].pieces[6].y = 380
        self.games[7].pieces[7].x = 180
        self.games[7].pieces[7].y = 380
        self.games[7].pieces[8].x = 220
        self.games[7].pieces[8].y = 380

        # Game 9
        self.games[8].pieces[0].x = 260
        self.games[8].pieces[0].y = 300
        self.games[8].pieces[1].x = 300
        self.games[8].pieces[1].y = 300
        self.games[8].pieces[2].x = 340
        self.games[8].pieces[2].y = 300
        self.games[8].pieces[3].x = 260
        self.games[8].pieces[3].y = 340
        self.games[8].pieces[4].x = 300
        self.games[8].pieces[4].y = 340
        self.games[8].pieces[5].x = 340
        self.games[8].pieces[5].y = 340
        self.games[8].pieces[6].x = 260
        self.games[8].pieces[6].y = 380
        self.games[8].pieces[7].x = 300
        self.games[8].pieces[7].y = 380
        self.games[8].pieces[8].x = 340
        self.games[8].pieces[8].y = 380

        # Set colors for each point
        for i in range(9):
            for j in range(9):
                self.games[i].pieces[j].color = self.games[i].pieces[j]

        # game_pieces = []
        # i = 1
        # for game in games:
        #     pieces = []
        #     j = 1
        #     for Piece in game:
        #         Piece.x = j * 20
        #         Piece.y =
        #         j += 1
        #     i += 1


class View_Setup():
    """
    This class sets up the board correctly and draws the pieces in their place
    """
    def __init__(self, model, screen):
        self.model = model
        self.screen = screen

    # TODO
    # Modify
    def draw(self):
        self.screen.fill(pygame.Color(25, 25, 25))
        # Draw vertical division lines
        pygame.draw.line(self.screen, pygame.Color(125, 125, 125), (300, 0), (300, 900), 5)
        pygame.draw.line(self.screen, pygame.Color(125, 125, 125), (600, 0), (600, 900), 5)

        # Draw horizontal division lines
        pygame.draw.line(self.screen, pygame.Color(125, 125, 125), (0, 300), (900, 300), 5)
        pygame.draw.line(self.screen, pygame.Color(125, 125, 125), (0, 600), (900, 600), 5)

        for i in self.model.piece.games:
            for j in i.pieces:
                pygame.draw.rect(self.screen, pygame.Color(j.color), pygame.Rect(j.x, j.y, j.width, j.height))
        pygame.display.update()


def make_game(pieces, focus):
    """
    This function makes a game board object and fills it with the pieces given
    in the correct locations
    """
    game = Board()
    game.pieces = pieces
    game.focus = focus

    # Redundent?!?!?!


"""********************"""

if __name__ == '__main__':
    pygame.init()

    size = (900, 900)
    screen = pygame.display.set_mode(size)

    model = TicTacToeModel()
    view = PyGameWindowView(model, screen)
    # controller = PyGameMouseController(model)

    running = True

    """Prompt user to select color"""
    # name = input("What you want your name to be? ")
    color = input("What do you want your color to be? ")
    player1 = Player('player1', color)

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for boards in model.boards:
                    for pieces in boards.pieces:
                        if pieces.collision(x, y):
                            # print("collision at: " + str(pieces.x) + ' ' + str(pieces.y))
                            if pieces.color == 'Green':
                                pieces.set_color(player1.color)
                            elif pieces.color == player1.color:
                                pieces.set_color('Green')
        view.draw()
        time.sleep(.001)

    pygame.quit()
