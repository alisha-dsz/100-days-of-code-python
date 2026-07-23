import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(fun = player.move_player, key = "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_cars()
    car.move_cars()

    if player.is_at_finish_line():
        player.reset_player()
        score.update_level()

        car.increase_speed()

    for car_item in car.all_cars:
        if car_item.distance(player) < 20:
            game_is_on = False
            score.game_end()


screen.exitonclick()