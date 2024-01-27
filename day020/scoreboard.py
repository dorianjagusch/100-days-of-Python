from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(x=0, y=350)
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.update()

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}",
                   align=ALIGNMENT,
                   font=FONT
                   )

    def end_game(self):
        self.goto(0, 0)
        self.write(f"GAME OVER",
                   align=ALIGNMENT,
                   font=FONT
                   )