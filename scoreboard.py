import turtle
import playing_board

import constants


class Scoreboard(turtle.Turtle):
    def __init__(self, right_or_left):
        super().__init__()
        self.hideturtle()
        self.color(constants.SCOREBOARD_COLOR)
        self.penup()
        self.right_or_left = right_or_left
        if self.right_or_left == "right":
            self.goto(
                constants.SCREEN_LEFT_BORDER + (6 * constants.BORDER_OFFSET),
                playing_board.get_lines()["top"] - (3 * constants.BORDER_OFFSET)
            )
        else:
            self.goto(
                constants.SCREEN_RIGHT_BORDER - (6 * constants.BORDER_OFFSET),
                playing_board.get_lines()["top"] - (3 * constants.BORDER_OFFSET)
            )
        self._score = 0
        self.display_score()


    def display_score(self):
        if self.get_score() < constants.WINNING_SCORE:
            self.write(
                f"{self.get_score()}",
                align=constants.ALIGN,
                font=(constants.FONTNAME, constants.FONTSIZE, constants.FONTTYPE)
            )
        else:
            self.write(
                "WINNER",
                align=constants.ALIGN,
                font=(constants.FONTNAME, constants.FONTSIZE, constants.FONTTYPE)
            )


    def increment_score(self):
        self._score += 1
        self.clear()
        self.display_score()
        print(self.get_score())


    def get_score(self):
        return self._score
