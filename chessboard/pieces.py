from chessboard.color import *
from abc import abstractmethod


class Piece:
    def __init__(self, color, name, icon):
        self.color = color
        self.name = name
        self.icon = icon
        self.position = None
        self.alg_not = None

    def set_position(self, position):
        self.position = position
        self.alg_not = AlgNot(position[:1], int(position[-1]))

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

    def possible_moves(self):
        indexes = self.__class__.parse_algebraic_notation(self.position)
        moves = []

        for i in range(1, 3):
            moves.append((indexes[0] + i, indexes[1] + (3 - i)))
            moves.append((indexes[0] - i, indexes[1] - (3 - i)))
            moves.append((indexes[0] + (3 - i), indexes[1] - i))
            moves.append((indexes[0] - (3 - i), indexes[1] + i))
        moves = list(filter(lambda x: x[0] in range(0, 8) and (x[1] in range(0, 8)), moves))
        possible_moves = Moves()
        possible_moves.add_non_directional_moves([Piece.parse_to_algebraic_notation(i) for i in moves])
        return possible_moves


class Queen(Piece):
    icons = {Color.WHITE: "♕", Color.BLACK: "♛"}

    def __init__(self, color):
        super().__init__(color, "Q", Queen.icons[color])

    def possible_moves(self):
        indexes = self.__class__.parse_algebraic_notation(self.position)
        possible_moves = Moves()

        possible_moves.add_directional_moves([Piece.parse_to_algebraic_notation(i) for i in
                                              zip([i for i in range(indexes[0] - 1, -1, -1)],
                                                  [j for j in range(indexes[1] + 1, 8)])])
        possible_moves.add_directional_moves([Piece.parse_to_algebraic_notation(i) for i in
                                              zip([i for i in range(indexes[0] + 1, 8)],
                                                  [j for j in range(indexes[1] + 1, 8)])])
        possible_moves.add_directional_moves([Piece.parse_to_algebraic_notation(i) for i in
                                              zip([i for i in range(indexes[0] + 1, 8)],
                                                  [j for j in range(indexes[1] - 1, -1, -1)])])
        possible_moves.add_directional_moves([Piece.parse_to_algebraic_notation(i) for i in
                                              zip([i for i in range(indexes[0] - 1, -1, -1)],
                                                  [j for j in range(indexes[1] - 1, -1, -1)])])
        possible_moves.add_directional_moves(
            [Piece.parse_to_algebraic_notation((indexes[0], j)) for j in range(indexes[1] + 1, 8)])
        possible_moves.add_directional_moves(
            [Piece.parse_to_algebraic_notation((indexes[0], j)) for j in range(indexes[1] - 1, -1, -1)])
        possible_moves.add_directional_moves(
            [Piece.parse_to_algebraic_notation((i, indexes[1])) for i in range(indexes[0] + 1, 8)])
        possible_moves.add_directional_moves(
            [Piece.parse_to_algebraic_notation((i, indexes[1])) for i in range(indexes[0] - 1, -1, -1)])
        return possible_moves


class Bishop(Piece):
    icons = {Color.WHITE: "♗", Color.BLACK: "♝"}

    def __init__(self, color):
        super().__init__(color, "B", Bishop.icons[color])

    def possible_moves(self):
        indexes = self.__class__.parse_algebraic_notation(self.position)
        possible_moves = Moves()

        possible_moves.add_directional_moves([Piece.parse_to_algebraic_notation(i) for i in
                                              zip([i for i in range(indexes[0] - 1, -1, -1)],
                                                  [j for j in range(indexes[1] + 1, 8)])])
        possible_moves.add_directional_moves([Piece.parse_to_algebraic_notation(i) for i in
                                              zip([i for i in range(indexes[0] + 1, 8)],
                                                  [j for j in range(indexes[1] + 1, 8)])])
        possible_moves.add_directional_moves([Piece.parse_to_algebraic_notation(i) for i in
                                              zip([i for i in range(indexes[0] + 1, 8)],
                                                  [j for j in range(indexes[1] - 1, -1, -1)])])
        possible_moves.add_directional_moves([Piece.parse_to_algebraic_notation(i) for i in
                                              zip([i for i in range(indexes[0] - 1, -1, -1)],
                                                  [j for j in range(indexes[1] - 1, -1, -1)])])

        return possible_moves


