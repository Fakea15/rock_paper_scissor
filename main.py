import random as rd
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget

Window.size = (300, 650)


class Text(Widget):

    # Computer leh Player tum tir tu ber.
    def on_click(self):
        rps = ["rock", "paper", "scissor"]
        computer = rd.choice(rps)
        Player = self.ids.name_input.text.lower()
        if Player == rps[0] and computer == rps[0]:
            self.ids.name_label.text = "ROCK, you are draw!"
        elif Player == rps[1] and computer == rps[1]:
            self.ids.name_label.text = "PAPER, you are draw!"
        elif Player == rps[2] and computer == rps[2]:
            self.ids.name_label.text = "SCISSOR, you are draw!"
        elif Player == rps[0] and computer == rps[1]:
            self.ids.name_label.text = "PAPER, you lose!"
        elif Player == rps[2] and computer == rps[1]:
            self.ids.name_label.text = "PAPER, you win!"
        elif Player == rps[1] and computer == rps[0]:
            self.ids.name_label.text = "ROCK, you lose!"
        elif Player == rps[2] and computer == rps[0]:
            self.ids.name_label.text = "ROCK, you lose!"
        elif Player == rps[0] and computer == rps[2]:
            self.ids.name_label.text = "SCISSOR, you win!"
        elif Player == rps[1] and computer == rps[2]:
            self.ids.name_label.text = "SCISSOR, you lose!"
        elif Player == "":
            self.ids.name_label.text = "Please Enter something"
        elif Player != 'rock' or 'paper' or 'scissor':
            self.ids.name_label.text = "Please Check the spelling"

        # A input na box button hmeh zawh ruala ti ruak tu
        self.ids.name_input.text = ''

    def on_clicked_reset(self):
        self.ids.name_label.text = ""

class BoxLayout(BoxLayout):
    pass

class ImageLayout(GridLayout):
    pass

class MainApp(App):
    pass

MainApp().run()



