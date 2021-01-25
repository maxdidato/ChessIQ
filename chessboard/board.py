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
        for positions in square.piece.possible_moves().get_directional_moves():
            for position in [str(i[0]) + str(i[1]) for i in positions]:
                candidate_square = self[position]
                if candidate_square.piece:
                    if candidate_square.piece.color != square.piece.color:
                        possible_moves.append(position)
                    break
                else:
                    possible_moves.append(position)
        for position in [str(i[0]) + str(i[1]) for i in square.piece.possible_moves().get_non_directional_moves()]:
            candidate_square = self[position]
            if not candidate_square.piece or candidate_square.piece.color != square.piece.color:
                possible_moves.append(position)
        return possible_moves

    def __initial_pieces_setting(self):
        self['a8'].place_piece(Rook(Color.BLACK))
        self['b8'].place_piece(Knight(Color.BLACK))
        self['c8'].place_piece(Bishop(Color.BLACK))
        self['d8'].place_piece(Queen(Color.BLACK))
        self['e8'].place_piece(King(Color.BLACK))
        self['f8'].place_piece(Bishop(Color.BLACK))
        self['g8'].place_piece(Knight(Color.BLACK))
        self['h8'].place_piece(Rook(Color.BLACK))
        for letter in list(string.ascii_lowercase[0:8]):
            self[letter + '7'].place_piece(Pawn(Color.BLACK))
        self['a1'].place_piece(Rook(Color.WHITE))
        self['b1'].place_piece(Knight(Color.WHITE))
        self['c1'].place_piece(Bishop(Color.WHITE))
        self['d1'].place_piece(Queen(Color.WHITE))
        self['e1'].place_piece(King(Color.WHITE))
        self['f1'].place_piece(Bishop(Color.WHITE))
        self['g1'].place_piece(Knight(Color.WHITE))
        self['h1'].place_piece(Rook(Color.WHITE))
        for letter in list(string.ascii_lowercase[0:8]):
            self[letter + '2'].place_piece(Pawn(Color.WHITE))

    def __initialize(self):
        for i, num in enumerate(reversed(range(1, 9))):
            for j, let in enumerate(list(string.ascii_lowercase[0:8])):
                algebraic_notation = str(let) + str(num)
                color = Color.LIGHT if (i + j) % 2 == 0 else Color.DARK
                self[algebraic_notation] = Square(color, algebraic_notation)
