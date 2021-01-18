import pygame as pg
from pygame.locals import *


class UIBoard(Rect):

    def __init__(self, left, top, board_size, to_draw):
        self.board = to_draw
        self.drawn_squares = []
        self.__square_size = board_size / 8
        self.__screen = pg.display.set_mode([500, 500])
        super().__init__(left, top, board_size, board_size)

    def __initialise(self):
        pg.init()
        self.__screen.fill((255, 255, 255))
        for row_idx, row in enumerate(self.board):
            for cell_idx, cell in enumerate(row):
                self.drawn_squares.append(
                    UISquare(self.top + self.__square_size * cell_idx, self.left + self.__square_size * row_idx,
                             self.__square_size, self.__square_size,
                             cell))
        return self

    def draw_board(self):
        for drawn_square in self.drawn_squares:
            if drawn_square.highlighted:
                pg.draw.rect(self.__screen, pg.Color('yellow'), drawn_square, 0)
            elif drawn_square.move_candidate:
                pg.draw.rect(self.__screen, pg.Color('lightblue'), drawn_square, 0)
            else:
                pg.draw.rect(self.__screen, pg.Color(drawn_square.square.color.value), drawn_square, 0)
            if drawn_square.square.piece:
                f = pg.font.Font("segoe-ui-symbol.ttf", int(self.__square_size))
                self.__screen.blit(
                    f.render(drawn_square.square.piece.icon, True, pg.Color(drawn_square.square.piece.color.value)),
                    (drawn_square.left, drawn_square.top))

    def get_other_highlighted_squares(self, to_exclude):
        return list(filter(lambda x: x != to_exclude, filter(lambda x: x.highlighted, self.drawn_squares)))

    def manage_left_click(self, position):
        clicked_square = next(filter(lambda x: x.collidepoint(position), self.drawn_squares), None)
        if not clicked_square:
            return
        if clicked_square.move_candidate:
            highlighted_square = next(filter(lambda x: x.highlighted,self.drawn_squares))
            self.board.move_piece(highlighted_square.square.alg_not,clicked_square.square.alg_not)
            for square in self.drawn_squares:
                square.highlighted = False
                square.move_candidate = False
            return
        for square in self.drawn_squares:
            square.highlighted = False
            square.move_candidate = False
        if clicked_square and clicked_square.square.piece:
            clicked_square.toggle_highlight()
            if clicked_square.highlighted:
                for move in self.board.possible_moves(clicked_square.square):
                    next(filter(lambda x: x.square.alg_not == move, self.drawn_squares)).move_candidate = True
        # for square in self.get_other_highlighted_squares(clicked_square):
        #     square.highlighted = False

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


class UISquare(Rect):

    def __init__(self, left, top, width, height, square):
        self.square = square
        self.highlighted = False
        self.move_candidate = False
        super().__init__(left, top, width, height)

    def toggle_highlight(self):
        self.highlighted = not self.highlighted
