import tkinter as tk
from tkinter import messagebox
import random

# Base GUI Helper class
class BaseWindow:
    def labeled_entry(self, container, label_text):
        tk.Label(container, text=label_text, font=("Arial", 12), bg="#f0f0f0").pack(pady=2)
        entry = tk.Entry(container, width=50, font=("Arial", 12))
        entry.pack(pady=2)
        return entry

    def styled_button(self, container, text, command, bg="#4CAF50"):
        return tk.Button(container, text=text, command=command, font=("Arial", 12),
                         bg=bg, fg="white", relief="raised")

    def load_quiz_data(self):
        try:
            with open("quiz_data.txt", "r") as file:
                blocks = file.read().split("-" * 40 + "\n")
            questions = []
            for block in blocks:
                lines = block.strip().split("\n")
                if len(lines) >= 6:
                    question = lines[0][10:]
                    choices = {k: lines[i][3:] for i, k in enumerate(['a', 'b', 'c', 'd'], start=1)}
                    answer = lines[5][-1]
                    questions.append((question, choices, answer))
            return questions
        except FileNotFoundError:
            return None


class QuizTakerWindow(BaseWindow):
    def __init__(self, master):
        self.window = tk.Toplevel(master)
        self.window.title("Take the Quiz")
        self.window.geometry("500x400")
        self.window.configure(bg="#f0f0f0")

        self.questions = self.load_quiz_data()
        if not self.questions:
            tk.Label(self.window, text="No questions found or file missing.", font=("Arial", 14), bg="#f0f0f0").pack(pady=20)
            return

        random.shuffle(self.questions)
        self.current_index = 0
        self.score = 0
        self.show_question()

    def show_question(self):
        for widget in self.window.winfo_children():
            widget.destroy()

        if self.current_index < len(self.questions):
            question_text, choices, correct_answer = self.questions[self.current_index]
            tk.Label(self.window, text=f"Q{self.current_index + 1}: {question_text}",
                     font=("Arial", 14), wraplength=400, bg="#f0f0f0").pack(pady=10)

            self.answer_var = tk.StringVar(value="")
            for key in ['a', 'b', 'c', 'd']:
                tk.Radiobutton(self.window, text=f"{key}. {choices[key]}", variable=self.answer_var, value=key,
                               anchor="w", justify="left", bg="#f0f0f0", font=("Arial", 12)).pack(fill="x", padx=20, pady=2)

            self.styled_button(self.window, "Submit", lambda: self.submit_answer(correct_answer)).pack(pady=10)
        else:
            tk.Label(self.window, text="Quiz Complete!", font=("Arial", 16), bg="#f0f0f0").pack(pady=20)
            tk.Label(self.window, text=f"Your Score: {self.score} out of {len(self.questions)}",
                     font=("Arial", 14), bg="#f0f0f0").pack()
            self.styled_button(self.window, "Back to Menu", self.window.destroy, bg="#f44336").pack(pady=10)

    def submit_answer(self, correct_answer):
        selected = self.answer_var.get()
        if not selected:
            messagebox.showwarning("No Answer", "Please select an answer.")
            return

        if selected == correct_answer:
            self.score += 1
            messagebox.showinfo("Result", "Correct!")
        else:
            messagebox.showerror("Result", f"Wrong! Correct answer was: {correct_answer}")

        self.current_index += 1
        self.window.after(500, self.show_question)

import tkinter as tk
from tkinter import messagebox
import random

# Base GUI Helper class
class BaseWindow:
    def labeled_entry(self, container, label_text):
        tk.Label(container, text=label_text, font=("Arial", 12), bg="#f0f0f0").pack(pady=2)
        entry = tk.Entry(container, width=50, font=("Arial", 12))
        entry.pack(pady=2)
        return entry

    def styled_button(self, container, text, command, bg="#4CAF50"):
        return tk.Button(container, text=text, command=command, font=("Arial", 12),
                         bg=bg, fg="white", relief="raised")

    def load_quiz_data(self):
        try:
            with open("quiz_data.txt", "r") as file:
                blocks = file.read().split("-" * 40 + "\n")
            questions = []
            for block in blocks:
                lines = block.strip().split("\n")
                if len(lines) >= 6:
                    question = lines[0][10:]
                    choices = {k: lines[i][3:] for i, k in enumerate(['a', 'b', 'c', 'd'], start=1)}
                    answer = lines[5][-1]
                    questions.append((question, choices, answer))
            return questions
        except FileNotFoundError:
            return None


