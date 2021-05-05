import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Games")
state_image = r"days\21-30\day25\US State Game\data\blank_states_img.gif"
screen.addshape(state_image)

turtle.shape(state_image)

data = pandas.read_csv(r"days\21-30\day25\US State Game\data\50_states.csv")
state_list = data.state.to_list()

guessed_states = []
 
while len(guessed_states) < 50:
    user_answer = screen.textinput(title = f"{len(guessed_states)}/50 States Correct", prompt = "Enter the name of the state.").strip().title()
    if user_answer == "Exit":
        missing_states = []
        for state in state_list:
            if state not in guessed_states:
                missing_states.append(state)
        
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv(r"days\21-30\day25\US State Game\data\learn_states.csv")
        break
    if user_answer in state_list:
        guessed_states.append(user_answer)
        turt = turtle.Turtle()
        turt.hideturtle()
        turt.pu()
        state_data = data[data.state == user_answer] 
        turt.goto(int(state_data.x), int(state_data.y))
        turt.write(user_answer)


screen.exitonclick()