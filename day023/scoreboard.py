from turtle import Turtle

FONT = ("Courier", 20, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        with open("data.txt", "r") as file:
            self.highscore = int(file.read())
        self.hideturtle()
        self.color("black")
        self.setposition(0, 260)
        self.level = -1
        self.update()

    def update(self):
        self.clear()
        self.level += 1
        if self.level > self.highscore:
            self.highscore = self.level
        self.write(f"Level: {self.level}       Highscore: {self.highscore}", align="center", font=FONT)

    def reset(self):
        self.save_highscore()
        self.level = -1
        self.update()

    def save_highscore(self):
        with open("data.txt", "w") as file:
            file.write(f"{self.highscore}")
