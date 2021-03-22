from abc import abstractmethod

from chessboard.color import *


class Piece:
    def __init__(self, color, name, icon):
        self.color = color
        self.name = name
        self.icon = icon
        self.position = None
        self.moves = 0

    def set_position(self, position):
        self.position = position

    @abstractmethod
    def possible_moves(self):
        pass


class Knight(Piece):
    icons = {Color.WHITE: "♘", Color.BLACK: "♞"}

    def __init__(self, color):
        super().__init__(color, "N", Knight.icons[color])

    def possible_moves(self):
        possible_moves = []
        pos = Pos(self.position)
        if pos.north_east(1):
            possible_moves.append(pos.north_east(1)[0].north(1))
            possible_moves.append(pos.north_east(1)[0].east(1))
        if pos.north_west(1):
            possible_moves.append(pos.north_west(1)[0].north(1))
            possible_moves.append(pos.north_west(1)[0].west(1))
        if pos.south_east(1):
            possible_moves.append(pos.south_east(1)[0].south(1))
            possible_moves.append(pos.south_east(1)[0].east(1))
        if pos.south_west(1):
            possible_moves.append(pos.south_west(1)[0].south(1))
            possible_moves.append(pos.south_west(1)[0].west(1))
        return [[i] for sublist in (filter(None, possible_moves)) for i in sublist]


class Queen(Piece):
    icons = {Color.WHITE: "♕", Color.BLACK: "♛"}

    def __init__(self, color):
        super().__init__(color, "Q", Queen.icons[color])

    def possible_moves(self):
        return [Pos((self.position[0], int(self.position[1]))).north(8),
                Pos((self.position[0], int(self.position[1]))).south(8),
                Pos((self.position[0], int(self.position[1]))).east(8),
                Pos((self.position[0], int(self.position[1]))).west(8),
                Pos((self.position[0], int(self.position[1]))).north_east(8),
                Pos((self.position[0], int(self.position[1]))).north_west(8),
                Pos((self.position[0], int(self.position[1]))).south_east(8),
                Pos((self.position[0], int(self.position[1]))).south_west(8)]


class Bishop(Piece):
    icons = {Color.WHITE: "♗", Color.BLACK: "♝"}

    def __init__(self, color):
        super().__init__(color, "B", Bishop.icons[color])

    def possible_moves(self):
        return [Pos((self.position[0], int(self.position[1]))).north_east(8),
                Pos((self.position[0], int(self.position[1]))).north_west(8),
                Pos((self.position[0], int(self.position[1]))).south_east(8),
                Pos((self.position[0], int(self.position[1]))).south_west(8)]


class Pawn(Piece):
    icons = {Color.WHITE: "♙", Color.BLACK: "♟"}

    def __init__(self, color):
        super().__init__(color, "P", Pawn.icons[color])

    def possible_moves(self):
        position = Pos((self.position[0], int(self.position[1])))
        if self.color == Color.WHITE:
            return [position.north(1 + (self.moves == 0))]
        else:
            return [position.south(1 + (self.moves == 0))]


class King(Piece):
    icons = {Color.WHITE: "♔", Color.BLACK: "♚"}

    def __init__(self, color):
        super().__init__(color, "K", King.icons[color])

    def possible_moves(self):
        return [Pos((self.position[0], int(self.position[1]))).north(1),
                Pos((self.position[0], int(self.position[1]))).south(1),
                Pos((self.position[0], int(self.position[1]))).east(1),
                Pos((self.position[0], int(self.position[1]))).west(1),
                Pos((self.position[0], int(self.position[1]))).north_east(1),
                Pos((self.position[0], int(self.position[1]))).north_west(1),
                Pos((self.position[0], int(self.position[1]))).south_east(1),
                Pos((self.position[0], int(self.position[1]))).south_west(1)]


class Rook(Piece):
    icons = {Color.WHITE: "♖", Color.BLACK: "♜"}

    def __init__(self, color):
        super().__init__(color, "R", Rook.icons[color])

    def possible_moves(self):
        return [Pos((self.position[0], int(self.position[1]))).north(8),
                Pos((self.position[0], int(self.position[1]))).south(8),
                Pos((self.position[0], int(self.position[1]))).east(8),
                Pos((self.position[0], int(self.position[1]))).west(8)]


class Pos(tuple):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    nums = [1, 2, 3, 4, 5, 6, 7, 8]

    def __init__(self, pos):
        if pos[0] in self.letters and pos[1] in self.nums:
            self.letter = pos[0]
            self.num = pos[1]
        else:
            raise ValueError(
                "Must have first element lower case char between a:h and second element int between 1:8")

    def north(self, steps):
        return Pos.to_pos(zip([self.letter for _ in range(1, 8)], self.nums[self.num:self.num + steps:]))

    def south(self, steps):
        return Pos.to_pos(
            zip([self.letter for _ in range(1, 8)],
                reversed(self.nums[max(0, self.num - 1 - steps):self.num - 1:])))

    def east(self, steps):
        index = self.letters.index(self.letter)
        return Pos.to_pos(zip(self.letters[index + 1:index + 1 + steps:], [self.num for _ in range(1, 8)]))

    def west(self, steps):
        index = self.letters.index(self.letter)
        return Pos.to_pos(
            zip(reversed(self.letters[max(0, index - steps):index:]), [self.num for _ in range(1, 8)]))

    def north_east(self, steps):
        return Pos.to_pos(zip([i[0] for i in self.east(steps)], [j[1] for j in self.north(steps)]))

    def south_west(self, steps):
        return Pos.to_pos(zip([i[0] for i in self.west(steps)], [j[1] for j in self.south(steps)]))

    def south_east(self, steps):
        return Pos.to_pos(zip([i[0] for i in self.east(steps)], [j[1] for j in self.south(steps)]))

    def north_west(self, steps):
        return Pos.to_pos(zip([i[0] for i in self.west(steps)], [j[1] for j in self.north(steps)]))

    @staticmethod
    def to_pos(steps):
        return [Pos(i) for i in steps]
