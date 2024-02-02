import quiz_brain as qb
from tkinter import *

THEME_COLOR = "#375362"
FONT = "Arial", 20, "italic"


class QuizInterface:

    def __init__(self, quiz_brain: qb.QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiiiiizzzzzzzz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score: ", fg="white", bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.q_text = self.canvas.create_text(150, 125,
                                              text="",
                                              width=280,
                                              fill=THEME_COLOR,
                                              font=FONT)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, command=self.answer_false)

        true_img = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=true_img, command=self.answer_true)
        self.get_next_question()
        self.render()

        self.window.mainloop()

    def render(self):
        self.score_label.grid(row=0, column=1)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.correct_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=q_text)
        else:
            self.canvas.itemconfig(self.q_text, text="You have reached the end of the quiz.\n"
                                                     f"You got {self.quiz.score}/10 points!")
            self.correct_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, result):
        self.canvas.config(bg="green" if result else "red")
        self.window.after(1000, self.get_next_question)
