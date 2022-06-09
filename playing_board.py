from turtle import Turtle
import constants


def prepare_board(board):
    board.screensize(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
    board.setup(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
    board.bgcolor(constants.SCREEN_BACKGROUND_COLOR)


def key_bindings(board, paddles):
    board.listen()
    board.onkeypress(paddles[0].up, "Up")
    board.onkeypress(paddles[0].down, "Down")
    board.onkeypress(paddles[1].up, "w")
    board.onkeypress(paddles[1].down, "z")


def top_of_playing_area():
    return get_lines()["top"] - constants.BORDER_OFFSET


def bottom_of_playing_area():
    return get_lines()["bottom"] + constants.BORDER_OFFSET


def get_lines():
    return {
        "middle": constants.MIDDLE,
        "bottom": constants.SCREEN_HEIGHT / (-2) + constants.BORDER_OFFSET,
        "top": constants.SCREEN_HEIGHT / 2 - constants.BORDER_OFFSET,
        "left": constants.SCREEN_WIDTH / (-2) + constants.BORDER_OFFSET,
        "right": constants.SCREEN_WIDTH / 2 - constants.BORDER_OFFSET
    }


def get_points(lines):
    return {
        "middle_bottom": (lines["middle"], lines["bottom"]),
        "middle_top": (lines["middle"], lines["top"]),
        "left_top": (lines["left"], lines["top"]),
        "left_bottom": (lines["left"], lines["bottom"]),
        "right_bottom": (lines["right"], lines["bottom"]),
        "right_top": (lines["right"], lines["top"]),
    }


def traverse_marked_lines(points, turtle):
    turtle.goto(points["middle_top"])
    turtle.goto(points["left_top"])
    turtle.goto(points["left_bottom"])
    turtle.goto(points["right_bottom"])
    turtle.goto(points["right_top"])
    turtle.goto(points["middle_top"])


def get_border_turtle(points):
    t = Turtle()
    t.hideturtle()
    t.penup()
    t.goto(points["middle_bottom"])
    t.color(constants.LINE_COLOR)
    t.pendown()
    t.pensize(constants.PENSIZE)
    return t


def mark_board():
    lines = get_lines()
    points = get_points(lines)
    turtle = get_border_turtle(points)
    traverse_marked_lines(points, turtle)
