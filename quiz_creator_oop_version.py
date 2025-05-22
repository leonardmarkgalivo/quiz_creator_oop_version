import tkinter as tk
from tkinter import messagebox
import random

class BaseWindow:
    def labeled_entry(self, container, label_text):
        tk.Label(container, text=label_text, font=("Arial", 12), bg="#f0f0f0").pack(pady=2)
        entry_widget = tk.Entry(container, width=50, font=("Arial", 12))
        entry_widget.pack(pady=2)
        return entry_widget

    def styled_button(self, container, button_text, command, bg="#4CAF50"):
        button_widget = tk.Button(container, text=button_text, command=command, font=("Arial", 12),
                        bg=bg, fg="white", relief="raised")
        button_widget.pack(pady=5)
        return button_widget

    def load_quiz_data(self):
        try:
            with open("quiz_data.txt", "r") as quiz_file:
                blocks = quiz_file.read().split("-" * 40 + "\n")
            questions = []
            for block in blocks:
                lines = block.strip().split("\n")
                if len(lines) >= 6 and lines[0].startswith("Question: "):
                    question_text = lines[0][10:].strip()
                    choices = {
                        'option_a': lines[1][3:].strip(),
                        'option_b': lines[2][3:].strip(),
                        'option_c': lines[3][3:].strip(),
                        'option_d': lines[4][3:].strip()
                    }
                    answer = lines[5].split()[-1].strip().lower()
                    if answer in ['option_a', 'option_b', 'option_c', 'option_d']:
                        questions.append((question_text, choices, answer))
            return questions if questions else None
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
        self.answer_var = tk.StringVar(value="")
        self.show_question()

    def show_question(self):
        for widget in self.window.winfo_children():
            widget.destroy()

        if self.current_index < len(self.questions):
            question_text, choices, correct_answer = self.questions[self.current_index]
            tk.Label(self.window, text=f"Q{self.current_index + 1}: {question_text}",
                     font=("Arial", 14), wraplength=400, bg="#f0f0f0").pack(pady=10)

            self.answer_var.set("")
            for option_key, option_text in choices.items():
                tk.Radiobutton(self.window, text=f"{option_key[-1]}. {option_text}", 
                              variable=self.answer_var, value=option_key,
                              anchor="w", justify="left", bg="#f0f0f0", font=("Arial", 12)).pack(fill="x", padx=20, pady=2)

            self.styled_button(self.window, "Submit", lambda: self.submit_answer(correct_answer))
        else:
            tk.Label(self.window, text="Quiz Complete!", font=("Arial", 16), bg="#f0f0f0").pack(pady=20)
            tk.Label(self.window, text=f"Your Score: {self.score} out of {len(self.questions)}",
                     font=("Arial", 14), bg="#f0f0f0").pack()
            self.styled_button(self.window, "Back to Menu", self.window.destroy, bg="#f44336")

    def submit_answer(self, correct_answer):
        selected = self.answer_var.get()
        if not selected:
            messagebox.showwarning("No Answer", "Please select an answer.")
            return

        if selected == correct_answer:
            self.score += 1
            messagebox.showinfo("Result", "Correct!")
        else:
            messagebox.showerror("Result", f"Wrong! Correct answer was: {correct_answer[-1]}")

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
        for label_text in ['Choice A:', 'Choice B:', 'Choice C:', 'Choice D:']:
            self.entries.append(self.labeled_entry(self.window, label_text))

        self.answer_entry = self.labeled_entry(self.window, "Correct answer (a/b/c/d):")

        self.styled_button(self.window, "Save Question", self.save_question)
        self.styled_button(self.window, "Close", self.window.destroy, bg="#f44336")

    def save_question(self):
        question_text = self.question_entry.get().strip()
        choices = [entry.get().strip() for entry in self.entries]
        answer = self.answer_entry.get().strip().lower()

        if not question_text or not all(choices) or answer not in ['a', 'b', 'c', 'd']:
            messagebox.showwarning("Invalid Input", "Please fill in all fields correctly.")
            return

        try:
            with open("quiz_data.txt", "a") as quiz_file:
                quiz_file.write(f"Question: {question_text}\n")
                for index, option_text in enumerate(choices):
                    quiz_file.write(f"{chr(97+index)}. {option_text}\n")
                quiz_file.write(f"Answer: option_{answer}\n")
                quiz_file.write("-" * 40 + "\n")
            messagebox.showinfo("Saved", "Question saved successfully!")
            self.question_entry.delete(0, tk.END)
            for entry in self.entries:
                entry.delete(0, tk.END)
            self.answer_entry.delete(0, tk.END)
        except Exception as save_error:
            messagebox.showerror("Error", f"Failed to save: {save_error}")


class MainWindow(BaseWindow):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Quiz App Start Menu")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f0f0")

        tk.Label(self.root, text="Welcome to the Quiz App", font=("Arial", 16), bg="#f0f0f0").pack(pady=20)
        self.styled_button(self.root, "Take Quiz", self.open_taker)
        self.styled_button(self.root, "Create Quiz", self.open_creator, bg="#2196F3")

        self.root.mainloop()

    def open_taker(self):
        QuizTakerWindow(self.root)

    def open_creator(self):
        QuizCreatorWindow(self.root)

if __name__ == "__main__":
    MainWindow()