class QuizTakerWindow(BaseWindow):
    def __init__(self, master):
        self.window = tk.Toplevel(master)
        self.window.title("Take the Quiz")
        self.window.geometry("500x400")
        self.window.configure(bg="#f0f0f0")

        self.questions = self.load_quiz_data()
        if not self.questions:
            tk.Label(self.window, text="No questions found or file missing.", font=("Arial", 14), bg="#f0f0f0").pack(pady=20)
            return

        random.shuffle(self.questions)
        self.current_index = 0
        self.score = 0
        self.show_question()

    def show_question(self):
        for widget in self.window.winfo_children():
            widget.destroy()

        if self.current_index < len(self.questions):
            question_text, choices, correct_answer = self.questions[self.current_index]
            tk.Label(self.window, text=f"Q{self.current_index + 1}: {question_text}",
                     font=("Arial", 14), wraplength=400, bg="#f0f0f0").pack(pady=10)

            self.answer_var = tk.StringVar(value="")
            for key in ['a', 'b', 'c', 'd']:
                tk.Radiobutton(self.window, text=f"{key}. {choices[key]}", variable=self.answer_var, value=key,
                               anchor="w", justify="left", bg="#f0f0f0", font=("Arial", 12)).pack(fill="x", padx=20, pady=2)

            self.styled_button(self.window, "Submit", lambda: self.submit_answer(correct_answer)).pack(pady=10)
        else:
            tk.Label(self.window, text="Quiz Complete!", font=("Arial", 16), bg="#f0f0f0").pack(pady=20)
            tk.Label(self.window, text=f"Your Score: {self.score} out of {len(self.questions)}",
                     font=("Arial", 14), bg="#f0f0f0").pack()
            self.styled_button(self.window, "Back to Menu", self.window.destroy, bg="#f44336").pack(pady=10)

    def submit_answer(self, correct_answer):
        selected = self.answer_var.get()
        if not selected:
            messagebox.showwarning("No Answer", "Please select an answer.")
            return

        if selected == correct_answer:
            self.score += 1
            messagebox.showinfo("Result", "Correct!")
        else:
            messagebox.showerror("Result", f"Wrong! Correct answer was: {correct_answer}")

        self.current_index += 1
        self.window.after(500, self.show_question)


class QuizCreatorWindow(BaseWindow):
    def __init__(self, master):
        self.window = tk.Toplevel(master)
        self.window.title("Create Quiz")
        self.window.geometry("500x600")
        self.window.configure(bg="#f0f0f0")

        self.entries = []
        tk.Label(self.window, text="Enter your quiz question and choices", font=("Arial", 14), bg="#f0f0f0").pack(pady=10)

        self.question_entry = self.labeled_entry(self.window, "Question:")
        for label in ['Choice A:', 'Choice B:', 'Choice C:', 'Choice D:']:
            self.entries.append(self.labeled_entry(self.window, label))

        self.answer_entry = self.labeled_entry(self.window, "Correct answer (a/b/c/d):")

        self.styled_button(self.window, "Save Question", self.save_question).pack(pady=10)
        self.styled_button(self.window, "Close", self.window.destroy, bg="#f44336").pack(pady=5)

    def save_question(self):
        question = self.question_entry.get()
        choices = [entry.get() for entry in self.entries]
        answer = self.answer_entry.get().lower()

        if not question or not all(choices) or answer not in ['a', 'b', 'c', 'd']:
            messagebox.showwarning("Invalid Input", "Please fill in all fields correctly.")
            return

        try:
            with open("quiz_data.txt", "a") as f:
                f.write(f"Question: {question}\n")
                for i, option in enumerate(choices):
                    f.write(f"{chr(97+i)}. {option}\n")
                f.write(f"Answer: {answer}\n")
                f.write("-" * 40 + "\n")
            messagebox.showinfo("Saved", "Question saved successfully!")
            self.question_entry.delete(0, tk.END)
            for entry in self.entries:
                entry.delete(0, tk.END)
            self.answer_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save: {e}")


class MainWindow(BaseWindow):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Quiz App Start Menu")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f0f0")

        tk.Label(self.root, text="Welcome to the Quiz App", font=("Arial", 16), bg="#f0f0f0").pack(pady=20)
        self.styled_button(self.root, "Take Quiz", self.open_taker).pack(pady=10)
        self.styled_button(self.root, "Create Quiz", self.open_creator, bg="#2196F3").pack(pady=10)

        self.root.mainloop()

    def open_taker(self):
        QuizTakerWindow(self.root)

    def open_creator(self):
        QuizCreatorWindow(self.root)


if __name__ == "__main__":
    MainWindow()
