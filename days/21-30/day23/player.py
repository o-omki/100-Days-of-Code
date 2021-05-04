from turtle import Turtle

STARTING_POSITION = (0, -280)
FINISH_LINE = 280
MOVE_DISTANCE = 10

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.go_to_start()
        
        
    def move_up(self):
        self.fd(MOVE_DISTANCE)

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE

    def go_to_start(self):
        self.goto(STARTING_POSITION)
         