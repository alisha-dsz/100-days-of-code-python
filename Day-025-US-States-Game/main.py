import turtle
import pandas as pd

screen = turtle.Screen()
screen.setup(width = 725, height = 491)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Correct State",
                                    prompt="What's another states name?").title()
    if answer_state == "Exit":
        if all_states not in guessed_states:
            df = pd.DataFrame(all_states)
            df.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(x = state_data.x.item(), y = state_data.y.item())
            t.write(answer_state)
            all_states.remove(answer_state)

