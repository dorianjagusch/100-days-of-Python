from turtle import Turtle
from paddle import LEFT, RIGHT


ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")


class ScoreBoard(Turtle):

    def __init__(self, side):
        super().__init__()
        self.side = side
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = -1
        self.setposition((100 - 2 * self.side * 100, 200))
        self.update()

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

