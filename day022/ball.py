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
        self.speed_mult = 0.5
        self.x_step = UNIT_SIZE * self.speed_mult
        self.y_step = UNIT_SIZE * self.speed_mult
        self.n_bounces = 0
        self.spawn()

    def spawn(self):
        self.x_step *= -1
        self.goto(0, 0)

    def move(self):
        x = self.xcor() + self.x_step
        y = self.ycor() + self.y_step
        self.goto((x, y))

    def check_collisions(self, colliders):
        for collider in colliders:
            if collider.collide(self):
                return collider

    def side_bounce(self):
        self.n_bounces += 1
        self.x_step *= -1
        if self.n_bounces > 5:
            self.speed_mult += 0.05

    def top_bounce(self):
        self.y_step *= -1


