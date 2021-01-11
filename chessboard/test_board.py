from unittest import TestCase
from chessboard.board import *
from parameterized import parameterized


class TestChessBoard(TestCase):

    def test_initialize(self):
        board = ChessBoard()
        self.assertEquals(len([square for row in board for square in row]), 64)


    @parameterized.expand([
        ("a8", (0, 0)),
        ("h1", (7, 7)),
        ("c4", (4, 2)),
        ("d5", (3, 3)),
        ("h8", (0, 7)),
        ("e7", (1, 4)),
        ("f2", (6, 5)),
        ("g3", (5, 6)),
        ("b6", (2, 1)),
        ("a1", (7, 0))
    ])
    def test_it_sets_a_piece_given_the_algebraic_notation(self, alg_not, indexes):
        """
        8 ║♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜
        7 ║♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟
        6 ║… … … … … … … …
        5 ║… … … … … … … …
        4 ║… … … … … … … …
        3 ║… … ♘ … … … … …
        2 ║♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙
        1 ║♖ … ♗ ♕ ♔ ♗ ♘ ♖
        —╚═══════════════
        —— a b c d e f g h
        """
        board = ChessBoard()
        piece = Knight(Color.WHITE)
        board.place_piece(piece, alg_not)
        self.assertIs(board[indexes[0]][indexes[1]].piece, piece,
                      "The algebraic notation " + alg_not + " does not correspond to " + str(indexes))
