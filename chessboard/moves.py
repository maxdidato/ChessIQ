from typing import List
from typing import Tuple

from chessboard.pieces import *

AlgNot = Tuple[str, int]


class Move:
    def __init__(self, source: AlgNot, dest: AlgNot):
        self.source = source
        self.dest = dest

    @abstractmethod
    def move_piece(self, board) -> None:
        pass


class BasicMove(Move):

    def move_piece(self, board):
        board[self.dest].place_piece(board[self.source].piece)
        board[self.source].piece = None
        board[self.dest].piece.moves = board[self.dest].piece.moves + 1


class Castling(Move):

    def move_piece(self, board):
        if self.dest[0] == 'h':
            board[Pos(self.source).east(2)[-1]].place_piece(board[self.source].piece)
            board[self.source].piece = None
            board[Pos(self.dest).west(2)[-1]].place_piece(board[self.dest].piece)
            board[self.dest].piece = None
        else:
            board[Pos(self.source).west(2)[-1]].place_piece(board[self.source].piece)
            board[self.source].piece = None
            board[Pos(self.dest).east(3)[-1]].place_piece(board[self.dest].piece)
            board[self.dest].piece = None


class EnPassant(BasicMove):

    def __init__(self, source: AlgNot, dest: AlgNot, capture: AlgNot):
        super().__init__(source, dest)
        self.capture = capture

    def move_piece(self, board):
        super().move_piece(board)
        board[self.capture].piece = None


def en_passant(board, square):
    en_passant_moves = []
    positions = Pos(square.alg_not).east(1) + Pos(square.alg_not).west(1)
    if square.piece.color == Color.BLACK and square.alg_not[1] == 4:
        for position in positions:
            if isinstance(board[position].piece, Pawn) and board[position].piece.moves == 1 and not board[
                Pos(position).south(1)[0]].piece:
                en_passant_moves.append(EnPassant(square.alg_not, Pos(position).south(1)[0], position))
    elif square.piece.color == Color.WHITE and square.alg_not[1] == 5:
        for position in positions:
            if isinstance(board[position].piece, Pawn) and board[position].piece.moves == 1 and not board[
                Pos(position).north(1)[0]].piece:
                en_passant_moves.append(EnPassant(square.alg_not, Pos(position).north(1)[0], position))
    return en_passant_moves


def pawn_capture(board, pawn_square) -> List[Move]:
    position = Pos((pawn_square.alg_not[0], int(pawn_square.alg_not[1])))
    captures = []
    direction = "north" if pawn_square.piece.color == Color.WHITE else "south"
    potential_captures = getattr(position, direction + "_west")(1) + getattr(position, direction + "_east")(1)
    for potential_capture in potential_captures:
        if board[potential_capture].has_opponent_piece(pawn_square.piece):
            captures.append(BasicMove(pawn_square.alg_not, potential_capture))
    return captures


def castling(board, king_square) -> List[Move]:
    castling_positions = []
    rook_squares = list(
        filter(lambda x: x.piece and isinstance(x.piece, Rook) and x.piece.color == king_square.piece.color,
               list(board.values())))
    rook_squares.sort()  # so I know what is the closer rook
    if king_square.piece.moves == 0:
        if rook_squares[0].piece.moves == 0 and not any(
                filter(lambda x: board[x].piece, Pos(king_square.alg_not).west(3))):
            castling_positions.append(Castling(king_square.alg_not, rook_squares[0].alg_not))
        if rook_squares[1].piece.moves == 0 and not any(
                filter(lambda x: board[x].piece, Pos(king_square.alg_not).east(2))):
            castling_positions.append(Castling(king_square.alg_not, rook_squares[1].alg_not))
    return castling_positions
