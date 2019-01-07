"""
Used for the graphical interface
"""

import tkinter as tk


class Menu:
    main = tk.Tk()
    main.geometry("480x480")
    frame = tk.Frame(main)
    text = ""
    accept = tk.Button(frame, text="Button")

    def click_accept(self):
        print("Clicked")

    def __init__(self):
        self.frame.pack()
        self.accept.pack()
        self.accept.config(command=self.click_accept)
