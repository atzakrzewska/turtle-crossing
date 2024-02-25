from turtle import Turtle

FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.level = 1
        self.update()

    def update(self):
        self.goto(x=-270, y=250)
        self.write(f"Level {self.level}", False, "left", FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", False, "center", FONT)
