"""
Used for creating graphical interfaces
"""

import tkinter as tk


class Menu:
    """
    Creates a menu using given parameters. Arguments given should be
    tuples or lists. each tuple/list will create an item in the menu.
    For example:
      -Menu(("button", text_displayed_on_button, function_to_execute_on_click),
          ("text",))
    creates a button and text box
    """

    def __init__(self, *create):
        main = tk.Tk()
        main.geometry("480x480")
        frame = tk.Frame(main)
        text = ""
        frame.pack()
        for item in create:
            if item[0].lower() == "button":
                accept = tk.Button(frame, text = item[1], command=item[2])

            if item[0].lower() == "text":
                accept = tk.Text(frame)
                

            accept.pack()
