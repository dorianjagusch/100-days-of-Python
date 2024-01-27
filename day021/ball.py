from turtle import Turtle
from paddle import UNIT_SIZE
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=0.6, stretch_len=0.6)
        self.spawn()

    def spawn(self):
        self.speed("fastest")
        self.goto(0,0)
        self.speed(2)
        angle = random.randint(0, 360)
        while 80 < angle < 100 or 260 < angle < 280:
            angle = random.randint(0, 360)
        self.setheading(angle)

    def move(self):
        self.forward(UNIT_SIZE)

    def check_collisions(self, colliders):
        for collider in colliders:
            if collider.collide(self):
                return collider

    def reflect_horizontal(self):
        if self.heading() < 180:
            new_angle = 360 - self.heading()
        else:
            new_angle = 180 - self.heading()
        self.setheading(new_angle)

    def reflect_vertical(self):
        self.setheading(180 - self.heading())
