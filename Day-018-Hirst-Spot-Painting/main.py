# import colorgram as c
#
# colors = c.extract("spot-painting.jpg", 20)

# color_list = []

# for index in range(20):
#     color_item = colors[index]
#     rgb = color_item.rgb
#     red = rgb.r
#     green = rgb.g
#     blue = rgb.b
#     color_tuple = (red, green, blue)
#     color_list.append(color_tuple)
#
# print(color_list)

import turtle as t
import random

tim = t.Turtle()
tim.speed(50)
tim.hideturtle()
t.colormode(255)

color_list = [(236, 35, 108), (221, 231, 237), (145, 28, 66), (230, 237, 232), (239, 75, 35), (7, 148, 95), (220, 171, 45), (183, 158, 47), (45, 191, 232), (28, 127, 194), (254, 223, 0), (125, 192, 78), (85, 27, 91), (243, 218, 56), (178, 40, 98), (44, 170, 114), (211, 132, 166), (206, 57, 35)]

def random_color():
    rgb_color = random.choice(color_list)
    return rgb_color


tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)

number_of_dots = 100

for dots in range(1, number_of_dots + 1):
    tim.dot(20, random_color())
    tim.penup()
    tim.forward(50)

    if dots % 10 == 0:
        tim.setheading(90)
        tim.penup()
        tim.forward(50)
        tim.setheading(180)
        tim.penup()
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()