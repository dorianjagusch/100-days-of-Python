from turtle import Turtle

PADDLE_SIZE = 5
UNIT_SIZE = 30
LEFT = 1
RIGHT = 0


class Paddle(Turtle):

    def __init__(self, side):
        super().__init__()
        self.side = side
        self.x_step = UNIT_SIZE
        self.y_step = UNIT_SIZE
        self.create_self()

    def create_self(self):
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(((1 - 2 * self.side) * 350, 0))
        self.shapesize(stretch_wid=5, stretch_len = 1)

    def up(self):
        if self.ycor() > 250:
            return
        self.setposition(x=self.xcor(), y=self.ycor() + UNIT_SIZE)

    def down(self):
        if self.ycor() < -250:
            return
        self.setposition(x=self.xcor(), y=self.ycor() - UNIT_SIZE)

    def collide(self, ball):
        if self.distance(ball) < 50 and (ball.xcor() > 320 or ball.xcor() < -320):
            return True
        return False
