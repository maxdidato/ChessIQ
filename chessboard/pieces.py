from chessboard.color import *


class Piece:
    def __init__(self, color, name, icon):
        self.color = color
        self.name = name
        self.icon = icon


class Knight(Piece):
    icons = {Color.WHITE: "♘", Color.BLACK: "♞"}

    def __init__(self, color):
        super().__init__(color, "N", Knight.icons[color])


class Queen(Piece):
    icons = {Color.WHITE: "♕", Color.BLACK: "♛"}

    def __init__(self, color):
        super().__init__(color, "Q", Queen.icons[color])


class Bishop(Piece):
    icons = {Color.WHITE: "♗", Color.BLACK: "♝"}

    def __init__(self, color):
        super().__init__(color, "B", Bishop.icons[color])


class Pawn(Piece):
    icons = {Color.WHITE: "♙", Color.BLACK: "♟"}

    def __init__(self, color):
        super().__init__(color, "P", Pawn.icons[color])


class King(Piece):
    icons = {Color.WHITE: "♔", Color.BLACK: "♚"}

    def __init__(self, color):
        super().__init__(color, "K", King.icons[color])


class Rook(Piece):
    icons = {Color.WHITE: "♖", Color.BLACK: "♜"}

    def __init__(self, color):
        super().__init__(color, "R", Rook.icons[color])
