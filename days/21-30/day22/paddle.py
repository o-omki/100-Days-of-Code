from turtle import Turtle 

class Paddle(Turtle):
    def __init__(self, paddle_postion):
        super().__init__()
        self.x_cord = paddle_postion[0]
        self.y_cord = paddle_postion[1]
        self.create_paddle()
        
    def create_paddle(self):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len = 1, stretch_wid = 5)
        self.pu()
        self.goto(self.x_cord, self.y_cord)

    def paddle_up(self):
        y_shift = self.ycor() + 40
        self.goto(self.xcor(), y_shift)

    def paddle_down(self):
        y_shift = self.ycor() - 40
        self.goto(self.xcor(), y_shift)