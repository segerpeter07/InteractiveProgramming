import ast

D = 'blank'


class model(object):
    def __init__(self):
        self.socket_list = []
        self.users = []
        self.correlation = {}

    def save_val(self, thruput, member):
        # print('saving', thruput)
        # print(thruput)
        to_use = self.correlation[member]
        if thruput[0] == 'u':
            to_use.set_color(thruput[1:])
            print(member, thruput[1:])
        elif to_use.turn_state:
            try:
                if 'hb' in thruput and len(thruput) > 2:
                    thruput = thruput[:len(thruput)-2]
                ls = ast.literal_eval(thruput)
                if to_use.input(ls):
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
                print('not your turn' + str(member))
            pass

    def update_socket_list(self, thruput):
        if thruput not in self.socket_list:
            self.socket_list.append(thruput)
            print(len(self.socket_list))
            if len(self.socket_list) == 1:
                self.users.append(user('x', True))
                self.correlation[thruput] = self.users[0]

            elif len(self.socket_list) == 2:
                self.users.append(user('o', False))
                self.correlation[thruput] = self.users[1]

            else:
                print('Invalid number of connections: 2 players expected.')
                print('Ignoring Extra Connection')
            print(self.users)

    def change_turns(self):
        for u in self.users:
            u.flip_turn()


class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def multiply_by(self, coefficient):
        return Point(self.x * coefficient, self.y * coefficient)

    def add(self, other_point):
        return Point(self.x + other_point.x, self.y + other_point.y)

    def __str__(self):
        return '{} {}'.format(self.x, self.y)


class tic_tac_toe(object):
    def __init__(self, f, x=0, y=0, size=100):
        self.origin = Point(x, y)
        self.size = size
        self.focus = f
        self.state = [[D, D, D],
                      [D, D, D],
                      [D, D, D]]

    def __str__(self):
        to_return = str(self.state[0]) + '\n' + str(self.state[1]) + '\n' + str(self.state[2]) + '\n'
        return to_return

    def add_char(self, char, i, j):
        if self.state[i][j] is D:
            self.state[i][j] = char
            print('Clicked Valid Box.')
            return True
        else:
            print('Box already taken')
            return False

    def on_click(self, x, y, char):
        x = x * 3
        y = y * 3
        print(x, y)
        j = helper_func(x)
        i = helper_func(y)
        print('sub box:', i, j)
        if self.add_char(char, i, j):
            change_focus(int(j), int(i))
            return True
        else:
            return False

    def get_state(self):
        return self.state

    def check_if_won(self):
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
        ls = []
        ls.append(self.focus)
        # print(self.state)
        if self.state is not None:
            for i in self.state:
                for q in i:
                    ls.append(q)
        return ls


class user(object):
    def __init__(self, char=D, turn_state=False):
        self.char = char
        self.turn_state = turn_state

    def input(self, ls):
        """
            Accepts the point value of the clicked position. Ideally as a
            decimal ranging from 0-1
        """
        click_x = ls[0]
        click_y = ls[1]
        i = helper_func(click_x)
        j = helper_func(click_y)
        print('box clicked on:', i, ':', j)
        print('box in focus:', get_board_focus())
        if main_board[j][i].focus:
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
    if val > 2/3:
        i = 2
    elif val < 1/3:
        i = 0
    else:
        i = 1
    return i


def change_focus(row, column):
    for rw in main_board:
        for game in rw:
            game.focus = False
    main_board[column][row].focus = True
    print('focus on:', column, row)


main_board = [[tic_tac_toe(True), tic_tac_toe(False), tic_tac_toe(False)],
              [tic_tac_toe(False), tic_tac_toe(False), tic_tac_toe(False)],
              [tic_tac_toe(False), tic_tac_toe(False), tic_tac_toe(False)]]


def check_if_won(board):
    # checks if the rows have a winner
    ls = []
    for i in board:
        ts = []
        for v in i:
            ts.append(v.check_if_won)

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
    ls = []
    for row in main_board:
        ts = []
        for val in row:
            # print(val.get_to_send())
            ts.append(val.get_to_send())
        ls.append(ts)
    return ls


def get_board_focus():
    for i, row in enumerate(main_board):
        for o, column in enumerate(row):
            if column.focus == 1:
                return str(i) + ':' + str(o)
    return 'none in focus'


print(get_board_state())
print(get_board_focus())
"""test = tic_tac_toe()

print(test)
print(test.check_if_won())

# test.add_char('x', 0, 0)
test.on_click(1, 1, 'o')
test.on_click(1, 40, 'o')
test.on_click(1, 70, 'o')
print(test.check_if_won())

print(test)"""
