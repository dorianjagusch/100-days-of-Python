import turtle
import pandas as p


screen = turtle.Screen()
screen.title("State the Name is the Game")
us_map = "blank_states_img.gif"
screen.addshape(us_map)

bg = turtle.Turtle(shape=us_map)

guessed_states = []
state_data = p.read_csv("50_states.csv")
all_states = state_data.state.to_list()

while len(guessed_states) < 50:
    user_answer = screen.textinput(title=f"{len(guessed_states)}/50 States guessed", prompt="Guess a state:").title()

    if user_answer.lower() == "exit":
        break
    if user_answer in all_states and user_answer not in guessed_states:
        guessed_states.append(user_answer)
        found_state = state_data[state_data.state == user_answer]
        state_name = turtle.Turtle()
        state_name.color("black")
        state_name.penup()
        state_name.hideturtle()
        state_name.goto(int(found_state.x), int(found_state.y))
        state_name.write(f"{user_answer}")


to_learn = (state for state in all_states if state not in guessed_states)
states_to_learn = p.DataFrame({"state": to_learn})
states_to_learn.to_csv("states_to_learn.csv")



