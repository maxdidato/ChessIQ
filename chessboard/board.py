import copy
import string
from typing import *

from chessboard.moves import *

AlgNot = Tuple[str, int]


class Square:
    def __init__(self, color, alg_not):
        self.color = color
        self.alg_not = alg_not
        self.piece = None

    def place_piece(self, piece: Piece) -> NoReturn:
        self.piece = piece
        piece.position = self.alg_not

    def has_opponent_piece(self, piece: Piece) -> bool:
        return self.piece and self.piece.color != piece.color

    def __lt__(self, other):
        return self.alg_not < other.alg_not


class IllegalMove(Exception):

    def __init__(self, piece, source_pos, dest_pos):
        super().__init__(
            "Piece " + piece.color.name + " " + piece.name + " cannot be moved from " + str(source_pos) + " to " + str(
                dest_pos))


class ChessBoard(dict):

    def __init__(self):
        super().__init__()
        self.__initialize()
        self.__initial_pieces_setting()

    def move_piece(self, move: Move) -> NoReturn:
        if move.dest not in [move.dest for move in self.possible_moves(self[move.source])]:
            raise IllegalMove(self[move.source].piece, self[move.source].alg_not, self[move.dest].alg_not)
        move.move_piece(self)

    def possible_moves(self, square: Square) -> List[Move]:
        possible_moves: List[Move] = []
        for dir_moves in square.piece.possible_moves():
            for position in dir_moves:
                if self[position].piece:
                    if self[position].piece.color != square.piece.color and isinstance(square.piece, Pawn):
                        possible_moves.append(BasicMove(square.alg_not, position))
                    break
                else:
                    possible_moves.append(BasicMove(square.alg_not, position))
        if isinstance(square.piece, Pawn):
            possible_moves = possible_moves + self.pawn_capture(square)
        if isinstance(square.piece, King):
            possible_moves = possible_moves + self.castling(square)
        return possible_moves

    def pawn_capture(self, pawn_square: Square) -> List[Move]:
        position = Pos((pawn_square.alg_not[0], int(pawn_square.alg_not[1])))
        captures = []
        if pawn_square.piece.color == Color.WHITE:
            potential_captures = position.north_west(1) + position.north_east(1)
        else:
            potential_captures = position.south_west(1) + position.south_east(1)
        for potential_capture in potential_captures:
            if self[potential_capture].has_opponent_piece(pawn_square.piece):
                captures.append(BasicMove(pawn_square.alg_not, potential_capture))
        return captures

    def castling(self, king_square: Square) -> List[Move]:
        castling_positions = []
        rook_squares: List[Square] = list(
            filter(lambda x: x.piece and isinstance(x.piece, Rook) and x.piece.color == king_square.piece.color,
                   list(self.values())))
        rook_squares.sort()  # so I know what is the closer rook
        if king_square.piece.moves == 0:
            if rook_squares[0].piece.moves == 0 and not any(
                    filter(lambda x: self[x].piece, Pos(king_square.alg_not).west(3))):
                castling_positions.append(Castling(king_square.alg_not, rook_squares[0].alg_not))
            if rook_squares[1].piece.moves == 0 and not any(
                    filter(lambda x: self[x].piece, Pos(king_square.alg_not).east(2))):
                castling_positions.append(Castling(king_square.alg_not, rook_squares[1].alg_not))
        return castling_positions

    def is_move_leaving_king_in_check(self, move: Move) -> bool:
        possible_board = copy.deepcopy(self)
        possible_board.move_piece(move)
        if possible_board.is_king_in_check(self[move.source].piece.color):
            return True
        else:
            return False

    def get_opponent_squares(self, color: Color) -> List[Square]:
        return list(filter(lambda x: x.piece and x.piece.color != color, list(self.values())))

    def is_king_in_check(self, color: Color) -> bool:
        king_square = next(
            filter(lambda x: x.piece and isinstance(x.piece, King) and x.piece.color == color, list(self.values())))
        for opponent_square in self.get_opponent_squares(color):
            if king_square.alg_not in [move.dest for move in self.possible_moves(opponent_square)]:
                return True

    def __initial_pieces_setting(self) -> NoReturn:
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

    def __initialize(self) -> NoReturn:
        for i, num in enumerate(reversed(range(1, 9))):
            for j, let in enumerate(list(string.ascii_lowercase[0:8])):
                color = Color.LIGHT if (i + j) % 2 == 0 else Color.DARK
                self[(let, num)] = Square(color, (let, num))
