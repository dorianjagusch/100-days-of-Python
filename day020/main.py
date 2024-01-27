from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("I'm a sneeeek")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()
game_ongoing = True

screen.listen()
screen.onkey(key='Up', fun=snake.turn_north)
screen.onkey(key='Left', fun=snake.turn_west)
screen.onkey(key='Down', fun=snake.turn_south)
screen.onkey(key='Right', fun=snake.turn_east)

while game_ongoing:
    screen.update()
    sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.update()

    if snake.head.xcor() < -380 or snake.head.xcor() > 380 or snake.head.ycor() < -380 or snake.head.ycor() > 380:
        game_ongoing = False
        score_board.end_game()

    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 15:
            game_ongoing = False
            score_board.end_game()

screen.exitonclick()
