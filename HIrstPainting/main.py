import turtle as t

tim = t.Turtle()

for steps in range(100):
    for c in ('blue', 'red', 'green'):
        tim.color(c)
        tim.forward(steps)
        tim.right(30)

screen = t.Screen()
screen.exitonclick()