import string
from chessboard import color
from ui.uisquare import *


class UIBoard(Rect):

    def __init__(self, left, top, board_size, to_draw):
        self.board = to_draw
        self.turn = color.Color.WHITE
        self.drawn_squares = []
        self.__square_size = board_size / 8
        self.__screen = pg.display.set_mode([500, 500])
        super().__init__(left, top, board_size, board_size)

    def __initialise(self):
        pg.init()
        self.__screen.fill((255, 255, 255))
        for row_idx, num in enumerate(reversed(range(1, 9))):
            for cell_idx, let in enumerate(list(string.ascii_lowercase[0:8])):
                self.drawn_squares.append(
                    UISquare(self.__screen, self.top + self.__square_size * cell_idx,
                             self.left + self.__square_size * row_idx,
                             self.__square_size, self.__square_size,
                             self.board[(let, num)]))
        return self

    def draw_board(self):
        for drawn_square in self.drawn_squares:
            drawn_square.draw()

    def highlight_possible_moves(self, ui_square):
        for move in self.board.possible_moves(ui_square.square):
            next(filter(lambda x: x.square.alg_not == move, self.drawn_squares)).change_state(MoveCandidate)

    def find_clicked_square(self, coordinates):
        return next(filter(lambda x: x.collidepoint(coordinates), self.drawn_squares), None)

    def get_highlighted_square(self):
        return next(filter(lambda x: x.has_state(Highlighted), self.drawn_squares))

    def reset_squares_to_default(self):
        for square in self.drawn_squares:
            square.change_state(Default)

    def manage_left_click(self, coordinates):
        clicked_square = self.find_clicked_square(coordinates)
        if clicked_square.has_state(MoveCandidate):
            self.board.move_piece(self.get_highlighted_square().alg_not,clicked_square.alg_not)
            self.turn = color.Color.WHITE if self.turn == color.Color.BLACK else color.Color.BLACK
            self.reset_squares_to_default()
        elif clicked_square.square.piece and clicked_square.square.piece.color == self.turn:
            self.reset_squares_to_default()
            clicked_square.left_click()
            if clicked_square.has_state(Highlighted):
                self.highlight_possible_moves(clicked_square)

    def start(self):
        self.__initialise()
        while True:
            for event in pg.event.get():
                if event.type == MOUSEBUTTONUP:
                    if self.collidepoint(event.pos):
                        self.manage_left_click(event.pos)
                if event.type == QUIT:
                    pg.quit()
            self.draw_board()
            pg.display.flip()
            pg.display.update()


