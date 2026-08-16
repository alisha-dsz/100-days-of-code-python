from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain : QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score : 0", fg="white", bg=THEME_COLOR, font=("Arial", 15, "bold"))
        self.score.grid(row=0, column=1, pady=(3,0))

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.green_canvas = Canvas(width=300, height=250, bg="green", highlightthickness=0)
        self.red_canvas = Canvas(width=300, height=250, bg="red", highlightthickness=0)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="Question",
                                                     font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_image,command=self.true_answer)
        self.true_button.grid(row=2, column=0,  pady=(0,5))

        self.false_image = PhotoImage(file="images/false.png")
        self.false_button=Button(image=self.false_image, command=self.false_answer)
        self.false_button.grid(row=2, column=1, pady=(0,5))

        self.generate_new_question()

        self.window.mainloop()

    def generate_new_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score.config(text=f"Score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text )
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.canvas.config(bg="white")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_answer(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.generate_new_question)