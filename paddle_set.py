import paddle


def get_set(board):
    return [
        paddle.Paddle(shade="blue", board=board, side="right"),
        paddle.Paddle(shade="red", board=board, side="left")
    ]
