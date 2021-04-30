from question_model import Question
from question_set import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data: 
    question_text = question["text"]
    question_answer = question["answer"]
    question_bank.append(Question(question_text, question_answer))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz. \nYour final score is: {quiz.score} / {quiz.question_number}")