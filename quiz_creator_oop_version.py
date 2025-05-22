import tkinter as tk

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Quiz App Start Menu")
        self.root.geometry("400x300")
        self.root.mainloop()

if __name__ == "__main__":
    MainWindow()