from turtle import Turtle, Screen 
import random 

screen = Screen()
screen.setup(500, 400) 
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a colour").strip()

all_turtles = []
turtle_colours = ["coral", "blue", "grey", "purple", "green"]
x_cord = -237
y_cord = 100
for colour in turtle_colours:
    turt_clr = colour
    colour = Turtle(shape = "turtle")
    colour.color(turt_clr)
    colour.penup()
    colour.goto(x = x_cord, y = y_cord)
    y_cord -= 50
    all_turtles.append(colour)

game_start = False 
if user_bet: 
    game_start = True

print(turtle_colours)

while game_start: 
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            game_start = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print("Your win")
            else:
                print(f"You lost, {winner} won the race!")
        dist = random.randint(0, 10) 
        turtle.fd(dist)
screen.exitonclick()  