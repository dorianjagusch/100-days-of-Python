from turtle import Turtle

STEP_SIZE = 20
EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270


class Snake:

    def __init__(self):
        self.body = []
        self.initialise_snake()
        self.head = self.body[0]

    def initialise_snake(self):
        for i in range(3):
            self.add_seg((0, i * STEP_SIZE))

    def add_seg(self, position):
        seg = Turtle(shape="square")
        seg.color("white")
        seg.penup()
        seg.setposition(position)
        self.body.append(seg)

    def extend(self):
        self.add_seg(self.body[-1].position())

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            ahead_pos = self.body[i - 1].position()
            self.body[i].goto((ahead_pos[0], ahead_pos[1]))
        self.head.forward(STEP_SIZE)

    def turn_east(self):
        if self.head.heading() != WEST:
            self.head.seth(EAST)

    def turn_north(self):
        if self.head.heading() != SOUTH:
            self.head.seth(NORTH)

    def turn_west(self):
        if self.head.heading() != EAST:
            self.head.seth(WEST)

    def turn_south(self):
        if self.head.heading() != NORTH:
            self.head.seth(SOUTH)

    def reset(self):
        for segment in self.body:
            segment.goto(1000, 1000)
        self.body.clear()
        self.initialise_snake()
        self.head = self.body[0]
