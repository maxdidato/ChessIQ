from typing import Tuple

from chessboard.pieces import *

AlgNot = Tuple[str, int]


class Move:
    def __init__(self, source: AlgNot, dest: AlgNot):
        self.source = source
        self.dest = dest

    @abstractmethod
    def move_piece(self, board):
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
