import string
import time
from typing import *

from chessboard import color
from chessboard.moves import *
from ui.uisquare import *


class UIBoard(Rect):

    def __init__(self, left, top, board_size, to_draw):
        self.board: ChessBoard = to_draw
        self.turn: Color = color.Color.WHITE
        self.drawn_squares: List[UISquare] = []
        self.__square_size = board_size / 8
        self.__screen = pg.display.set_mode([500, 500])
        super().__init__(left, top, board_size, board_size)

    def __initialise(self):
        pg.display.init()
        pg.font.init()
        pg.mixer.quit()
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

    def highlight_possible_moves(self, ui_square: UISquare):
        for move in self.board.possible_moves(ui_square.square):
            if not self.board.is_move_leaving_king_in_check(move):
                target_square = next(filter(lambda x: x.square.alg_not == move.dest, self.drawn_squares))
                target_square.change_state(MoveCandidate)
                target_square.candidate_move = move

    def find_clicked_square(self, coordinates) -> UISquare:
        return next(filter(lambda x: x.collidepoint(coordinates), self.drawn_squares), None)

    def get_highlighted_square(self) -> UISquare:
        return next(filter(lambda x: x.has_state(Highlighted), self.drawn_squares))

    def reset_squares_to_default(self) -> NoReturn:
        for square in self.drawn_squares:
            square.change_state(Default)
            square.candidate_move = None

    def manage_left_click(self, coordinates) -> NoReturn:
        clicked_square = self.find_clicked_square(coordinates)
        if clicked_square.has_state(MoveCandidate):
            self.board.move_piece(clicked_square.candidate_move)
            self.turn = color.Color.WHITE if self.turn == color.Color.BLACK else color.Color.BLACK
            self.reset_squares_to_default()
            if self.board.is_king_in_check(self.turn):
                print("YEAH IT IS CHECKED!!!!!!!!!!!!!!!!!")
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
            time.sleep(0.1)
