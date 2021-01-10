from chessboard.pieces import *
from chessboard.color import *


class Square:
    def __init__(self, color, piece=None):
        self.color = color
        self.piece = piece


class ChessBoard(list):

    def initialize(self):
        self.__draw_board()
        self.__initial_pieces_setting()

    @staticmethod
    def __parse_algebraic_notation(notation):
        letter = notation[:1]
        number = int(notation[-1])
        return abs(8 - number), ord(letter) - 97

    def __place_piece(self, piece, position):
        indexes = self.__parse_algebraic_notation(position)
        self[indexes[0]][indexes[1]].piece = piece

    def __initial_pieces_setting(self):
        self.__place_piece(Rook(Color.BLACK), 'a8')
        self.__place_piece(Knight(Color.BLACK), 'b8')
        self.__place_piece(Bishop(Color.BLACK), 'c8')
        self.__place_piece(Queen(Color.BLACK), 'd8')
        self.__place_piece(King(Color.BLACK), 'e8')
        self.__place_piece(Bishop(Color.BLACK), 'f8')
        self.__place_piece(Knight(Color.BLACK), 'g8')
        self.__place_piece(Rook(Color.BLACK), 'h8')
        self.__place_piece(Pawn(Color.BLACK), 'a7')
        self.__place_piece(Pawn(Color.BLACK), 'b7')
        self.__place_piece(Pawn(Color.BLACK), 'c7')
        self.__place_piece(Pawn(Color.BLACK), 'd7')
        self.__place_piece(Pawn(Color.BLACK), 'e7')
        self.__place_piece(Pawn(Color.BLACK), 'f7')
        self.__place_piece(Pawn(Color.BLACK), 'g7')
        self.__place_piece(Pawn(Color.BLACK), 'h7')
        self.__place_piece(Rook(Color.WHITE), 'a1')
        self.__place_piece(Knight(Color.WHITE), 'b1')
        self.__place_piece(Bishop(Color.WHITE), 'c1')
        self.__place_piece(Queen(Color.WHITE), 'd1')
        self.__place_piece(King(Color.WHITE), 'e1')
        self.__place_piece(Bishop(Color.WHITE), 'f1')
        self.__place_piece(Knight(Color.WHITE), 'g1')
        self.__place_piece(Rook(Color.WHITE), 'h1')
        self.__place_piece(Pawn(Color.WHITE), 'a2')
        self.__place_piece(Pawn(Color.WHITE), 'b2')
        self.__place_piece(Pawn(Color.WHITE), 'c2')
        self.__place_piece(Pawn(Color.WHITE), 'd2')
        self.__place_piece(Pawn(Color.WHITE), 'e2')
        self.__place_piece(Pawn(Color.WHITE), 'f2')
        self.__place_piece(Pawn(Color.WHITE), 'g2')
        self.__place_piece(Pawn(Color.WHITE), 'h2')

    def __draw_board(self):
        for i in range(8):
            self.append([])
            for j in range(8):
                self[i].append(Square(Color.from_index(j + i)))
