import turtle
import pandas

# Get coordinates from mouse
# def get_mouse_click_coor(x, y):
# print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

screen = turtle.Screen()
screen.title("Argentina Guess Game")
turtle.setup(1920,1080)
image = "mapa2.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("23_provincias2.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 24:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/24 provincias correctas",
                                    prompt="Introduce el nombre de una provincia").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("provincias_por_aprender.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)



