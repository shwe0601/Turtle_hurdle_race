from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.current_score()

    def current_score(self):
        self.write(f"Level {self.level} : ", align="left", font=FONT)

    def update(self):
        self.level += 1
        self.clear()
        self.current_score()

    def Game_Over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
