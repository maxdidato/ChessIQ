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
        self.alg_not = Position(position[:1], int(position[-1]))

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
        moves = [Piece.parse_to_algebraic_notation(i) for i in moves]
        possible_moves.add_non_directional_moves([(str(i[0]), int(i[1])) for i in moves])
        return possible_moves


class Queen(Piece):
    icons = {Color.WHITE: "♕", Color.BLACK: "♛"}

    def __init__(self, color):
        super().__init__(color, "Q", Queen.icons[color])

    def possible_moves(self):
        possible_moves = Moves()
        possible_moves.add_directional_moves(Position((self.position[0], int(self.position[1]))).north(8))
        possible_moves.add_directional_moves(Position((self.position[0], int(self.position[1]))).south(8))
        possible_moves.add_directional_moves(Position((self.position[0], int(self.position[1]))).east(8))
        possible_moves.add_directional_moves(Position((self.position[0], int(self.position[1]))).west(8))
        possible_moves.add_directional_moves(Position((self.position[0], int(self.position[1]))).north_east(8))
        possible_moves.add_directional_moves(Position((self.position[0], int(self.position[1]))).north_west(8))
        possible_moves.add_directional_moves(Position((self.position[0], int(self.position[1]))).south_east(8))
        possible_moves.add_directional_moves(Position((self.position[0], int(self.position[1]))).south_west(8))
        return possible_moves


class Bishop(Piece):
    icons = {Color.WHITE: "♗", Color.BLACK: "♝"}

    def __init__(self, color):
        super().__init__(color, "B", Bishop.icons[color])

    def possible_moves(self):
        possible_moves = Moves()
        possible_moves.add_directional_moves(Position((self.position[0], int(self.position[1]))).north_east(8))
        possible_moves.add_directional_moves(Position((self.position[0], int(self.position[1]))).north_west(8))
        possible_moves.add_directional_moves(Position((self.position[0], int(self.position[1]))).south_east(8))
        possible_moves.add_directional_moves(Position((self.position[0], int(self.position[1]))).south_west(8))
        return possible_moves


class Pawn(Piece):
    icons = {Color.WHITE: "♙", Color.BLACK: "♟"}

    def __init__(self, color):
        super().__init__(color, "P", Pawn.icons[color])

    def possible_moves(self):
        possible_moves = Moves()
        if self.color == Color.WHITE:
            possible_moves.add_directional_moves(Position((self.position[0], int(self.position[1]))).north(1))
        else:
            possible_moves.add_directional_moves(Position((self.position[0], int(self.position[1]))).south(1))
        return possible_moves


class King(Piece):
    icons = {Color.WHITE: "♔", Color.BLACK: "♚"}

    def __init__(self, color):
        super().__init__(color, "K", King.icons[color])

    def possible_moves(self):
        possible_moves = Moves()
        possible_moves.add_directional_moves(Position((self.position[0], int(self.position[1]))).north(1))
        possible_moves.add_directional_moves(Position((self.position[0], int(self.position[1]))).south(1))
        possible_moves.add_directional_moves(Position((self.position[0], int(self.position[1]))).east(1))
        possible_moves.add_directional_moves(Position((self.position[0], int(self.position[1]))).west(1))
        possible_moves.add_directional_moves(Position((self.position[0], int(self.position[1]))).north_east(1))
        possible_moves.add_directional_moves(Position((self.position[0], int(self.position[1]))).north_west(1))
        possible_moves.add_directional_moves(Position((self.position[0], int(self.position[1]))).south_east(1))
        possible_moves.add_directional_moves(Position((self.position[0], int(self.position[1]))).south_west(1))
        return possible_moves


class Rook(Piece):
    icons = {Color.WHITE: "♖", Color.BLACK: "♜"}

    def __init__(self, color):
        super().__init__(color, "R", Rook.icons[color])

    def possible_moves(self):
        possible_moves = Moves()
        possible_moves.add_directional_moves(Position((self.position[0], int(self.position[1]))).north(8))
        possible_moves.add_directional_moves(Position((self.position[0], int(self.position[1]))).south(8))
        possible_moves.add_directional_moves(Position((self.position[0], int(self.position[1]))).east(8))
        possible_moves.add_directional_moves(Position((self.position[0], int(self.position[1]))).west(8))
        return possible_moves


class Position:
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    nums = [1, 2, 3, 4, 5, 6, 7, 8]

    def __init__(self, pos):
        if pos[0] in self.letters and pos[1] in self.nums:
            self.letter = pos[0]
            self.num = pos[1]
        else:
            raise ValueError("Must have first element lower case char between a:h and second element int between 1:8")

    def north(self, steps):
        return list(zip([self.letter for _ in range(1, 8)], self.nums[self.num:self.num + steps:]))

    def south(self, steps):
        return list(
            zip([self.letter for _ in range(1, 8)], reversed(self.nums[max(0, self.num - 1 - steps):self.num - 1:])))

    def east(self, steps):
        index = self.letters.index(self.letter)
        return list(zip(self.letters[index + 1:index + 1 + steps:], [self.num for _ in range(1, 8)]))

    def west(self, steps):
        index = self.letters.index(self.letter)
        return list(zip(reversed(self.letters[max(0, index - steps):index:]), [self.num for _ in range(1, 8)]))

    def north_east(self, steps):
        return list(zip([i[0] for i in self.east(steps)], [j[1] for j in self.north(steps)]))

    def south_west(self, steps):
        return list(zip([i[0] for i in self.west(steps)], [j[1] for j in self.south(steps)]))

    def south_east(self, steps):
        return list(zip([i[0] for i in self.east(steps)], [j[1] for j in self.south(steps)]))

    def north_west(self, steps):
        return list(zip([i[0] for i in self.west(steps)], [j[1] for j in self.north(steps)]))


class Moves:
    def __init__(self):
        self.moves = [[], []]

    def add_directional_moves(self, moves_list):
        self.moves[0].append(moves_list)

    def add_non_directional_moves(self, moves_list):
        self.moves[1] = moves_list

    def get_directional_moves(self):
        return self.moves[0]

    def get_non_directional_moves(self):
        return self.moves[1]
