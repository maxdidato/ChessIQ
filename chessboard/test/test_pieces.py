from unittest import TestCase
from chessboard.pieces import *


class TestPieces(TestCase):

    def test_knight_moves(self):
        knight = Knight(Color.WHITE)
        knight.position = ('d', 5)
        self.assertEqual(knight.possible_moves(),
                         [[('e', 7)], [('f', 6)], [('c', 7)], [('b', 6)], [('e', 3)], [('f', 4)], [('c', 3)],
                          [('b', 4)]])

    def test_knight_moves_when_not_all_available(self):
        knight = Knight(Color.BLACK)
        knight.position = ('a', 1)
        self.assertEqual(knight.possible_moves(), [[('b', 3)], [('c', 2)]])

    def test_king_moves(self):
        king = King(Color.WHITE)
        king.position = ('d', 5)
        self.assertEqual(king.possible_moves(),
                         [[('d', 6)], [('d', 4)], [('e', 5)], [('c', 5)], [('e', 6)], [('c', 6)], [('e', 4)],
                          [('c', 4)]])

    def test_king_moves_when_not_all_available(self):
        king = King(Color.BLACK)
        king.position = ('a', 1)
        self.assertEqual(king.possible_moves(), [[('a', 2)], [], [('b', 1)], [], [('b', 2)], [], [], []])

    def test_queen_moves(self):
        queen = King(Color.WHITE)
        queen.position = ('d', 5)
        self.assertEqual(queen.possible_moves(),
                         [[('d', 6)], [('d', 4)], [('e', 5)], [('c', 5)], [('e', 6)], [('c', 6)], [('e', 4)],
                          [('c', 4)]])

    def test_queen_moves_when_not_all_available(self):
        queen = King(Color.BLACK)
        queen.position = ('h', 1)
        self.assertEqual(queen.possible_moves(), [[('h', 2)], [], [], [('g', 1)], [], [('g', 2)], [], []])

    def test_rook_moves(self):
        rook = Rook(Color.WHITE)
        rook.position = ('d', 5)
        self.assertEqual(rook.possible_moves(),
                         [[('d', 6), ('d', 7), ('d', 8)], [('d', 4), ('d', 3), ('d', 2), ('d', 1)],
                          [('e', 5), ('f', 5), ('g', 5), ('h', 5)], [('c', 5), ('b', 5), ('a', 5)]]
                         )

    def test_rook_moves_when_not_all_available(self):
        rook = Rook(Color.BLACK)
        rook.position = ('h', 1)
        self.assertEqual(rook.possible_moves(),
                         [[('h', 2), ('h', 3), ('h', 4), ('h', 5), ('h', 6), ('h', 7), ('h', 8)], [], [],
                          [('g', 1), ('f', 1), ('e', 1), ('d', 1), ('c', 1), ('b', 1), ('a', 1)]])

    def test_pawn_moves(self):
        pawn = Pawn(Color.WHITE)
        pawn.position = ('d', 5)
        self.assertEqual(pawn.possible_moves(),
                         [[('d', 6)]]
                         )

    def test_black_pawn_initial_moves(self):
        pawn = Pawn(Color.BLACK)
        pawn.position = ('d', 7)
        self.assertEqual(pawn.possible_moves(), [[('d', 6), ('d', 5)]])

    def test_white_pawn_initial_moves(self):
        pawn = Pawn(Color.WHITE)
        pawn.position = ('d', 2)
        self.assertEqual(pawn.possible_moves(), [[('d', 3), ('d', 4)]])

    def test_pawn_moves_when_not_all_available(self):
        pawn = Pawn(Color.BLACK)
        pawn.position = ('a', 1)
        self.assertEqual(pawn.possible_moves(), [[]])

    def test_bishop_moves(self):
        bishop = Bishop(Color.WHITE)
        bishop.position = ('d', 5)
        self.assertEqual(bishop.possible_moves(),
                         [[('e', 6), ('f', 7), ('g', 8)], [('c', 6), ('b', 7), ('a', 8)],
                          [('e', 4), ('f', 3), ('g', 2), ('h', 1)], [('c', 4), ('b', 3), ('a', 2)]]
                         )

    def test_bishop_moves_when_not_all_available(self):
        bishop = Bishop(Color.BLACK)
        bishop.position = ('h', 8)
        self.assertEqual(bishop.possible_moves(),
                         [[], [], [], [('g', 7), ('f', 6), ('e', 5), ('d', 4), ('c', 3), ('b', 2), ('a', 1)]])
