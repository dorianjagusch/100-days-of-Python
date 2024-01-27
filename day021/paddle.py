from turtle import Turtle

PADDLE_SIZE = 5
UNIT_SIZE = 20
LEFT = 0
RIGHT = 1


class Paddle(Turtle):

    def __init__(self, side):
        super().__init__()
        self.components = []
        self.side = side
        self.create_paddle()

    def create_paddle(self):
        for i in range(-PADDLE_SIZE // 2 + 1, PADDLE_SIZE // 2 + 1):
            paddle = Turtle("square")
            paddle.color("white")
            paddle.penup()
            if self.side == LEFT:
                print(i - (PADDLE_SIZE // 2))
                paddle.goto(-350, (i * UNIT_SIZE))
            if self.side == RIGHT:
                paddle.goto(350, (i * UNIT_SIZE))
            self.components.append(paddle)

    def up(self):
        for paddle in self.components:
            if paddle.ycor() > 260:
                return
        for paddle in self.components:
            paddle.setposition(x=paddle.xcor(), y=paddle.ycor() + UNIT_SIZE)

    def down(self):
        for paddle in self.components:
            if paddle.ycor() < -260:
                return
        for paddle in self.components:
            paddle.setposition(x=paddle.xcor(), y=paddle.ycor() - UNIT_SIZE)

    def collide(self, ball):
        for component in self.components:
            if component.distance(ball) < 15:
                return True
        return False
