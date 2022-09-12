
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizUi

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
# print(question_bank)
quiz = QuizBrain(question_bank)
QuizUi = QuizUi(quiz)

# while quiz.still_have_questions():
#     quiz.next_question()
print("You have completed the Quiz!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")