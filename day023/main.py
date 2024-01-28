import turtle

from car_manager import CarManager, Car
from player import Player
from scoreboard import ScoreBoard
from turtle import Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("grey")
screen.tracer(0)
screen.title("Flatten the turt")

player = Player()
scoreboard = ScoreBoard()
car_manager = CarManager()

screen.listen()
screen.onkey(key="Up", fun=player.move_up)

while True:
    time.sleep(0.1)
    screen.update()

    car_manager.spawn_cars()
    car_manager.move_cars()

    if car_manager.check_collision(player):
        player.reset()
        scoreboard.reset()
        car_manager.reset()

    if player.ycor() >= 280:
        player.reset()
        scoreboard.update()
        car_manager.increase_speed()


screen.exitonclick()
