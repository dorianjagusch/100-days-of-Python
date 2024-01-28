from turtle import Turtle
import random

COLOURS = ["red", "orange", "yellow", "green", "blue", "purple"]
BASE_SPEED = 10
SPEED_INC = 3


class Car(Turtle):

    def __init__(self, speed):
        super().__init__()
        self.color(random.choice(COLOURS))
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.y_pos = random.randint(-200, 200)
        self.goto((320, self.y_pos))
        self.speed = speed
        self.setheading(180)

    def hit_wall(self):
        self.color(random.choice(COLOURS))
        self.goto((320, random.randint(-200, 200)))

    def increase_speed(self):
        self.speed += SPEED_INC

    def move(self):
        self.goto((self.xcor() - self.speed, self.y_pos))


class CarManager:

    def __init__(self):
        self.cars = []
        self.speed = BASE_SPEED
        self.spawn_cars()

    def spawn_cars(self):
        for _ in range(20):
            if random.random() < 0.01:
                self.cars.append(Car(self.speed))

    def increase_speed(self):
        self.speed += SPEED_INC
        for car in self.cars:
            car.increase_speed()

    def move_cars(self):
        for car in self.cars:
            car.move()

    def check_collision(self, player):
        for car in self.cars:
            if car.distance(player) < 20 and car.ycor() - 20 <= player.ycor() <= car.ycor() + 20:
                return True
        return False

    def reset(self):
        for car in self.cars:
            car.goto(400, 400)
        self.cars.clear()
