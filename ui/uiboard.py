import pygame as pg
from pygame.locals import *


class UIBoard(Rect):

    def __init__(self, left, top, board_size, to_draw):
        self.board = to_draw
        self.__board_size = board_size
        self.__cell_size = board_size / 8
        self.drawn_cells = []
        self.__screen = pg.display.set_mode([500, 500])
        super().__init__(left, top, self.__board_size, self.__board_size)

    def __initialise(self):
        pg.init()
        self.__screen.fill((255, 255, 255))
        self.drawn_cells = []
        for row_idx, row in enumerate(self.board):
            for cell_idx, cell in enumerate(row):
                self.drawn_cells.append(
                    UICell(self.top + self.__cell_size * cell_idx, self.left + self.__cell_size * row_idx,
                           self.__cell_size, self.__cell_size,
                           cell))
        return self

    def draw_board(self):
        for drawn_cell in self.drawn_cells:
            if drawn_cell.highlighted:
                pg.draw.rect(self.__screen, pg.Color('yellow'), drawn_cell, 0)
            else:
                pg.draw.rect(self.__screen, pg.Color(drawn_cell.cell.color.value), drawn_cell, 0)
            if drawn_cell.cell.piece:
                f = pg.font.Font("segoe-ui-symbol.ttf", int(self.__cell_size))
                self.__screen.blit(
                    f.render(drawn_cell.cell.piece.icon, True, pg.Color(drawn_cell.cell.piece.color.value)),
                    (drawn_cell.left, drawn_cell.top))

    def manage_left_click(self, position):
        clicked_cell = next(filter(lambda x: x.collidepoint(position) == 1, self.drawn_cells), None)
        if clicked_cell:
            clicked_cell.highlight()

    def start(self):
        self.__initialise()
        while True:
            for event in pg.event.get():
                if event.type == MOUSEBUTTONUP:
                    self.manage_left_click(event.pos)
                if event.type == QUIT:
                    pg.quit()
            self.draw_board()
            pg.display.flip()
            pg.display.update()


class UICell(Rect):

    def __init__(self, left, top, width, height, cell):
        self.cell = cell
        self.highlighted = False
        super().__init__(left, top, width, height)

    def highlight(self):
        self.highlighted = True
