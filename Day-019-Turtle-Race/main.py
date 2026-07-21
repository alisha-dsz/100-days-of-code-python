import turtle as t
import random

screen = t.Screen()
screen.setup(width = 500, height = 400)

is_race_on = False

user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "pink", "green", "blue", "purple"]

y_positions = [ -70, -40, -10, 20, 50, 80 ]

all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print("Congratulations. You have won the bet.")
            else:
                print(f"You lose. {winning_turtle} has won the race.")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()
