from turtle import Turtle

FORWARD = 20

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("deep pink")

    def up(self):
        new_y = self.ycor() + 20
        self.goto(x = self.xcor(), y = new_y)


    def down(self):
        new_y = self.ycor() - 20
        self.goto(x = self.xcor(), y = new_y)
