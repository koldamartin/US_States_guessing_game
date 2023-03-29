import turtle
import pandas

screen = turtle.Screen()
screen.title("USA States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

df = pandas.read_csv("50_states.csv")

#def capitalize_words(state):
    #return ' '.join(word.capitalize() for word in state.lower().split())
    #Tuto funkci lze nahradit pomoci title() funkce

def get_coordinates(state):
    # state_data = df[df.state == state]
    # x = int(state_data.x)
    # y = int(state_data.y)
    state_data = df.state == state
    x = int(df.loc[state_data]["x"]) # Locate the value in 'x' column for state input
    y = int(df.loc[state_data]["y"])
    return (x,y)

def place_text():
    text = turtle.Turtle()
    text.hideturtle()
    text.penup()
    text.setpos(get_coordinates(answer_state.title()))
    text.write(arg=f"{answer_state.title()}", font=("Courier", 8, "normal"))

guessed_states = []
correct_answers = 0
game_on = True

while game_on:
    answer_state = screen.textinput(title=f"{correct_answers}/50 States Correct", prompt="What's another state's name?")
    if answer_state.title() in df.values and answer_state.title() not in guessed_states:
        place_text()
        guessed_states.append(answer_state.title())
        correct_answers += 1
        if correct_answers == 50:
            game_on = False
    elif answer_state == "Exit":
        break

# Print States that were not guessed into csv
all_states = df.state.tolist()
missing_states = [state for state in all_states if state not in guessed_states]
new_df = pandas.DataFrame(missing_states, columns=["States to learn"])
new_df.to_csv("states_to_learn.csv", index=False)


