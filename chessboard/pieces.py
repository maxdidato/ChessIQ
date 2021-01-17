from chessboard.color import *
from abc import abstractmethod


class Piece:
    def __init__(self, color, name, icon):
        self.color = color
        self.name = name
        self.icon = icon
        self.position = None

    def set_position(self, position):
        self.position = position

    @staticmethod
    def parse_algebraic_notation(notation):
        letter = notation[:1]
        number = int(notation[-1])
        return abs(8 - number), ord(letter) - 97

    @staticmethod
    def parse_to_algebraic_notation(indexes):
        return str(chr(indexes[1] + 97)) + str(abs(indexes[0] - 8))

    @abstractmethod
    def possible_moves(self):
        pass


class Knight(Piece):
    icons = {Color.WHITE: "♘", Color.BLACK: "♞"}

    def __init__(self, color):
        super().__init__(color, "N", Knight.icons[color])


class Queen(Piece):
    icons = {Color.WHITE: "♕", Color.BLACK: "♛"}

    def __init__(self, color):
        super().__init__(color, "Q", Queen.icons[color])

    def possible_moves(self):
        indexes = self.__class__.parse_algebraic_notation(self.position)
        possible_moves = Moves()

        possible_moves.set_northeast([Piece.parse_to_algebraic_notation(i) for i in
                                      zip([i for i in range(indexes[0], -1, -1)], [j for j in range(indexes[1], 8)])])
        possible_moves.set_southeast([Piece.parse_to_algebraic_notation(i) for i in
                                      zip([i for i in range(indexes[0], 8)], [j for j in range(indexes[1], 8)])])
        possible_moves.set_southwest([Piece.parse_to_algebraic_notation(i) for i in
                                      zip([i for i in range(indexes[0], 8)], [j for j in range(indexes[1], -1, -1)])])
        possible_moves.set_northwest([Piece.parse_to_algebraic_notation(i) for i in
                                      zip([i for i in range(indexes[0], -1, -1)],
                                          [j for j in range(indexes[1], -1, -1)])])
        possible_moves.set_east([Piece.parse_to_algebraic_notation((indexes[0], j)) for j in range(indexes[1], 8)])
        possible_moves.set_west([Piece.parse_to_algebraic_notation((indexes[0], j)) for j in range(indexes[1], -1, -1)])
        possible_moves.set_south([Piece.parse_to_algebraic_notation((i, indexes[1])) for i in range(indexes[0], 8)])
        possible_moves.set_north(
            [Piece.parse_to_algebraic_notation((i, indexes[1])) for i in range(indexes[0], -1, -1)])
        return possible_moves


class Bishop(Piece):
    icons = {Color.WHITE: "♗", Color.BLACK: "♝"}

    def __init__(self, color):
        super().__init__(color, "B", Bishop.icons[color])

    def possible_moves(self):
        indexes = self.__class__.parse_algebraic_notation(self.position)
        possible_moves = Moves()

        possible_moves.set_northeast([Piece.parse_to_algebraic_notation(i) for i in
                                      zip([i for i in range(indexes[0], -1, -1)], [j for j in range(indexes[1], 8)])])
        possible_moves.set_southeast([Piece.parse_to_algebraic_notation(i) for i in
                                      zip([i for i in range(indexes[0], 8)], [j for j in range(indexes[1], 8)])])
        possible_moves.set_southwest([Piece.parse_to_algebraic_notation(i) for i in
                                      zip([i for i in range(indexes[0], 8)], [j for j in range(indexes[1], -1, -1)])])
        possible_moves.set_northwest([Piece.parse_to_algebraic_notation(i) for i in
                                      zip([i for i in range(indexes[0], -1, -1)],
                                          [j for j in range(indexes[1], -1, -1)])])

        return possible_moves


