"""
This is a simple tic tac toe game that is meant to be implemented
as a multiplayer game.
I can be modified to play with the computer, however the default is
with another player

@Author: Peter Seger
"""


class board():
    """
    This is the game board which contains functions to:
    -Create the board
    -Update the board
    -Print the board
    -Add a play piece
    -Clear the board
    """

    def __init__(self):
        self.board_vals = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}

    def print_board(self):
        print('   |   |')
        print(' ' + self.board_vals[1] + ' | ' + self.board_vals[2] + ' | ' + self.board_vals[3])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board_vals[4] + ' | ' + self.board_vals[5] + ' | ' + self.board_vals[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board_vals[7] + ' | ' + self.board_vals[8] + ' | ' + self.board_vals[9])
        print('   |   |')

    def insert_play(self, play, play_piece):
        self.board_vals[play] = play_piece


if __name__ == '__main__':
    test = board()
    test.insert_play(5, 'X')
    test.print_board()
