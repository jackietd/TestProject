"""Used to create the main menu"""
import Graphics.BasicInterface as Interface


class MainMenu:
    def test_command(self):
        #This is a test command that will be changed later
        print("Clicked")

    def __init__(self):
        # Creates a menu with a button and text area
        GUI = Interface.Menu(("button", "Press Me",self.test_command),
                             ("text",))
