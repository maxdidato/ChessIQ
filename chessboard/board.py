from chessboard.pieces import *
from chessboard.color import *
import string


class Square:
    def __init__(self, color, alg_not):
        self.color = color
        self.alg_not = alg_not
        self.piece = None

    def move_piece(self, dest_square):
        dest_square.piece = self.piece
        dest_square.piece.position = dest_square.alg_not
        self.piece = None

    def place_piece(self, piece):
        self.piece = piece
        piece.position = self.alg_not


class ChessBoard(dict):

    def __init__(self):
        super().__init__()
        self.__initialize()
        self.__initial_pieces_setting()

    def possible_moves(self, square):
        possible_moves = []
        for dir_moves in square.piece.possible_moves():
            for position in dir_moves:
                possible_moves.append(position)
                if self[position].piece:
                    if self[position].piece.color == square.piece.color:
                        possible_moves.remove(position)
                    break
        return possible_moves

    def __initial_pieces_setting(self):
        self[('a', 8)].place_piece(Rook(Color.BLACK))
        self[('b', 8)].place_piece(Knight(Color.BLACK))
        self[('c', 8)].place_piece(Bishop(Color.BLACK))
        self[('d', 8)].place_piece(Queen(Color.BLACK))
        self[('e', 8)].place_piece(King(Color.BLACK))
        self[('f', 8)].place_piece(Bishop(Color.BLACK))
        self[('g', 8)].place_piece(Knight(Color.BLACK))
        self[('h', 8)].place_piece(Rook(Color.BLACK))
        for letter in list(string.ascii_lowercase[0:8]):
            self[(letter, 7)].place_piece(Pawn(Color.BLACK))
        self[('a', 1)].place_piece(Rook(Color.WHITE))
        self[('b', 1)].place_piece(Knight(Color.WHITE))
        self[('c', 1)].place_piece(Bishop(Color.WHITE))
        self[('d', 1)].place_piece(Queen(Color.WHITE))
        self[('e', 1)].place_piece(King(Color.WHITE))
        self[('f', 1)].place_piece(Bishop(Color.WHITE))
        self[('g', 1)].place_piece(Knight(Color.WHITE))
        self[('h', 1)].place_piece(Rook(Color.WHITE))
        for letter in list(string.ascii_lowercase[0:8]):
            self[(letter, 2)].place_piece(Pawn(Color.WHITE))

    def __initialize(self):
        for i, num in enumerate(reversed(range(1, 9))):
            for j, let in enumerate(list(string.ascii_lowercase[0:8])):
                color = Color.LIGHT if (i + j) % 2 == 0 else Color.DARK
                self[(let, num)] = Square(color, (let, num))
