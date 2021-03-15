from unittest import TestCase

from chessboard.board import *


class TestChessBoard(TestCase):

    def test_move_piece_from_location_to_another(self):
        """
      0  8 ║♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜
      1  7 ║♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟
      2  6 ║… … … … … … … …
      3  5 ║… … … … … … … …
      4  4 ║… … … … … … … …   c4 = 4,2
      5  3 ║… … … … … … … …
      6  2 ║♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙
      7  1 ║♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖
        —╚═══════════════
        —— a b c d e f g h
        ___0 1 2 3 4 5 6 7
        """
        board = ChessBoard()
        source_pos = ('a', 2)
        dest_pos = ('a', 3)
        source_piece = board[source_pos].piece
        board.move_piece(source_pos, dest_pos)
        self.assertEqual(board[source_pos].piece, None)
        self.assertEqual(board[dest_pos].piece, source_piece)

    def test_illegal_move(self):
        board = ChessBoard()
        source_pos = ('a', 2)
        dest_pos = ('a', 1)
        with self.assertRaises(IllegalMove):
            board.move_piece(source_pos, dest_pos)

    def test_get_possible_moves_for_square(self):
        board = ChessBoard()
        # clear board
        for square in board.values():
            square.piece = None

        board[('a', 1)].place_piece(Rook(Color.WHITE))
        possible_moves = board.possible_moves(board[('a', 1)])
        self.assertEqual(possible_moves, [('a', 2), ('a', 3), ('a', 4), ('a', 5), ('a', 6), ('a', 7), ('a', 8),
                                          ('b', 1), ('c', 1), ('d', 1), ('e', 1), ('f', 1), ('g', 1), ('h', 1)])

    def test_possible_moves_when_same_color_piece_on_trajectory(self):
        board = ChessBoard()
        # clear board
        for square in board.values():
            square.piece = None

        board[('a', 1)].place_piece(Rook(Color.WHITE))
        board[('a', 3)].place_piece(Pawn(Color.WHITE))
        possible_moves = board.possible_moves(board[('a', 1)])
        self.assertEqual(possible_moves, [('a', 2),
                                          ('b', 1), ('c', 1), ('d', 1), ('e', 1), ('f', 1), ('g', 1), ('h', 1)])

    def test_possible_moves_when_other_color_piece_on_trajectory(self):
        board = ChessBoard()
        # clear board
        for square in board.values():
            square.piece = None

        board[('a', 1)].place_piece(Rook(Color.WHITE))
        board[('a', 3)].place_piece(Pawn(Color.BLACK))
        possible_moves = board.possible_moves(board[('a', 1)])
        self.assertEqual(possible_moves, [('a', 2), ('a', 3),
                                          ('b', 1), ('c', 1), ('d', 1), ('e', 1), ('f', 1), ('g', 1), ('h', 1)])

    def test_possible_moves_for_non_directional_pieces_knight(self):
        board = ChessBoard()
        # clear board
        for square in board.values():
            square.piece = None

        board[('a', 1)].place_piece(Knight(Color.WHITE))
        board[('a', 2)].place_piece(Pawn(Color.WHITE))
        board[('b', 2)].place_piece(Pawn(Color.WHITE))
        board[('b', 1)].place_piece(Pawn(Color.WHITE))
        possible_moves = board.possible_moves(board[('a', 1)])
        self.assertEqual(possible_moves, [('b', 3), ('c', 2)])

    def test_king_in_check_when_opponent_piece_can_attach_the_king(self):
        board = ChessBoard()

        # clear board
        for square in board.values():
            square.piece = None

        board[('c', 8)].place_piece(King(Color.BLACK))
        board[('c', 1)].place_piece(Queen(Color.WHITE))
        board[('b', 2)].place_piece(King(Color.WHITE))

        self.assertTrue(board.is_king_in_check(Color.BLACK))
        self.assertFalse(board.is_king_in_check(Color.WHITE))

    def test_king_in_check_and_then_covered(self):
        board = ChessBoard()

        # clear board
        for square in board.values():
            square.piece = None

        board[('c', 8)].place_piece(King(Color.BLACK))
        board[('c', 1)].place_piece(Queen(Color.WHITE))
        board[('b', 2)].place_piece(King(Color.WHITE))
        self.assertTrue(board.is_king_in_check(Color.BLACK))
        board[('c', 2)].place_piece(Pawn(Color.WHITE))

        self.assertFalse(board.is_king_in_check(Color.BLACK))

    def test_if_move_doesnt_leave_king_in_check(self):
        board = ChessBoard()

        # clear board
        for square in board.values():
            square.piece = None

        board[('c', 8)].place_piece(King(Color.BLACK))
        board[('c', 7)].place_piece(Bishop(Color.BLACK))
        board[('c', 1)].place_piece(Queen(Color.WHITE))
        self.assertFalse(board.is_king_in_check(Color.BLACK))

        self.assertTrue(board.is_move_leaving_king_in_check(('c', 7), ('e', 5)))

    def test_if_move_leaves_king_in_check(self):
        board = ChessBoard()

        # clear board
        for square in board.values():
            square.piece = None

        board[('c', 8)].place_piece(King(Color.BLACK))
        board[('c', 7)].place_piece(Pawn(Color.BLACK))
        board[('c', 1)].place_piece(Queen(Color.WHITE))
        self.assertFalse(board.is_king_in_check(Color.BLACK))

        self.assertFalse(board.is_move_leaving_king_in_check(('c', 7), ('c', 6)))
