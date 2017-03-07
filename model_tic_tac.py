"""
    Model for Super Tic Tac tic_tac_toe
    @Author Alex Chapman
    3/6/17
"""


import ast

D = 'Green'


class model(object):
    """
        class which handles the actual functioning of the server. Includes
        handling new users connecting, as well as clients sending commands
        such as color changes and click values.

        Attributes:
            SOCKET_LIST - List of addresses that have connected to server
            users       - List of user objects
            correlation - Dictionary that relates other two attributes
    """
    def __init__(self):
        """Returns model object"""
        # list of addresses
        self.socket_list = []
        # list of user objects
        self.users = []
        # dictionary relating users to addresses
        self.correlation = {}

    def save_val(self, thruput, member):
        """
            function call which allows data to be passed into the game field.
            Commands: 'hb'      - heartbeat message sent on loop to sync
                      'uCOLOR'  - sets the color of the user that calls it
                      '[x, y]'  - click value of given

            Input: thruput -> command or whatnot to be processed
                   member  -> address from which the message originated
        """
        # figures out which user sent the message
        to_use = self.correlation[member]

        # if the command is the color set
        if thruput[0] == 'u':
            to_use.set_color(thruput[1:])
            print(member, thruput[1:])

        # on the click command check if it is that user's turn
        elif to_use.turn_state:
            try:
                # if hb is appended to the end of the click, remove it
                if 'hb' in thruput and len(thruput) > 2:
                    thruput = thruput[:len(thruput)-2]

                # interperet point input as list
                ls = ast.literal_eval(thruput)

                # passes the point value down to the user and returns if
                # the turn was successfully passed
                if to_use.input(ls):
                    # change whos turn it is
                    self.change_turns()
                    print('Turns Changed.')
                else:
                    print('Invalid Click. Still your turn.')
            except (SyntaxError, ValueError) as e:
                if(thruput == 'hb'):
                    pass
                else:
                    print('didnt work' + thruput)
                pass
        else:
            if(thruput == 'hb'):
                pass
            else:
                print('not your turn ' + str(member))
            pass

    def update_socket_list(self, thruput):
        """
            called upon clients connection, creates and establishes list of
            addresses which are in turn paired with user objects.

            inputs: thruput -> address of most recently connected machine
        """
        if thruput not in self.socket_list:  # if address not already listed
            self.socket_list.append(thruput)
            # print(len(self.socket_list))
            # the first user has a predefined 'x' char (now irrelevant)
            if len(self.socket_list) == 1:
                # first user to connect gets first turn
                self.users.append(user('x', True))
                # adds new user object to the dictionary so it can be found
                self.correlation[thruput] = self.users[0]

            # see above
            elif len(self.socket_list) == 2:
                self.users.append(user('o', False))
                self.correlation[thruput] = self.users[1]

            else:
                print('Invalid number of connections: 2 players expected.')
                print('Ignoring Extra Connection')
            # print(self.users)

    # changes the turns, excecution above
    def change_turns(self):
        """Changes the turns"""
        for u in self.users:
            u.flip_turn()


class tic_tac_toe(object):
    """
        Class which handles the creation of game objects for each of the 9
        major game tiles. Contains a 3x3 matrix of color vals, with the
        default color being defined at the top of the file.

        Attributes:
            focus - whether or not the game matrix is in focus (playable)
            state - 3x3 matrix holding the values of that specific board
    """
    def __init__(self, f, x=0, y=0):
        """Returns new tic_tac_toe object"""
        self.focus = f
        self.state = [[D, D, D],
                      [D, D, D],
                      [D, D, D]]

    def __str__(self):
        """Returns string representation of tic_tac_tow object"""
        to_return = (str(self.state[0]) + '\n' +
                     str(self.state[1]) + '\n' +
                     str(self.state[2]) + '\n')
        return to_return

    def add_char(self, char, i, j):
        """
            Function which handles an attempted click: i.e. adding a new color
            to the game matrix if the box clicked on is empty.
        """
        if self.state[i][j] is D:
            self.state[i][j] = char
            print('Clicked Valid Box.')
            return True
        else:
            print('Box already taken.')
            return False

    def on_click(self, x, y, char):
        """
            Called by the user on click of the specific sub-game board.

            Inputs:
                x    - decimal representation of click on the bigger board
                y    - decimal representation of click on the bigger board
                char - color string of calling user
        """
        x = x * 3
        y = y * 3

        # converts the decimal point to row and column clicked
        j = helper_func(x)
        i = helper_func(y)

        # only excecutes if the square clicked is unoccupied and in focus
        if self.add_char(char, i, j):
            # changes the big-board focus to the equivalent of the square clkd.
            change_focus(int(j), int(i))
            return True
        else:
            return False

    def check_if_won(self):
        """
            Method to check the state matrix of the board to evaluate wheteher
            or not it has been won. If won, it returns the winning string. If
            not, returns the default string (D)
        """
        # checks if the rows have a winner
        for row in self.state:
            if(row[0] == row[1] and row[0] == row[2]):
                return row[0]

        # checks if the columns have a winner
        for column in range(0, len(self.state)):
            one = self.state[0][column]
            two = self.state[1][column]
            three = self.state[2][column]
            if(one == two and one == three):
                return one

        # checks if the upper-left bottom-right diagonal has a winner
        one = self.state[0][0]
        two = self.state[1][1]
        three = self.state[2][2]
        if(one == two and one == three):
            return one

        # checks if the other diagonal has a winner
        one = self.state[0][2]
        three = self.state[2][0]
        if(one == two and one == three):
            return one
        return D

    def get_to_send(self):
        """
            Returns nested list to send to clients
            Format:
                [[ROW],[ROW],[ROW]]
                    L ROW = [focus, < 9 length list of all square values >]
        """
        ls = []
        ls.append(self.focus)
        # print(self.state)
        if self.state is not None:
            for i in self.state:
                for q in i:
                    ls.append(q)
        return ls