class Pawn(Piece):
    icons = {Color.WHITE: "♙", Color.BLACK: "♟"}

    def __init__(self, color):
        super().__init__(color, "P", Pawn.icons[color])

    def possible_moves(self):
        indexes = self.__class__.parse_algebraic_notation(self.position)
        possible_moves = Moves()
        if self.color == Color.WHITE:
            possible_moves.set_north([Piece.parse_to_algebraic_notation((indexes[0] - 1, indexes[1]))])
        else:
            possible_moves.set_south([Piece.parse_to_algebraic_notation((indexes[0] + 1, indexes[1]))])
        return possible_moves


class King(Piece):
    icons = {Color.WHITE: "♔", Color.BLACK: "♚"}

    def __init__(self, color):
        super().__init__(color, "K", King.icons[color])

    def possible_moves(self):
        indexes = self.__class__.parse_algebraic_notation(self.position)
        possible_moves = Moves()
        possible_moves.set_north([Piece.parse_to_algebraic_notation((indexes[0] - 1, indexes[1]))])
        possible_moves.set_northeast([Piece.parse_to_algebraic_notation((indexes[0] - 1, indexes[1] + 1))])
        possible_moves.set_east([Piece.parse_to_algebraic_notation((indexes[0], indexes[1] + 1))])
        possible_moves.set_southeast([Piece.parse_to_algebraic_notation((indexes[0] + 1, indexes[1] + 1))])
        possible_moves.set_south([Piece.parse_to_algebraic_notation((indexes[0] + 1, indexes[1]))])
        possible_moves.set_southwest([Piece.parse_to_algebraic_notation((indexes[0] + 1, indexes[1] - 1))])
        possible_moves.set_west([Piece.parse_to_algebraic_notation((indexes[0], indexes[1] - 1))])
        possible_moves.set_northwest([Piece.parse_to_algebraic_notation((indexes[0] - 1, indexes[1] - 1))])
        return possible_moves


class Rook(Piece):
    icons = {Color.WHITE: "♖", Color.BLACK: "♜"}

    def __init__(self, color):
        super().__init__(color, "R", Rook.icons[color])

    def possible_moves(self):
        indexes = self.__class__.parse_algebraic_notation(self.position)
        possible_moves = Moves()
        possible_moves.set_east([Piece.parse_to_algebraic_notation((indexes[0], j)) for j in range(indexes[1], 8)])
        possible_moves.set_west([Piece.parse_to_algebraic_notation((indexes[0], j)) for j in range(indexes[1], -1, -1)])
        possible_moves.set_south([Piece.parse_to_algebraic_notation((i, indexes[1])) for i in range(indexes[0], 8)])
        possible_moves.set_north(
            [Piece.parse_to_algebraic_notation((i, indexes[1])) for i in range(indexes[0], -1, -1)])
        return possible_moves


class Moves:
    def __init__(self):
        self.moves = {}

    @staticmethod
    def filter_illegal_moves(moves_list):
        return list(filter(lambda pos: ord(pos[0]) in range(97, 106) and int(pos[1]) in range(1, 9),moves_list))

    def all_moves(self):
        return [item for subl in self.moves.values() for item in subl]

    def set_north(self, moves_list):
        self.moves['N'] = Moves.filter_illegal_moves(moves_list)

    def set_east(self, moves_list):
        self.moves['E'] = Moves.filter_illegal_moves(moves_list)

    def set_south(self, moves_list):
        self.moves['S'] = Moves.filter_illegal_moves(moves_list)

    def set_west(self, moves_list):
        self.moves['W'] = Moves.filter_illegal_moves(moves_list)

    def set_northeast(self, moves_list):
        self.moves['NE'] = Moves.filter_illegal_moves(moves_list)

    def set_northwest(self, moves_list):
        self.moves['NW'] = Moves.filter_illegal_moves(moves_list)

    def set_southeast(self, moves_list):
        self.moves['SE'] = Moves.filter_illegal_moves(moves_list)

    def set_southwest(self, moves_list):
        self.moves['SW'] = Moves.filter_illegal_moves(moves_list)
