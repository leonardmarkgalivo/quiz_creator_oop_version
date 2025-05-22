import tkinter as tk

class QuizCreatorWindow:
    def __init__(self, master):
        self.window = tk.Toplevel(master)
        self.window.title("Quiz Creator")
        self.window.geometry("500x500")

        self.entry_question = tk.Entry(self.window)
        self.entry_question.pack()

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Quiz App Start Menu")
        self.root.geometry("400x300")

        tk.Button(self.root, text="Create Quiz", command=self.open_creator).pack(pady=10)
        tk.Button(self.root, text="Take Quiz", command=self.open_taker).pack(pady=10)

        self.root.mainloop()

    def open_creator(self):
        QuizCreatorWindow(self.root)

    def open_taker(self):
        pass

if __name__ == "__main__":
    MainWindow()