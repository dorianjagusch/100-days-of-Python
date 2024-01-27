from ball import Ball
from line import Line
from paddle import Paddle, LEFT, RIGHT
from scoreboard import ScoreBoard
from turtle import Screen
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

line = Line()
scoreboard1 = ScoreBoard(LEFT)
scoreboard2 = ScoreBoard(RIGHT)

paddle1 = Paddle(LEFT)
paddle2 = Paddle(RIGHT)

paddles = [paddle1, paddle2]

ball = Ball()

screen.listen()
screen.onkey(key='w', fun=paddle1.up)
screen.onkey(key='s', fun=paddle1.down)
screen.onkey(key='Up', fun=paddle2.up)
screen.onkey(key='Down', fun=paddle2.down)

game_ongoing = True

while game_ongoing:
    screen.update()
    time.sleep(0.1)
    ball.move()

    if ball.check_collisions(paddles):
        ball.reflect_vertical()

    if ball.ycor() < -330 or ball.ycor() > 300:
        ball.reflect_horizontal()

    #TODO: Fix Ball leaving arena

    if ball.xcor() < -380:
        scoreboard1.update()
        ball.spawn()
    elif ball.xcor() > 380:
        scoreboard2.update()
        ball.spawn()

screen.exitonclick()
