from ui.uiboard import *
from chessboard.board import *

chess_board = ChessBoard()
ui_board = UIBoard(30, 30, 400, chess_board)
ui_board.start()
