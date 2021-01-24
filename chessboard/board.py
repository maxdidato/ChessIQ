from chessboard.pieces import *
from chessboard.color import *
import string


class Square:
    def __init__(self, color, alg_not):
        self.color = color
        self.alg_not = alg_not
        self.piece = None


class ChessBoard(dict):

    def __init__(self):
        super().__init__()
        self.__initialize()
        self.__initial_pieces_setting()

    def place_piece(self, piece, position):
        self[position].piece = piece
        piece.position = position

    def move_piece(self, source_pos, dest_pos):
        self[dest_pos].piece = self[source_pos].piece
        self[dest_pos].piece.position = dest_pos
        self[source_pos].piece = None

    def possible_moves(self, square):
        possible_moves = []
        for positions in square.piece.possible_moves().get_directional_moves():
            for position in positions:
                candidate_square = self[position]
                if candidate_square.piece:
                    if candidate_square.piece.color != square.piece.color:
                        possible_moves.append(position)
                    break
                else:
                    possible_moves.append(position)
        for position in square.piece.possible_moves().get_non_directional_moves():
            candidate_square = self[position]
            if not candidate_square.piece or candidate_square.piece.color != square.piece.color:
                possible_moves.append(position)
        return possible_moves

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
            for j, let in enumerate(list(string.ascii_lowercase[0:8])):
                algebraic_notation = str(let) + str(num)
                color = Color.LIGHT if (i + j) % 2 == 0 else Color.DARK
                self[algebraic_notation] = Square(color, algebraic_notation)
