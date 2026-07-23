from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time


is_game_on = True
screen = Screen()
screen.setup(width = 800, height = 600)
screen.title("Pong Game")
screen.bgcolor("black")

screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(fun = r_paddle.up, key = "Up")
screen.onkey(fun = r_paddle.down, key = "Down")
screen.onkey(fun = l_paddle.up, key = "w")
screen.onkey(fun = l_paddle.down, key = "s")

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 60 and ball.xcor() > 320 or ball.distance(l_paddle) < 60 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 410:
        ball.reset_game()
        score.l_point()

    if ball.xcor() < -410:
        ball.reset_game()
        score.r_point()

screen.exitonclick()