from abc import abstractmethod

import pygame as pg
from pygame.locals import *

from chessboard.board import ChessBoard
from chessboard.board import Square


class UISquare(Rect):

    def __init__(self, screen, left, top, width, height, square):
        self.square: Square = square
        self.screen = screen
        self.candidate_move = None
        self.alg_not: ChessBoard.AlgNot = square.alg_not
        super().__init__(left, top, width, height)
        self.state = Default(self)

    def draw(self):
        self.state.draw()
        if self.square.piece:
            f = pg.font.Font("segoe-ui-symbol.ttf", int(self.width))
            self.screen.blit(
                f.render(self.square.piece.icon, True, pg.Color(self.square.piece.color.value)),
                (self.left, self.top))

    def change_state(self, state_class):
        self.state = state_class(self)

    def has_state(self, state_class):
        return isinstance(self.state, state_class)

    def left_click(self):
        self.state.left_click()


class UiSquareState:
    def __init__(self, ui_square):
        self.ui_square = ui_square

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def left_click(self):
        pass


class Highlighted(UiSquareState):
    def __init__(self, ui_square):
        super().__init__(ui_square)

    def draw(self):
        pg.draw.rect(self.ui_square.screen, pg.Color('yellow'), self.ui_square, 0)

    def left_click(self):
        self.ui_square.change_state(Default)


class MoveCandidate(UiSquareState):
    def __init__(self, ui_square):
        super().__init__(ui_square)

    def draw(self):
        pg.draw.rect(self.ui_square.screen, pg.Color('lightblue'), self.ui_square, 0)

    def left_click(self):
        pass


class Default(UiSquareState):
    def __init__(self, ui_square):
        super().__init__(ui_square)

    def draw(self):
        pg.draw.rect(self.ui_square.screen, pg.Color(self.ui_square.square.color.value), self.ui_square, 0)

    def left_click(self):
        self.ui_square.change_state(Highlighted)
