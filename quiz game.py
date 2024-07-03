import tkinter as tk
from tkinter import messagebox
import random

# Sample questions for the quiz
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "choices": ["Harper Lee", "Mark Twain", "Ernest Hemingway", "F. Scott Fitzgerald"],
        "answer": "Harper Lee"
    },
    {
        "question": "What is the chemical symbol for water?",
        "choices": ["O2", "H2O", "CO2", "HO"],
        "answer": "H2O"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "choices": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Jupiter"
    },
    {
        "question": "What is the smallest prime number?",
        "choices": ["1", "2", "3", "5"],
        "answer": "2"
    },
    {
        "question": "What is the speed of light?",
        "choices": ["300,000 km/s", "150,000 km/s", "299,792 km/s", "200,000 km/s"],
        "answer": "299,792 km/s"
    },
    {
        "question": "Which programming language is known as the language of the web?",
        "choices": ["Python", "Java", "C++", "JavaScript"],
        "answer": "JavaScript"
    },
    {
        "question": "Who is the founder of Microsoft?",
        "choices": ["Steve Jobs", "Elon Musk", "Bill Gates", "Mark Zuckerberg"],
        "answer": "Bill Gates"
    },
    {
        "question": "What does 'HTTP' stand for?",
        "choices": ["HyperText Transfer Protocol", "HighText Transfer Protocol", "HyperText Transmission Protocol", "HyperTransfer Text Protocol"],
        "answer": "HyperText Transfer Protocol"
    },
    {
        "question": "What is the main language used for creating web pages?",
        "choices": ["Python", "HTML", "Java", "C#"],
        "answer": "HTML"
    },
    {
        "question": "Which company developed the Android operating system?",
        "choices": ["Apple", "Google", "Microsoft", "Samsung"],
        "answer": "Google"
    },
    {
        "question": "What does 'CPU' stand for?",
        "choices": ["Central Processing Unit", "Central Program Unit", "Computer Personal Unit", "Central Processor Unit"],
        "answer": "Central Processing Unit"
    },
    {
        "question": "Which language is primarily used for iOS development?",
        "choices": ["Java", "Kotlin", "Swift", "C#"],
        "answer": "Swift"
    },
    {
        "question": "Who invented the World Wide Web?",
        "choices": ["Bill Gates", "Tim Berners-Lee", "Steve Jobs", "Larry Page"],
        "answer": "Tim Berners-Lee"
    }
]

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.score = 0
        self.current_question = 0
        self.questions = quiz_questions.copy()
        random.shuffle(self.questions)

        self.create_widgets()
        self.display_welcome_message()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Welcome to the Quiz Game!", font=("Helvetica", 16))
        self.title_label.pack(pady=20)

        self.rules_label = tk.Label(self.root, text="You will be asked multiple-choice questions on various topics.\nFor each question, select the correct answer and press Submit.", font=("Helvetica", 12))
        self.rules_label.pack(pady=10)

        self.question_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.question_label.pack(pady=20)

        self.choice_var = tk.StringVar()
        self.choices_frame = tk.Frame(self.root)
        self.choices_frame.pack(pady=10)

        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(self.choices_frame, text="", variable=self.choice_var, value="", font=("Helvetica", 12))
            rb.pack(anchor="w")
            self.radio_buttons.append(rb)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer, font=("Helvetica", 12))
        self.submit_button.pack(pady=20)

        self.feedback_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.feedback_label.pack(pady=10)

    def display_welcome_message(self):
        self.current_question = 0
        self.score = 0
        self.title_label.config(text="Welcome to the Quiz Game!")
        self.rules_label.config(text="You will be asked multiple-choice questions on various topics.\nFor each question, select the correct answer and press Submit.")
        self.display_next_question()

    def display_next_question(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.question_label.config(text=question["question"])
            self.choice_var.set("")
            for i, choice in enumerate(question["choices"]):
                self.radio_buttons[i].config(text=choice, value=choice)
            self.feedback_label.config(text="")
        else:
            self.display_final_results()

    def check_answer(self):
        selected_answer = self.choice_var.get()
        correct_answer = self.questions[self.current_question]["answer"]

        if selected_answer == correct_answer:
            self.feedback_label.config(text="Correct!", fg="green")
            self.score += 1
        else:
            self.feedback_label.config(text=f"Incorrect. The correct answer is {correct_answer}.", fg="red")

        self.current_question += 1
        self.root.after(2000, self.display_next_question)  # Wait 2 seconds before displaying the next question

    def display_final_results(self):
        self.title_label.config(text="Quiz Completed!")
        self.rules_label.config(text="")
        self.question_label.config(text="")
        self.choices_frame.pack_forget()
        self.submit_button.pack_forget()

        performance = (self.score / len(self.questions)) * 100
        performance_message = ""
        if performance == 100:
            performance_message = "Perfect score! Excellent job!"
        elif performance >= 80:
            performance_message = "Great job! You have a strong grasp of the material."
        elif performance >= 50:
            performance_message = "Good effort! Keep studying and you'll improve."
        else:
            performance_message = "Keep practicing! You'll get better with more practice."

        self.feedback_label.config(text=f"Your final score is {self.score} out of {len(self.questions)}.\n{performance_message}", fg="blue")

        play_again_button = tk.Button(self.root, text="Play Again", command=self.play_again, font=("Helvetica", 12))
        play_again_button.pack(pady=20)

    def play_again(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.__init__(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    game = QuizGame(root)
    root.mainloop()
