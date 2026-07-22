import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = t.Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")

screen.tracer(0)

score = ScoreBoard()
snake = Snake()
food = Food()

screen.listen()

screen.onkey(fun = snake.up, key = "Up")
screen.onkey(fun = snake.down, key = "Down")
screen.onkey(fun = snake.right, key = "Right")
screen.onkey(fun = snake.left, key = "Left")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    if snake.head.distance(food) < 15:
        score.increase_score()
        snake.extend()
        food.refresh()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        score.game_over()

    for segment in snake.segments[1:]:
        # if snake.head.distance(segment) == 0:
        #     pass
        if snake.head.distance(segment) < 10:
            is_game_on = False
            score.game_over()

screen.exitonclick()





