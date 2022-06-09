import random
from turtle import Turtle
import constants
import playing_board

class Ball(Turtle):
    def __init__(self, right_paddle, left_paddle):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.forward_speed = constants.BALL_SPEED
        self.speed("fastest")
        self.direction = None
        self.set_random_heading()
        game_continue = True
        while game_continue:
            self.move(right_paddle, left_paddle)
            if right_paddle.scoreboard.get_score() == constants.WINNING_SCORE:
                game_continue = False
            if left_paddle.scoreboard.get_score() == constants.WINNING_SCORE:
                game_continue = False


    def set_random_heading(self):
        self.pick_angle()
        self.pick_direction()
        self.setheading(self.angle)


    def pick_angle(self):
        self.angle = random.randint(constants.BALL_ANGLE_LOWER_NUMBER, constants.BALL_ANGLE_HIGHER_NUMBER)
        if self.angle == 180:
            self.pick_angle()


    def pick_direction(self):
        self.direction = random.choice(["right", "left"])
        if self.direction == "right":
            self.angle += 180


    def respawn(self):
        self.hideturtle()
        self.goto(constants.MIDDLE, constants.MIDDLE)
        self.showturtle()
        self.set_random_heading()


    def offscreen_right(self):
        return self.left_of_ball() >= constants.SCREEN_RIGHT_BORDER


    def offscreen_left(self):
        return self.right_of_ball() <= constants.SCREEN_LEFT_BORDER


    def move(self, right_paddle, left_paddle):
        self.forward(self.forward_speed)
        self.bounce(right_paddle, left_paddle)
        self.go_offscreen(right_paddle, left_paddle)


    def go_offscreen(self, right_paddle, left_paddle):
        if self.offscreen_right():
            right_paddle.scoreboard.increment_score()
            self.respawn()
        elif self.offscreen_left():
            left_paddle.scoreboard.increment_score()
            self.respawn()


    def bounce(self, right_paddle, left_paddle):
        change = 0
        if self.hit_top_boundary():
            change = constants.UP - self.angle
        elif self.hit_bottom_boundary():
            change = constants.DOWN - self.angle
        elif self.hit_right_paddle(right_paddle):
            change = constants.RIGHT - self.angle
        elif self.hit_left_paddle(left_paddle):
            change = constants.LEFT - self.angle
        self.change_heading(change)


    def change_heading(self, change):
        if change != 0:
            self.angle += 180
            self.angle += change + change
            self.setheading(self.angle)


    def hit_top_boundary(self):
        return self.top_of_ball() >= playing_board.get_lines()["top"]


    def hit_bottom_boundary(self):
        return self.bottom_of_ball() <= playing_board.get_lines()["bottom"]


    def hit_right_paddle(self, right_paddle):
        if self.right_of_ball() >= right_paddle.left_of_paddle():
            if right_paddle.bottom_of_paddle() <= self.top_of_ball() \
                    and self.bottom_of_ball() <= right_paddle.top_of_paddle():
                if self.direction == "right":
                    self.direction = "left"
                    return True


    def hit_left_paddle(self, left_paddle):
        if self.left_of_ball() <= left_paddle.right_of_paddle():
            if left_paddle.bottom_of_paddle() <= self.top_of_ball() \
                    and self.bottom_of_ball() <= left_paddle.top_of_paddle():
                if self.direction == "left":
                    self.direction = "right"
                    return True


    def bottom_of_ball(self):
        return self.ycor() - constants.BALL_RADIUS


    def top_of_ball(self):
        return self.ycor() + constants.BALL_RADIUS


    def right_of_ball(self):
        return self.xcor() + constants.BALL_RADIUS


    def left_of_ball(self):
        return self.xcor() - constants.BALL_RADIUS
