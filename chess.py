from enum import Enum
import pygame as pg
from pygame.locals import *
import sys


class Color(Enum):
    WHITE = 'grey'
    BLACK = 'black'
    DARK = 'brown'
    LIGHT = 'beige'

    @classmethod
    def from_index(cls, index):
        if index % 2 == 0:
            return cls.DARK
        else:
            return cls.LIGHT


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


class Square:
    def __init__(self, color, piece=None):
        self.color = color
        self.piece = piece


class ChessBoard:
    def __init__(self):
        self.board = []

    def initialize(self):
        self.__draw_board()
        self.__initial_pieces_setting()

    def __parse_algebric_notation(self, notation):
        letter = notation[:1]
        number = int(notation[-1])
        return abs(8 - number), ord(letter) - 97

    def __place_piece(self, piece, position):
        indexes = self.__parse_algebric_notation(position)
        self.board[indexes[0]][indexes[1]].piece = piece

    def __initial_pieces_setting(self):
        self.__place_piece(Rook(Color.BLACK), 'a8')
        self.__place_piece(Knight(Color.BLACK), 'b8')
        self.__place_piece(Bishop(Color.BLACK), 'c8')
        self.__place_piece(Queen(Color.BLACK), 'd8')
        self.__place_piece(King(Color.BLACK), 'e8')
        self.__place_piece(Bishop(Color.BLACK), 'f8')
        self.__place_piece(Knight(Color.BLACK), 'g8')
        self.__place_piece(Rook(Color.BLACK), 'h8')
        self.__place_piece(Pawn(Color.BLACK), 'a7')
        self.__place_piece(Pawn(Color.BLACK), 'b7')
        self.__place_piece(Pawn(Color.BLACK), 'c7')
        self.__place_piece(Pawn(Color.BLACK), 'd7')
        self.__place_piece(Pawn(Color.BLACK), 'e7')
        self.__place_piece(Pawn(Color.BLACK), 'f7')
        self.__place_piece(Pawn(Color.BLACK), 'g7')
        self.__place_piece(Pawn(Color.BLACK), 'h7')
        self.__place_piece(Rook(Color.WHITE), 'a1')
        self.__place_piece(Knight(Color.WHITE), 'b1')
        self.__place_piece(Bishop(Color.WHITE), 'c1')
        self.__place_piece(Queen(Color.WHITE), 'd1')
        self.__place_piece(King(Color.WHITE), 'e1')
        self.__place_piece(Bishop(Color.WHITE), 'f1')
        self.__place_piece(Knight(Color.WHITE), 'g1')
        self.__place_piece(Rook(Color.WHITE), 'h1')
        self.__place_piece(Pawn(Color.WHITE), 'a2')
        self.__place_piece(Pawn(Color.WHITE), 'b2')
        self.__place_piece(Pawn(Color.WHITE), 'c2')
        self.__place_piece(Pawn(Color.WHITE), 'd2')
        self.__place_piece(Pawn(Color.WHITE), 'e2')
        self.__place_piece(Pawn(Color.WHITE), 'f2')
        self.__place_piece(Pawn(Color.WHITE), 'g2')
        self.__place_piece(Pawn(Color.WHITE), 'h2')

    def __draw_board(self):
        for i in range(8):
            self.board.append([])
            for j in range(8):
                self.board[i].append(Square(Color.from_index(j + i)))


pg.init()

screen = pg.display.set_mode([500, 500])
screen.fill((255, 255, 255))
chess_board = ChessBoard()
chess_board.initialize()
board_size = 400
cell_size = board_size / 8
board = pg.draw.rect(screen, pg.Color('blue'), pg.Rect(30, 30, board_size, board_size), 2)
while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()

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