class Pawn(Piece):
    icons = {Color.WHITE: "♙", Color.BLACK: "♟"}

    def __init__(self, color):
        super().__init__(color, "P", Pawn.icons[color])

    def possible_moves(self):
        indexes = self.__class__.parse_algebraic_notation(self.position)
        possible_moves = Moves()
        if self.color == Color.WHITE:
            possible_moves.add_directional_moves(self.alg_not.north(1))
            # possible_moves.add_directional_moves([Piece.parse_to_algebraic_notation((indexes[0] - 1, indexes[1]))])
        else:
            possible_moves.add_directional_moves(self.alg_not.south(1))
            # possible_moves.add_directional_moves([Piece.parse_to_algebraic_notation((indexes[0] + 1, indexes[1]))])
        return possible_moves


class King(Piece):
    icons = {Color.WHITE: "♔", Color.BLACK: "♚"}

    def __init__(self, color):
        super().__init__(color, "K", King.icons[color])

    def possible_moves(self):
        indexes = self.__class__.parse_algebraic_notation(self.position)
        possible_moves = Moves()
        possible_moves.add_directional_moves([Piece.parse_to_algebraic_notation((indexes[0] - 1, indexes[1]))])
        possible_moves.add_directional_moves([Piece.parse_to_algebraic_notation((indexes[0] - 1, indexes[1] + 1))])
        possible_moves.add_directional_moves([Piece.parse_to_algebraic_notation((indexes[0], indexes[1] + 1))])
        possible_moves.add_directional_moves([Piece.parse_to_algebraic_notation((indexes[0] + 1, indexes[1] + 1))])
        possible_moves.add_directional_moves([Piece.parse_to_algebraic_notation((indexes[0] + 1, indexes[1]))])
        possible_moves.add_directional_moves([Piece.parse_to_algebraic_notation((indexes[0] + 1, indexes[1] - 1))])
        possible_moves.add_directional_moves([Piece.parse_to_algebraic_notation((indexes[0], indexes[1] - 1))])
        possible_moves.add_directional_moves([Piece.parse_to_algebraic_notation((indexes[0] - 1, indexes[1] - 1))])
        return possible_moves


class Rook(Piece):
    icons = {Color.WHITE: "♖", Color.BLACK: "♜"}

    def __init__(self, color):
        super().__init__(color, "R", Rook.icons[color])

    def possible_moves(self):
        indexes = self.__class__.parse_algebraic_notation(self.position)
        possible_moves = Moves()
        possible_moves.add_directional_moves(
            [Piece.parse_to_algebraic_notation((indexes[0], j)) for j in range(indexes[1] + 1, 8)])
        possible_moves.add_directional_moves(
            [Piece.parse_to_algebraic_notation((indexes[0], j)) for j in range(indexes[1] - 1, -1, -1)])
        possible_moves.add_directional_moves(
            [Piece.parse_to_algebraic_notation((i, indexes[1])) for i in range(indexes[0] + 1, 8)])
        possible_moves.add_directional_moves(
            [Piece.parse_to_algebraic_notation((i, indexes[1])) for i in range(indexes[0] - 1, -1, -1)])
        return possible_moves


class AlgNot:
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    nums = [1, 2, 3, 4, 5, 6, 7, 8]

    def __init__(self, letter, num):
        self.letter = letter
        self.num = num

    # Think about composing methods to express mixed direction. like north().east().build(2)
    def north(self, steps):
        positions = zip([self.letter for i in range(1, 8)], self.nums[self.num:self.num + steps:])
        return [pos[0] + str(pos[1]) for pos in positions]

    def south(self, steps):
        positions = zip([self.letter for _ in range(1, 8)],
                        reversed(self.nums[max(0, self.num - 1 - steps):self.num - 1:]))
        return [pos[0] + str(pos[1]) for pos in positions]

    def east(self, steps):
        index = self.letters.index(self.letter)
        positions = zip(self.letters[index + 1:index + 1 + steps:], [self.num for _ in range(1, 8)])
        return [pos[0] + str(pos[1]) for pos in positions]

    def west(self, steps):
        index = self.letters.index(self.letter)
        positions = zip(reversed(self.letters[max(0, index - steps):index:]), [self.num for _ in range(1, 8)])
        return [pos[0] + str(pos[1]) for pos in positions]


# possible_moves.add_directional_moves([Piece.parse_to_algebraic_notation((indexes[0] - 1, indexes[1]))])


class Moves:
    def __init__(self):
        self.moves = [[], []]

    @staticmethod
    def filter_illegal_moves(moves_list):
        return list(filter(lambda pos: ord(pos[0]) in range(97, 106) and int(pos[1]) in range(1, 9), moves_list))

    def add_directional_moves(self, moves_list):
        self.moves[0].append(Moves.filter_illegal_moves(moves_list))

    def add_non_directional_moves(self, moves_list):
        self.moves[1] = Moves.filter_illegal_moves(moves_list)

    def get_directional_moves(self):
        return self.moves[0]

    def get_non_directional_moves(self):
        return self.moves[1]
