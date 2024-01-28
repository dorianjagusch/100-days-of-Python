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
        self.highscore = self.get_highscore()
        self.goto(x=0, y=350)
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.update()

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}",
                   align=ALIGNMENT,
                   font=FONT
                   )

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.set_highscore()
        self.score = -1
        self.update()

    def get_highscore(self):
        with open("data.txt", "r") as f:
            return int(f.read())

    def set_highscore(self):
        with open("data.txt", "w") as f:
            f.write(f"{self.highscore}")