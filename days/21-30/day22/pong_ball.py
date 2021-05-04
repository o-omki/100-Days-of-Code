from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.pu()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1 
    
    def move_ball(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def y_bounce(self):
        self.y_move *= -1
        self.ball_speed * 0.9

    def x_bounce(self):
        self.x_move *= -1
        self.ball_speed *= 0.9
    
    def reset_position(self):
        self.ball_speed = 0.1
        self.goto(0, 0)
        self.x_bounce()