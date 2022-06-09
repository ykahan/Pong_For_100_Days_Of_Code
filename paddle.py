import turtle
import constants
import playing_board
import scoreboard


def half_of_paddle_length():
    return constants.PADDLE_LENGTH / 2


class Paddle(turtle.Turtle):
    def __init__(self, shade, board, side):
        super().__init__()
        self.side = side
        self.screen = board
        self.shape("square")
        self.color(shade)
        self.penup()
        self.resizemode("user")
        self.shapesize(stretch_wid=0.5, stretch_len=3)
        self.ycoordinate = constants.MIDDLE
        self.speed("fastest")
        if self.side == "right":
            self.xcoordinate = playing_board.get_lines()["right"] - constants.BORDER_OFFSET
        else:
            self.xcoordinate = playing_board.get_lines()["left"] + constants.BORDER_OFFSET

        self.scoreboard = scoreboard.Scoreboard(self.side)
        self.goto(self.xcoordinate, self.ycoordinate)
        self.setheading(constants.UP)


    def top_of_paddle(self):
        return self.ycoordinate + half_of_paddle_length()


    def bottom_of_paddle(self):
        return self.ycoordinate - half_of_paddle_length()


    def up(self):
        if self.top_of_paddle() < playing_board.top_of_playing_area():
            self.forward(constants.SPEED_OF_PADDLE_MOVEMENT)
            self.ycoordinate += constants.SPEED_OF_PADDLE_MOVEMENT


    def down(self):
        if self.bottom_of_paddle() > playing_board.bottom_of_playing_area():
            self.backward(constants.SPEED_OF_PADDLE_MOVEMENT)
            self.ycoordinate -= constants.SPEED_OF_PADDLE_MOVEMENT


    def left_of_paddle(self):
        return self.xcoordinate - (constants.PADDLE_WIDTH / 2)


    def right_of_paddle(self):
        return self.xcoordinate + (constants.PADDLE_WIDTH / 2)
