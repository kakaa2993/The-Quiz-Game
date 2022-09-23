from tkinter import *
from quiz_brain import QuizBrain

THEM_COLOR = "#0F3460"
FONT = ("Arial", 20, "italic")
TEXT_COLOR = "#181818"


class QuizUi:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.windows = Tk()
        self.windows.title(string="Quiz Game")
        self.windows.config(background=THEM_COLOR, padx=50)

        self.canvas = Canvas(width=300, height=250, background="white")
        self.question_text = self.canvas.create_text(
            150, 125, text="the text here", width=250, font=FONT, fill=TEXT_COLOR
        )
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        # Label
        self.score = Label(text="score: 0", fg="white", background=THEM_COLOR, padx=20, pady=20, font=("Arial", 13,))
        self.score.grid(column=1, row=0)

        # Buttons
        true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2, padx=20, pady=20)

        false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2, padx=20, pady=20)

        self.get_next_question()
        self.windows.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_have_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text,
                text=f"You've completed the quizzes.\nYour final score is: {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer(answer="True")
        print(is_right)
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer(answer="False")
        print(is_right)
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(background="Green")
        else:
            self.canvas.configure(background="Red")
        self.windows.after(ms=1000, func=self.get_next_question)
