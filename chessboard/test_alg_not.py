from unittest import TestCase
from chessboard.pieces import AlgNot
from parameterized import parameterized


class TestChessBoard(TestCase):

    @parameterized.expand([
        (('a', 1), 1, ['a2']),
        (('a', 5), 1, ['a6']),
        (('d', 2), 3, ['d3', 'd4', 'd5']),
        (('e', 6), 1, ['e7']),
        (('h', 3), 6, ['h4', 'h5', 'h6', 'h7', 'h8']),
        (('b', 4), 1, ['b5']),
        (('b', 7), 1, ['b8']),
        (('a', 8), 1, []),
        (('c', 8), 4, []),
        (('e', 8), 8, []),
        (('a', 1), 2, ['a2', 'a3']),
        (('a', 8), 8, []),
        (('a', 4), 3, ['a5', 'a6', 'a7']),
        (('a', 4), 8, ['a5', 'a6', 'a7', 'a8']),
        (('h', 1), 8, ['h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8']),
    ])
    def test_num_of_positions_north_from_current(self, start_pos, num_of_steps, expected):
        alg_not = AlgNot(start_pos[0], start_pos[1])
        positions = alg_not.north(num_of_steps)
        self.assertEqual(expected, positions)

    @parameterized.expand([
        (('a', 1), 1, []),
        (('a', 5), 1, ['a4']),
        (('d', 2), 3, ['d1']),
        (('e', 6), 1, ['e5']),
        (('h', 3), 6, ['h2', 'h1']),
        (('b', 4), 1, ['b3']),
        (('b', 7), 1, ['b6']),
        (('a', 8), 1, ['a7']),
        (('c', 8), 4, ['c7', 'c6', 'c5', 'c4']),
        (('e', 8), 8, ['e7', 'e6', 'e5', 'e4', 'e3', 'e2', 'e1']),
        (('a', 1), 2, []),
        (('a', 2), 8, ['a1']),
        (('a', 4), 3, ['a3', 'a2', 'a1']),
        (('a', 4), 8, ['a3', 'a2', 'a1']),
        (('h', 1), 8, []),
    ])
    def test_num_of_positions_south_from_current(self, start_pos, num_of_steps, expected):
        alg_not = AlgNot(start_pos[0], start_pos[1])
        positions = alg_not.south(num_of_steps)
        self.assertEqual(expected, positions)

    @parameterized.expand([
        (('a', 1), 1, ['b1']),
        (('a', 5), 1, ['b5']),
        (('d', 2), 3, ['e2', 'f2', 'g2']),
        (('e', 6), 1, ['f6']),
        (('h', 3), 6, []),
        (('b', 4), 1, ['c4']),
        (('b', 7), 1, ['c7']),
        (('a', 8), 1, ['b8']),
        (('c', 8), 4, ['d8', 'e8', 'f8', 'g8']),
        (('e', 8), 8, ['f8', 'g8', 'h8']),
        (('a', 1), 2, ['b1', 'c1']),
        (('a', 2), 8, ['b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2']),
        (('g', 4), 3, ['h4']),
        (('d', 4), 8, ['e4', 'f4', 'g4', 'h4']),
        (('h', 1), 8, []),
    ])
    def test_num_of_positions_east_from_current(self, start_pos, num_of_steps, expected):
        alg_not = AlgNot(start_pos[0], start_pos[1])
        positions = alg_not.east(num_of_steps)
        self.assertEqual(expected, positions)

    @parameterized.expand([
        (('a', 1), 1, []),
        (('a', 5), 1, []),
        (('d', 2), 3, ['c2', 'b2', 'a2']),
        (('e', 6), 1, ['d6']),
        (('h', 3), 6, ['g3', 'f3', 'e3', 'd3', 'c3', 'b3']),
        (('b', 4), 1, ['a4']),
        (('b', 7), 1, ['a7']),
        (('a', 8), 1, []),
        (('c', 8), 4, ['b8', 'a8']),
        (('e', 8), 8, ['d8', 'c8', 'b8', 'a8']),
        (('a', 1), 2, []),
        (('a', 2), 8, []),
        (('g', 4), 3, ['f4', 'e4', 'd4']),
        (('d', 4), 8, ['c4', 'b4', 'a4']),
        # (('h', 1), 8, ['g1', 'f1', 'e1', 'd1', 'c1', 'b1', 'a1']),
    ])
    def test_num_of_positions_west_from_current(self, start_pos, num_of_steps, expected):
        alg_not = AlgNot(start_pos[0], start_pos[1])
        positions = alg_not.west(num_of_steps)
        self.assertEqual(expected, positions)
