import random
import turtle as t
import colorgram
import turtle as t

DOT_SIZE = 30

t.colormode(255)


def get_colours(image_path):
    image_colours = colorgram.extract(image_path, 30)
    image_colours = image_colours[4:]
    rgb_colours = []
    for colour in image_colours:
        r = colour.rgb.r
        g = colour.rgb.g
        b = colour.rgb.b
        rgb_colours.append((r, g, b))
    return rgb_colours


def draw_hirst(turtle, colours):
    for y in range(-screen.canvheight, int(screen.canvheight * 1.1), 2 * screen.canvheight // 10):
        print(f"y: {y}")
        for x in range(-screen.canvwidth, int(screen.canvwidth * 1.1), 2 * screen.canvwidth // 10):
            print(f"x: {x}")
            turtle.setposition(x, y)
            colour = random.choice(colours)
            turtle.dot(DOT_SIZE, colour)


screen = t.Screen()
tim = t.Turtle()
tim.penup()
tim.hideturtle()
tim.speed("fastest")
pic_colours = get_colours("image.jpg")
draw_hirst(tim, pic_colours)

screen.exitonclick()
