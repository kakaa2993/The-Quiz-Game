import html


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.current_question = None

    def still_have_questions(self) -> bool:
        return len(self.question_list) > self.question_number

    def next_question(self) -> str:
        self.current_question = self.question_list[self.question_number]
        current_text_question = html.unescape(self.current_question.text)
        self.question_number += 1
        return f"Q.{self.question_number}: {current_text_question}"

    def check_answer(self, answer):
        correct_answer = self.question_list[self.question_number]["correct_answer"]
        print(correct_answer)
        if answer == correct_answer:
            # "You are right!"
            self.score += 1
            return True
        else:
            # "That's wrong!"
            return False