class user(object):
    """
        User object designed to create a profile for each client that connects
        to the game. Also handles all high-level click functionality.

        Attributes:
            char        - string representing the color of the user, set by
                            uCOLOR command upon client initialization.
            turn_state  - Boolean representing whether or not it is this user's
                            turn.
    """
    def __init__(self, char=D, turn_state=False):
        """Returns a user object"""
        # sets the color to default, to be set by first client operation.
        self.char = char
        self.turn_state = turn_state

    def input(self, ls):
        """
            Accepts the point value of the clicked position as a decimal fro 0-1
            in both the x and y direction. Calculates which large tile is
            clicked on, and then calls that tile with the same clicked point.

            Input: point of click in the form [x, y]
        """
        click_x = ls[0]
        click_y = ls[1]

        # converts the decimal point to row and column clicked
        i = helper_func(click_x)
        j = helper_func(click_y)
        # print('box clicked on:', i, ':', j)
        # print('box in focus:', get_board_focus())
        if main_board[j][i].focus:
            # HIGHEST LEVEL CLICK MANAGEMENT
            # attempts to add color to the clicked-on board
            return main_board[j][i].on_click(click_x - i/3,
                                             click_y - j/3,
                                             self.char)
        else:
            return False

    def flip_turn(self):
        self.turn_state = not self.turn_state

    def set_color(self, color):
        self.char = color


def helper_func(val):
    """
        Function independent of a class, designed to convert a decimal into
        its corresponding integer value. Assumes 3 columns / rows.

        Input: Must be between 0 and 1 to function correctly
    """
    if val > 2/3:
        i = 2
    elif val < 1/3:
        i = 0
    else:
        i = 1
    return i


def change_focus(row, column):
    """
        Changes focus to the new main tile. takes a row and column integer as
        inputs, must be between 0-2 for both.
    """
    # sets all foci to false
    for rw in main_board:
        for game in rw:
            game.focus = False
    # goes to the single board that should be in focus and sets its focus
    main_board[column][row].focus = True
    print('focus on:', column, row)


# Initializes the base variable which holds the game boards needed
main_board = [[tic_tac_toe(True), tic_tac_toe(False), tic_tac_toe(False)],
              [tic_tac_toe(False), tic_tac_toe(False), tic_tac_toe(False)],
              [tic_tac_toe(False), tic_tac_toe(False), tic_tac_toe(False)]]


def check_if_won(board):
    """
        Function used to check if the main board has been won.

        Inputs: board - main game board to be checked.
        Output: string representing the color of the winner, if not the def.
    """
    # Finds out if each individual board has been won.
    ls = []
    for i in board:
        ts = []
        for v in i:
            ts.append(v.check_if_won)

    # checks if the rows have a winner
    for row in ls:
        if(row[0] == row[1] and row[0] == row[2]):
            return row[0]

    # checks if the columns have a winner
    for column in range(0, len(ls)):
        one = ls[0][column]
        two = ls[1][column]
        three = ls[2][column]
        if(one == two and one == three):
            return one

    # checks if the upper-left bottom-right diagonal has a winner
    one = ls[0][0]
    two = ls[1][1]
    three = ls[2][2]
    if(one == two and one == three):
        return one

    # checks if the other diagonal has a winner
    one = ls[0][2]
    three = ls[2][0]
    if(one == two and one == three):
        return one
    return D


def get_board_state():
    """
        Converts the game board into a readable form for sending to the clients
    """
    ls = []
    for row in main_board:
        ts = []
        for val in row:
            # print(val.get_to_send())
            ts.append(val.get_to_send())
        ls.append(ts)
    return ls


def get_board_focus():
    """Returns the index of the cell that is in focus"""
    for i, row in enumerate(main_board):
        for o, column in enumerate(row):
            if column.focus == 1:
                return str(i) + ':' + str(o)
    return 'none in focus'
