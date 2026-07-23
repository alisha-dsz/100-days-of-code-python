from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(x = - 280, y = 250)
        self.level = 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", False, font=FONT)
        self.level += 1

    def game_end(self):
        self.goto(0,0)
        self.write("GAME OVER!", False, align = "center", font=FONT)


