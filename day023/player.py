from turtle import Turtle

STARTING_POS = (0, -280)
STEP_SIZE = 20


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POS)
        self.setheading(90)

    def move_up(self):
        self.goto((0, self.ycor() + STEP_SIZE))

    def reset(self):
        self.goto(STARTING_POS)
