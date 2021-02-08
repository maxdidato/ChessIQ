from unittest import TestCase
from chessboard.pieces import Pos
from parameterized import parameterized


class TestPos(TestCase):

    @parameterized.expand([
        (('a', 1), 1, [('a', 2)]),
        (('a', 5), 1, [('a', 6)]),
        (('d', 2), 3, [('d', 3), ('d', 4), ('d', 5)]),
        (('e', 6), 1, [('e', 7)]),
        (('h', 3), 6, [('h', 4), ('h', 5), ('h', 6), ('h', 7), ('h', 8)]),
        (('b', 4), 1, [('b', 5)]),
        (('b', 7), 1, [('b', 8)]),
        (('a', 8), 1, []),
        (('c', 8), 4, []),
        (('e', 8), 8, []),
        (('a', 1), 2, [('a', 2), ('a', 3)]),
        (('a', 8), 8, []),
        (('a', 4), 3, [('a', 5), ('a', 6), ('a', 7)]),
        (('a', 4), 8, [('a', 5), ('a', 6), ('a', 7), ('a', 8)]),
        (('h', 1), 8, [('h', 2), ('h', 3), ('h', 4), ('h', 5), ('h', 6), ('h', 7), ('h', 8)]),
    ])
    def test_num_of_positions_north_from_current(self, start_pos, num_of_steps, expected):
        alg_not = Pos(start_pos)
        positions = alg_not.north(num_of_steps)
        self.assertEqual(expected, positions)

    @parameterized.expand([
        (('a', 1), 1, []),
        (('a', 5), 1, [('a', 4)]),
        (('d', 2), 3, [('d', 1)]),
        (('e', 6), 1, [('e', 5)]),
        (('h', 3), 6, [('h', 2), ('h', 1)]),
        (('b', 4), 1, [('b', 3)]),
        (('b', 7), 1, [('b', 6)]),
        (('a', 8), 1, [('a', 7)]),
        (('c', 8), 4, [('c', 7), ('c', 6), ('c', 5), ('c', 4)]),
        (('e', 8), 8, [('e', 7), ('e', 6), ('e', 5), ('e', 4), ('e', 3), ('e', 2), ('e', 1)]),
        (('a', 1), 2, []),
        (('a', 2), 8, [('a', 1)]),
        (('a', 4), 3, [('a', 3), ('a', 2), ('a', 1)]),
        (('a', 4), 8, [('a', 3), ('a', 2), ('a', 1)]),
        (('h', 1), 8, []),
    ])
    def test_num_of_positions_south_from_current(self, start_pos, num_of_steps, expected):
        alg_not = Pos(start_pos)
        positions = alg_not.south(num_of_steps)
        self.assertEqual(expected, positions)

    @parameterized.expand([
        (('a', 1), 1, [('b', 1)]),
        (('a', 5), 1, [('b', 5)]),
        (('d', 2), 3, [('e', 2), ('f', 2), ('g', 2)]),
        (('e', 6), 1, [('f', 6)]),
        (('h', 3), 6, []),
        (('b', 4), 1, [('c', 4)]),
        (('b', 7), 1, [('c', 7)]),
        (('a', 8), 1, [('b', 8)]),
        (('c', 8), 4, [('d', 8), ('e', 8), ('f', 8), ('g', 8)]),
        (('e', 8), 8, [('f', 8), ('g', 8), ('h', 8)]),
        (('a', 1), 2, [('b', 1), ('c', 1)]),
        (('a', 2), 8, [('b', 2), ('c', 2), ('d', 2), ('e', 2), ('f', 2), ('g', 2), ('h', 2)]),
        (('g', 4), 3, [('h', 4)]),
        (('d', 4), 8, [('e', 4), ('f', 4), ('g', 4), ('h', 4)]),
        (('h', 1), 8, []),
    ])
    def test_num_of_positions_east_from_current(self, start_pos, num_of_steps, expected):
        alg_not = Pos(start_pos)
        positions = alg_not.east(num_of_steps)
        self.assertEqual(expected, positions)

    @parameterized.expand([
        (('a', 1), 1, []),
        (('a', 5), 1, []),
        (('d', 2), 3, [('c', 2), ('b', 2), ('a', 2)]),
        (('e', 6), 1, [('d', 6)]),
        (('h', 3), 6, [('g', 3), ('f', 3), ('e', 3), ('d', 3), ('c', 3), ('b', 3)]),
        (('b', 4), 1, [('a', 4)]),
        (('b', 7), 1, [('a', 7)]),
        (('a', 8), 1, []),
        (('c', 8), 4, [('b', 8), ('a', 8)]),
        (('e', 8), 8, [('d', 8), ('c', 8), ('b', 8), ('a', 8)]),
        (('a', 1), 2, []),
        (('a', 2), 8, []),
        (('g', 4), 3, [('f', 4), ('e', 4), ('d', 4)]),
        (('d', 4), 8, [('c', 4), ('b', 4), ('a', 4)]),
        (('h', 1), 8, [('g', 1), ('f', 1), ('e', 1), ('d', 1), ('c', 1), ('b', 1), ('a', 1)]),
    ])
    def test_num_of_positions_west_from_current(self, start_pos, num_of_steps, expected):
        alg_not = Pos(start_pos)
        positions = alg_not.west(num_of_steps)
        self.assertEqual(expected, positions)

    @parameterized.expand([
        (('a', 1), 8, [('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6), ('g', 7), ('h', 8)]),
        (('a', 5), 1, [('b', 6)]),
        (('d', 2), 3, [('e', 3), ('f', 4), ('g', 5)]),
        (('e', 6), 1, [('f', 7)]),
        (('h', 3), 6, []),
        (('b', 4), 1, [('c', 5)]),
        (('b', 7), 1, [('c', 8)]),
        (('a', 8), 1, []),
        (('c', 8), 4, []),
        (('e', 8), 8, []),
        (('a', 1), 2, [('b', 2), ('c', 3)]),
        (('a', 2), 8, [('b', 3), ('c', 4), ('d', 5), ('e', 6), ('f', 7), ('g', 8)]),
        (('g', 4), 3, [('h', 5)]),
        (('d', 4), 8, [('e', 5), ('f', 6), ('g', 7), ('h', 8)]),
        (('h', 1), 8, []),
    ])
    def test_num_of_positions_north_east_from_current(self, start_pos, num_of_steps, expected):
        alg_not = Pos(start_pos)
        positions = alg_not.north_east(num_of_steps)
        self.assertEqual(expected, positions)

    @parameterized.expand([
        (('a', 1), 8, []),
        (('a', 5), 1, []),
        (('d', 2), 3, [('c', 1)]),
        (('e', 6), 4, [('d', 5), ('c', 4), ('b', 3), ('a', 2)]),
        (('h', 3), 6, [('g', 2), ('f', 1)]),
        (('b', 4), 1, [('a', 3)]),
        (('b', 7), 1, [('a', 6)]),
        (('a', 8), 1, []),
        (('c', 8), 4, [('b', 7), ('a', 6)]),
        (('e', 8), 8, [('d', 7), ('c', 6), ('b', 5), ('a', 4)]),
        (('a', 1), 2, []),
        (('a', 2), 8, []),
        (('g', 4), 3, [('f', 3), ('e', 2), ('d', 1)]),
        (('d', 4), 8, [('c', 3), ('b', 2), ('a', 1)]),
        (('h', 8), 8, [('g', 7), ('f', 6), ('e', 5), ('d', 4), ('c', 3), ('b', 2), ('a', 1)]),
    ])
    def test_num_of_positions_south_west_from_current(self, start_pos, num_of_steps, expected):
        alg_not = Pos(start_pos)
        positions = alg_not.south_west(num_of_steps)
        self.assertEqual(expected, positions)

    @parameterized.expand([
        (('a', 1), 8, []),
        (('a', 5), 1, [('b', 4)]),
        (('d', 2), 3, [('e', 1)]),
        (('e', 6), 4, [('f', 5), ('g', 4), ('h', 3)]),
        (('h', 3), 6, []),
        (('b', 4), 1, [('c', 3)]),
        (('b', 7), 1, [('c', 6)]),
        (('a', 8), 8, [('b', 7), ('c', 6), ('d', 5), ('e', 4), ('f', 3), ('g', 2), ('h', 1)]),
        (('c', 8), 4, [('d', 7), ('e', 6), ('f', 5), ('g', 4)]),
        (('e', 8), 8, [('f', 7), ('g', 6), ('h', 5)]),
        (('a', 1), 2, []),
        (('a', 2), 8, [('b', 1)]),
        (('g', 4), 3, [('h', 3)]),
        (('d', 4), 8, [('e', 3), ('f', 2), ('g', 1)]),
        (('h', 8), 8, []),
    ])
    def test_num_of_positions_south_east_from_current(self, start_pos, num_of_steps, expected):
        alg_not = Pos(start_pos)
        positions = alg_not.south_east(num_of_steps)
        self.assertEqual(expected, positions)

    @parameterized.expand([
        (('a', 1), 8, []),
        (('a', 5), 1, []),
        (('d', 2), 3, [('c', 3), ('b', 4), ('a', 5)]),
        (('e', 6), 4, [('d', 7), ('c', 8)]),
        (('h', 3), 6, [('g', 4), ('f', 5), ('e', 6), ('d', 7), ('c', 8)]),
        (('b', 4), 1, [('a', 5)]),
        (('b', 7), 1, [('a', 8)]),
        (('a', 8), 1, []),
        (('c', 8), 4, []),
        (('e', 8), 8, []),
        (('a', 1), 2, []),
        (('a', 2), 8, []),
        (('g', 4), 3, [('f', 5), ('e', 6), ('d', 7)]),
        (('d', 4), 8, [('c', 5), ('b', 6), ('a', 7)]),
        (('h', 1), 8, [('g', 2), ('f', 3), ('e', 4), ('d', 5), ('c', 6), ('b', 7), ('a', 8)]),
    ])
    def test_num_of_positions_north_west_from_current(self, start_pos, num_of_steps, expected):
        alg_not = Pos(start_pos)
        positions = alg_not.north_west(num_of_steps)
        self.assertEqual(expected, positions)
