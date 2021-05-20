import tkinter
from tkinter.constants import S
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain ):
        self.quiz = quiz_brain

        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx = 20, pady = 20, bg = THEME_COLOR)

        self.score_label = tkinter.Label(text = "Score: 0", fg = "white", bg = THEME_COLOR)
        self.score_label.grid(row = 0, column = 1)
        self.create_canvas()

        true_image = tkinter.PhotoImage(file = r"days\31-40\day34\quizzler_app\data\images\true.png")
        self.true_button = tkinter.Button(image = true_image, highlightthickness = 0, command = self.true_answer)
        self.true_button.grid(row = 2, column = 0)

        false_image = tkinter.PhotoImage(file = r"days\31-40\day34\quizzler_app\data\images\false.png")
        self.false_button = tkinter.Button(image = false_image, highlightthickness = 0, command = self.false_answer)
        self.false_button.grid(row = 2, column = 1)

        self.next_question() 
        
        self.window.mainloop()

    def create_canvas(self):
        self.canvas = tkinter.Canvas(height = 250, width = 300, bg = "white")
        self.question = self.canvas.create_text(150, 125, text = "abc", font = ("Arial", 20, "italic"), fill = THEME_COLOR, width = 280)
        self.canvas.grid(row = 1, column = 0, columnspan = 2, pady = 50)

    def next_question(self):
        self.canvas.config(bg = "white")
        if self.quiz.still_has_questions():
            self.score_label.config(text = f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text = q_text)
        else:
            self.canvas.itemconfig(self.question, text = "You've reached the end of the quiz")
            self.true_button.config(state = "disabled")
            self.false_button.config(state = "disabled")

    def true_answer(self):
        self.feedback(self.quiz.check_answer("True"))
    
    def false_answer(self):
        self.feedback(self.quiz.check_answer("False"))
    
    def update_score(self): ...

    def feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg = "green")
        else:
            self.canvas.config(bg = "red")

        self.window.after(1000, func = self.next_question)
        
        