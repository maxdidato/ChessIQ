from chessboard.pieces import *
from chessboard.color import *
import string


class Square:
    def __init__(self, color, alg_not):
        self.color = color
        self.alg_not = alg_not
        self.piece = None


class ChessBoard(list):

    def __init__(self):
        super().__init__()
        self.__initialize()
        self.__initial_pieces_setting()

    def place_piece(self, piece, position):
        square = next(filter(lambda x: x.alg_not == position, [square for row in self for square in row]),
                      None)
        square.piece = piece
        piece.position = position

    def __initial_pieces_setting(self):
        self.place_piece(Rook(Color.BLACK), 'a8')
        self.place_piece(Knight(Color.BLACK), 'b8')
        self.place_piece(Bishop(Color.BLACK), 'c8')
        self.place_piece(Queen(Color.BLACK), 'd8')
        self.place_piece(King(Color.BLACK), 'e8')
        self.place_piece(Bishop(Color.BLACK), 'f8')
        self.place_piece(Knight(Color.BLACK), 'g8')
        self.place_piece(Rook(Color.BLACK), 'h8')
        for letter in list(string.ascii_lowercase[0:8]):
            self.place_piece(Pawn(Color.BLACK), letter + '7')
        self.place_piece(Rook(Color.WHITE), 'a1')
        self.place_piece(Knight(Color.WHITE), 'b1')
        self.place_piece(Bishop(Color.WHITE), 'c1')
        self.place_piece(Queen(Color.WHITE), 'd1')
        self.place_piece(King(Color.WHITE), 'e1')
        self.place_piece(Bishop(Color.WHITE), 'f1')
        self.place_piece(Knight(Color.WHITE), 'g1')
        self.place_piece(Rook(Color.WHITE), 'h1')
        for letter in list(string.ascii_lowercase[0:8]):
            self.place_piece(Pawn(Color.WHITE), letter + '2')

    def __initialize(self):
        for i, num in enumerate(reversed(range(1, 9))):
            self.append([])
            for j, let in enumerate(list(string.ascii_lowercase[0:8])):
                algebraic_notation = str(let) + str(num)
                color = Color.LIGHT if (i + j) % 2 == 0 else Color.DARK
                self[i].append(Square(color, algebraic_notation))
