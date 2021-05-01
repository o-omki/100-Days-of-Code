from turtle import Turtle, Screen

kiddo = Turtle()
screen = Screen()


def move_fd():
    kiddo.fd(10)

def move_bk():
    kiddo.bk(10)

def turn_left():
    kiddo.setheading(kiddo.heading() + 10)

def turn_right():
    kiddo.rt(10)

def clear():
    kiddo.clear()
    kiddo.pu()
    kiddo.home()
    kiddo.pd()

screen.listen()  
screen.onkey(key = "w", fun = move_fd)
screen.onkey(key = "s", fun = move_bk)
screen.onkey(key = "a", fun = turn_left)
screen.onkey(key = "d", fun = turn_right)
screen.onkey(clear, 'c')




screen.exitonclick() 