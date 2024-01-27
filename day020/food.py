from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.color("red")
        self.shapesize(stretch_wid=.5, stretch_len=0.5)
        self.refresh()

    def refresh(self):
        x = random.randint(-370, 370)
        y = random.randint(-370, 370)
        self.goto(x, y)
