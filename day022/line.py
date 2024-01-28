from turtle import Turtle

DOWN = 270


class Line(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.width(5)
        self.hideturtle()
        self.penup()
        self.setposition(0, 300)
        self.draw_line()

    def draw_line(self):
        self.setheading(DOWN)
        while self.ycor() > -300:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
