import html


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_have_questions(self):
        return len(self.question_list) > self.question_number

    def next_question(self):
        current_question = self.question_list[self.question_number]
        current_text_question = html.unescape(current_question.text)
        self.question_number += 1
        return f"Q.{self.question_number}: {current_text_question}"
        # self.check_answer(answer=answer, correct_answer=current_question.answer)
        # return answer

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("You are right!")
            self.score += 1
        else:
            print("That's wrong!")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
