import tkinter as tk
from random import randint

class Application(tk.Frame):
    def __init__(self, master=None, title="Application", width=300, height=200):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title(title)
        self.master.geometry(f"{width}x{height}")
        self.master.minsize(width=width, height=height)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.button_roll = tk.Button(self, text="Rzuć kostką", command=self.roll_dice)
        self.button_roll.grid(row=0, column=0, columnspan=3)

        self.labels = []
        for i in range(3):
            row_labels = []
            for j in range(3):
                frame = tk.Frame(self)
                frame.grid(row=i + 1, column=j)
                label = tk.Label(frame, text="●", width=4, height=2)
                label.grid()
                row_labels.append(label)
            self.labels.append(row_labels)

    def roll_dice(self):
        result = randint(1, 6)

        for row_labels in self.labels:
            for label in row_labels:
                label.config(text="")

        if result == 1:
            self.labels[1][1].config(text="●")
        elif result == 2:
            self.labels[0][2].config(text="●")
            self.labels[2][0].config(text="●")
        elif result == 3:
            self.labels[0][2].config(text="●")
            self.labels[1][1].config(text="●")
            self.labels[2][0].config(text="●")
        elif result == 4:
            self.labels[0][0].config(text="●")
            self.labels[0][2].config(text="●")
            self.labels[2][0].config(text="●")
            self.labels[2][2].config(text="●")
        elif result == 5:
            self.labels[0][0].config(text="●")
            self.labels[0][2].config(text="●")
            self.labels[1][1].config(text="●")
            self.labels[2][0].config(text="●")
            self.labels[2][2].config(text="●")
        elif result == 6:
            self.labels[0][0].config(text="●")
            self.labels[1][0].config(text="●")
            self.labels[2][0].config(text="●")
            self.labels[0][2].config(text="●")
            self.labels[1][2].config(text="●")
            self.labels[2][2].config(text="●")

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root, "Rzut kostką")
    root.mainloop()
