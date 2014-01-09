import piece
from random import choice


class GameOver(BaseException):
    pass


class Board(object):
    def __init__(self):
        self.rows = tuple(tuple('#' for j in xrange(10)) for j in xrange(20))
        self.current = None
        self.tick_no = 0

    def tick(self):
        try:
            act = choice((
                None,
                None,
                None,
                self.current.left,
                self.current.right,
                self.current.rotate,
            ))
            if act is not None:
                act()
        except BaseException as ex:
            print ex
        else:
            self.draw(self.current.rendered)

        if not self.tick_no % 3:
            if self.current is not None:
                try:
                    self.current.down()
                except piece.Collision:
                    self.rows = self.current.rendered
                    self.current = None
            else:
                self.current = choice(piece.TETROMINOES)(self)
                try:
                    self.current.check()
                except piece.Collision as e:
                    raise GameOver(e)

    @staticmethod
    def draw(board):
        print '\n'.join(''.join(row) for row in board)

B = Board()
from time import sleep

while True:
    B.tick()
    sleep(0.2)