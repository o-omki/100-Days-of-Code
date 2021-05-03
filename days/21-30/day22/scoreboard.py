from turtle import Turtle 

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()

        self.left_score = 0
        self.right_score = 0

        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-180, 200)
        self.write(self.left_score, align = ALIGNMENT, font = FONT)
        self.goto(180, 200)
        self.write(self.right_score, align = ALIGNMENT, font = FONT)

    def update_left_score(self):
        self.left_score += 1
        self.update_scoreboard()

    def update_right_scoreboard(self):
        self.right_score += 1
        self.update_scoreboard()