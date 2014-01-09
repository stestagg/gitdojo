from abc import ABCMeta
from os import system


class Collision(BaseException):
    pass


class Piece(object):
    __metaclass__ = ABCMeta

    shape = ((0, -2), (0, -1), (0, 0), (0, 1))
    char = '#'

    def __init__(self, board):
        self.board = board
        self.position = (0, 5)
        self._rendered = False

    @property
    def rendered(self):
        if not self._rendered:
            print '\n' * 80
            d = [[self.board.rows[y][x] for x in xrange(10)]
                 for y in xrange(20)]
            y, x = self.position
            for dy, dx in self.shape:
                d[y + dy][x + dx] = self.char
            self._rendered = tuple(tuple(row) for row in d)
        return self._rendered

    def check(self, position=None):
        y, x = self.position if position is None else self.position
        for (dy, dx) in self.shape:
            try:
                if not (0 <= y + dy < 20 and 0 <= x + dx < 10):
                    raise Collision()
                if self.board.rows[y + dy][x + dx] != '#':
                    raise Collision()
            except Collision:
                raise
            except BaseException as e:
                raise Collision(e)

    def down(self):
        y, x = self.position
        y += 1
        self.check((y, x))
        self.position = (y, x)
        self._rendered = False

    def rotate(self):
        self.shape = tuple((-x, y) for (x, y) in self.shape)
        self._rendered = False

    def left(self):
        y, x = self.position
        self.check((y, x - 1))
        self.position = y, x - 1
        self._rendered = False

    def right(self):
        y, x = self.position
        self.check((y, x + 1))
        self.position = y, x + 1
        self._rendered = False


class TetraI(Piece):
    char = 'I'


class TetraT(Piece):
    char = 'T'

TETROMINOES = (TetraI, TetraI)