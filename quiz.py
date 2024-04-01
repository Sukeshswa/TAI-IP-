import tkinter as tk
import random
import time

class Question:
    def __init__(self, prompt, choices, answer):
        self.prompt = prompt
        self.choices = choices
        self.answer = answer

questions = [
    Question("Who is the father of computer?", ["john", "michael", "charles Babbage"], "charles Babbage"),
    Question("Which company invented smart phone?", ["microsoft", "IBM", "Google"], "IBM"),
    Question("What is the capital of France?", ["London", "Paris", "Madrid"], "Paris"),
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.score = 0
        self.current_question = None
        self.timer = None
        self.question_label = tk.Label(root, text="")
        self.choice_buttons = []
        self.score_label = tk.Label(root, text="Score: 0")
        self.start_button = tk.Button(root, text="Start", command=self.start_quiz)
        self.pause_button = tk.Button(root, text="Pause", state=tk.DISABLED, command=self.pause_quiz)
        self.restart_button = tk.Button(root, text="Restart", state=tk.DISABLED, command=self.restart_quiz)
        self.question_bank = questions.copy()

    def start_quiz(self):
        self.score = 0
        self.score_label.config(text="Score: {}".format(self.score))
        self.start_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.NORMAL)
        self.restart_button.config(state=tk.DISABLED)
        self.load_question()

    def pause_quiz(self):
        self.pause_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)
        self.restart_button.config(state=tk.NORMAL)
        if self.timer is not None:
            self.root.after_cancel(self.timer)

    def restart_quiz(self):
        self.score = 0
        self.score_label.config(text="Score: {}".format(self.score))
        self.question_bank = questions.copy()
        self.start_quiz()

    def load_question(self):
        if self.question_bank:
            self.current_question = random.choice(self.question_bank)
            self.question_bank.remove(self.current_question)
            self.display_question()
            self.start_timer()
        else:
            self.display_score()

    def display_question(self):
        self.question_label.config(text=self.current_question.prompt)
        for i in range(len(self.current_question.choices)):
            choice_button = tk.Button(self.root, text=self.current_question.choices[i], command=lambda idx=i: self.check_answer(idx))
            choice_button.grid(row=i+1, column=0, pady=5)
            self.choice_buttons.append(choice_button)

    def start_timer(self):
        self.timer = self.root.after(10000, self.display_time_up)

    def display_time_up(self):
        self.root.after_cancel(self.timer)
        self.choice_buttons.clear()
        self.load_question()

    def check_answer(self, idx):
        if self.current_question.choices[idx] == self.current_question.answer:
            self.score += 1
            self.score_label.config(text="Score: {}".format(self.score))
        self.choice_buttons.clear()
        self.load_question()

    def display_score(self):
        self.question_label.config(text="Quiz Finished!")
        self.score_label.config(text="Your Final Score: {}".format(self.score))
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.restart_button.config(state=tk.NORMAL)

def main():
    root = tk.Tk()
    root.title("Quiz App")
    quiz_app = QuizApp(root)
    quiz_app.question_label.grid(row=0, column=0, padx=10, pady=10)
    quiz_app.score_label.grid(row=0, column=1, padx=10, pady=10)
    quiz_app.start_button.grid(row=2, column=0, padx=10, pady=10)
    quiz_app.pause_button.grid(row=2, column=1, padx=10, pady=10)
    quiz_app.restart_button.grid(row=2, column=2, padx=10, pady=10)
    root.mainloop()

if __name__ == "__main__":
    main()
