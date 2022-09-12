from tkinter import *
from quiz_brain import QuizBrain

THEM_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizUi:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.windows = Tk()
        self.windows.title(string="Quiz Game")
        self.windows.config(background=THEM_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150, 125, text="the text here", width=250, font=FONT, fill=THEM_COLOR
        )
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        # Label
        self.score = Label(text="score: 0", fg="white", background=THEM_COLOR, padx=20, pady=20, font=("Arial", 13,))
        self.score.grid(column=1, row=0)

        # Buttons
        true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_button)
        self.true_button.grid(column=0, row=2, padx=20, pady=20)

        false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_button)
        self.false_button.grid(column=1, row=2, padx=20, pady=20)

        self.get_next_question()
        self.windows.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()

        self.canvas.itemconfig(self.question_text, text=q_text)

    def true_button(self):
        self.quiz.check_answer(answer="True")
        if self.quiz.still_have_questions():
            self.get_next_question()

    def false_button(self):
        self.quiz.check_answer(answer="False")
        if self.quiz.still_have_questions():
            self.get_next_question()