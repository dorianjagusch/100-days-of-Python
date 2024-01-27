import turtle as t
import random

turtle_colours = ["red", "orange", "yellow", "green", "blue", "purple"]

colour_str = '/'.join(turtle_colours)

screen = t.Screen()
screen.setup(width=800, height=600)
race_ongoing = False

user_bet = ""
while user_bet not in turtle_colours:
    user_bet = screen.textinput(title="Make your bet",
                                prompt="Which turtle do you think will emerge victorious? \n"
                                       f"Enter {colour_str}:").lower()

turtles = []
Y_OFFSET = screen.canvheight // len(turtle_colours)

for i, colour in enumerate(turtle_colours):
    turtles.append(t.Turtle(shape="turtle"))
    turtles[i].color(colour)
    turtles[i].penup()
    y_coord = Y_OFFSET - screen.canvheight + i * (2 * screen.canvheight // len(turtle_colours))
    turtles[i].goto(-screen.canvwidth + 20, y_coord)

if user_bet:
    race_ongoing = True

winner = ""

while race_ongoing:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))

    for turtle in turtles:
        if turtle.xcor() > screen.canvwidth - 20:
            winner = turtle.pencolor()
            race_ongoing = False


print(f"The {winner} turtle won!")
state = ""
if winner == user_bet:
    state = "correct"
else:
    state = "incorrect"
print(f"Your bet was {state} ")

screen.exitonclick()
