from tkinter import *
from view import View
from model import Model

class Controller(object):
    def start_game(self):
        view = View()
        model = Model()
        view.display_initial_view(model)
        view.highlight_bingo_value(model.bingo_values[12])
        view.root.mainloop()
