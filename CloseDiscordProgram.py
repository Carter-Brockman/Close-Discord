import tkinter as tk
from tkinter import messagebox
import os


discordIsOpen = True


class closeDiscordGUI:

    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("700x500")
        self.root.title("Close Discord")

        self.label = tk.Label(self.root, text="Close Discord", font=('arial', 24))
        self.label.pack(padx=0, pady=10)

        self.closeDiscordButton = tk.Button(self.root, text="Close Discord", font=('Arial', 34), command=killDiscord)
        self.closeDiscordButton.place(x=150, y=125, height=200, width=400)

        self.exitProgramButton = tk.Button(self.root, text="Exit Program", font=('Arial', 20), command=closeProgram)
        self.exitProgramButton.place(x=250, y=350, height=100, width=200)

        self.root.mainloop()


def killDiscord():
    os.system("taskkill /f /IM Discord.exe")
    messagebox.showinfo(title="Discord Closed", message="Discord has been closed")
    exit(0)


def closeProgram():
    exit(0)


closeDiscordGUI()