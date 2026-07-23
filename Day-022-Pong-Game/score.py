from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 40, "bold")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(50, 240)
        self.write(self.r_score, False, align=ALIGN, font=FONT)
        self.goto(-50, 240)
        self.write(self.l_score, False, align=ALIGN, font=FONT)


    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()