from tkinter import *
from PIL import ImageTk, Image
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.root = Tk()
        self.root.title("Quizzler")
        self.root.config(padx=20, pady=20, background=THEME_COLOR)
        # CANVAS
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.text_canvas = self.canvas.create_text(150, 125, text="", width=280, font=("Arial", 20, "italic"))
        # LABEL
        self.score_label = Label(text="Score: 0", background=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1, pady=20)
        # IMG BUTTONS
        self.img_correct = ImageTk.PhotoImage(Image.open("./images/true.png"))
        self.img_incorrect = ImageTk.PhotoImage(Image.open("./images/false.png"))
        # BUTTONS
        self.correct_button = Button(image=self.img_correct, highlightthickness=0, borderwidth=0,
                                     command=self.true_pressed)
        self.correct_button.grid(row=2, column=0, pady=30)

        self.incorrect_button = Button(image=self.img_incorrect, highlightthickness=0, borderwidth=0,
                                       command=self.false_pressed)
        self.incorrect_button.grid(row=2, column=1)
        # NEXT QUESTION
        self.get_next_question()

        self.root.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.text_canvas, text=q_text)
            self.canvas.config(bg="white")
        else:
            self.canvas.itemconfig(self.text_canvas, text="You've reached the end of the quiz")
            self.canvas.config(bg="white")
            self.correct_button["state"] = "disabled"
            self.incorrect_button["state"] = "disabled"

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.root.after(1000, self.get_next_question)
