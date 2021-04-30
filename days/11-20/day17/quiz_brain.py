class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list 
    
    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {question.text} (True /  False)?: ").strip()
        self._check_answer(user_answer, question.answer)
        
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def _check_answer(self,  user_answer, actual_answer):
        if user_answer.lower() == actual_answer.lower():
            print("You've got it right!")
            self.score += 1
        else:
            print("That's wrong.")
            print(f"The correct answer was: {actual_answer}")
        print(f"Your current score: {self.score} / {self.question_number}\n")
        