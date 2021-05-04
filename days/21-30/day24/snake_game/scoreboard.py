from turtle import Turtle

FONT = ("Courier", 15, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        
        self.pu()
        self.color("white")
        self.goto(0, 270)
        self.read_highscore()
        self.write(f"Score: {self.score} \tHigh Score: {self.highscore}", align = ALIGNMENT, font= FONT)
        self.hideturtle()
    
    def update_scoreboard(self): 
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} \tHigh Score: {self.highscore}", align = ALIGNMENT, font= FONT) 
        self.update_highscore()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align = ALIGNMENT, font = FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()

    def read_highscore(self):
        with open(r"days\21-30\day24\snake_game\data.txt") as file:
            self.highscore = int(file.read())

    def update_highscore(self):
        with open(r"days\21-30\day24\snake_game\data.txt", 'w') as file:
            file.write(str(self.highscore))