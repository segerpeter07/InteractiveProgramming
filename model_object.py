import time
import ast
max_ACC = 1
acc_standard = .9


class model(object):
    def __init__(self):
        self.state = 1
        self.x = 0
        self.y = 0
        self.socket_list = []
        self.users = []
        self.correlation = {}

    def save_val(self, thruput, member):
        # print(thruput)
        to_use = self.correlation[member]
        try:
            ls = ast.literal_eval(thruput)
            to_use.input(ls)
        except (SyntaxError, ValueError) as e:
            pass

    def update_socket_list(self, thruput):
        if thruput not in self.socket_list:
            self.socket_list.append(thruput)
            if len(self.socket_list) == 1:
                self.users.append(ship([1, 1, .5, .5, .25, .25, 0, -1]))
                self.correlation[thruput] = self.users[0]

            elif len(self.socket_list) == 2:
                self.users.append(gunner([0, 0, 0, 0, 0, 0, 0, 0]))
                self.correlation[thruput] = self.users[1]

            else:
                print('Invalid number of connections: 2 players expected.')
                print('Ignoring Extra Connection')

    def update_physics(self):
        # print(time.time())
        for i in self.users:
            i.update_physics()
        # print('updated')
        # print(self.users)
        # print(self.correlation)
        to_return = []
        for user in self.users:
            to_return.append(user.get_status_vector())
        print(to_return)
        return to_return


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


class base_class(object):
    """
    Base Class to make life easier for everyone involved
    creates base methods accessible to all objects that inherit it, i.e. ship
        and gunner.
    """
    def __init__(self, vector=[0, 0, 0, 0, 0, 0, 0, 0]):
        # [x,y] [dx,dy] [ddx,ddy] [theta,dtheta]
        self.loc = Point(vector[0], vector[1])
        self.vel = Point(vector[2], vector[3])
        self.acc = Point(vector[4], vector[5])
        self.rot = Point(vector[6], vector[7])
        self.last_time = time.time()

    def update_physics(self):
        current = time.time()
        diff = current - self.last_time
        self.last_time = current

        # calculates change in POSITION by eulers method
        delta_vel = self.acc.multiply_by(diff)
        self.vel = self.vel.add(delta_vel)
        delta_pos = self.vel.multiply_by(diff)
        self.loc = self.loc.add(delta_pos)

        if self.acc.x is not 0:
            cx = -1 * (abs(self.acc.x)/self.acc.x)
        else:
            cx = -1
        if self.acc.y is not 0:
            cy = -1 * (abs(self.acc.y)/self.acc.y)
        else:
            cy = -1

        self.acc = self.acc.add(Point(cx * diff * acc_standard,
                                      cy * diff * acc_standard))
        if abs(self.acc.x) < .005:
            self.acc.x = 0
        if abs(self.acc.y) < .005:
            self.acc.y = 0

        # calculates change in ROTATION by eulers method
        delta_theta = self.rot.y * diff
        self.rot.x += delta_theta
        # self.rot.y = self.rot.y / 2  # trailing rotational motion
        # print(self.loc, self.vel, self.acc, self.rot)
        # print(self.loc)


class gunner(base_class):
    """
        gunner class has little to no physics run on it, as it is always
        positioned in the middle of the ship. The only possible physics is
        in the rotation of the turret, encapsulated by the self.acc point.
    """
    def __str__(self):
        return "I'm a gunner"

    def input(self, ls):
        print('gunner')
        # controls: left, right, up, down, space
        # equivalent:0, 1, 2, 3, 4
        for val in ls:
            if val == 0:
                self.acc.x = -max_ACC
            elif val == 1:
                self.acc.x = -max_ACC
            elif val == 4:
                print('bang bang')

    def get_status_vector(self):
        return ['g', self.rot.x]


class ship(base_class):
    def __str__(self):
        return "I'm a ship"

    def input(self, ls):
        # controls: left, right, up, down, space
        # equivalent:0, 1, 2, 3, 4
        for val in ls:
            if val == 0:
                self.acc.x = -max_ACC
            elif val == 1:
                self.acc.x = max_ACC
            elif val == 2:
                self.acc.y = -max_ACC
            elif val == 3:
                self.acc.y = max_ACC
            elif val == 4:
                print('bang bang')

    def get_status_vector(self):
        return ['s', self.loc.x, self.loc.y]
