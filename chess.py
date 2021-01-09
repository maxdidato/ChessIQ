from enum import Enum
import pygame as pg
from pygame.locals import *
import sys


class Color(Enum):
    WHITE = 'grey'
    BLACK = 'black'


    @classmethod
    def from_index(cls,index):
        if (index) % 2 == 0:
            return cls.BLACK
        else:
            return cls.WHITE



class Piece:
    def __init__(self, color, name, icon):
        self.color = color
        self.name = name
        self.icon = icon


class Knight(Piece):
    icons = {Color.WHITE: "♘", Color.BLACK: "♞"}

    def __init__(self, color):
        super().__init__(color, "K", Knight.icons[color])


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
        super().__init__(color, "P", King.icons[color])


class Rook(Piece):
    icons = {Color.WHITE: "♖", Color.BLACK: "♜"}

    def __init__(self, color):
        super().__init__(color, "P", Rook.icons[color])


class Square:
    def __init__(self, color, piece=None):
        self.color = color
        self.piece = piece


class ChessBoard:
    def __init__(self):
        self.board = []

    def initialize(self):
        for i in range(8):
            self.board.append([])
            for j in range(8):
                self.board[i].append(Square(Color.from_index(j+i)))


pg.init()

screen = pg.display.set_mode([500, 500])
screen.fill((255, 255, 255))
while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
    board_size = 400
    cell_size = board_size / 8
    board = pg.draw.rect(screen, pg.Color('blue'), pg.Rect(30, 30, board_size, board_size), 2)
    chess_board = ChessBoard()
    chess_board.initialize()
    for row_idx, row in enumerate(chess_board.board):
        for cell_idx, cell in enumerate(row):
            rect = pg.Rect(board.top + cell_size * cell_idx, board.left + cell_size * row_idx, cell_size, cell_size)
            pg.draw.rect(screen, pg.Color(cell.color.value),
                         rect, 0)
            if (cell.piece):
                f = pg.font.Font("segoe-ui-symbol.ttf", int(cell_size))
                screen.blit(f.render(cell.piece.icon, True, pg.Color(cell.piece.color.value)), (rect.left, rect.top))

    pg.display.flip()
    pg.display.update()
