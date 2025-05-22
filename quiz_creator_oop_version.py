import tkinter as tk

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Quiz App Start Menu")
        self.root.geometry("400x300")

        tk.Button(self.root, text="Create Quiz", command=self.open_creator).pack(pady=10)
        tk.Button(self.root, text="Take Quiz", command=self.open_taker).pack(pady=10)

        self.root.mainloop()

    def open_creator(self):
        pass

    def open_taker(self):
        pass

if __name__ == "__main__":
    MainWindow()