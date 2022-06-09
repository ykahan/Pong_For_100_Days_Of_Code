import paddle_set
import playing_board
from turtle import Screen
import ball


board = Screen()
playing_board.prepare_board(board)
paddles = paddle_set.get_set(board)
playing_board.key_bindings(board, paddles)
playing_board.mark_board()
ball = ball.Ball(right_paddle=paddles[0], left_paddle=paddles[1])
board.exitonclick()

