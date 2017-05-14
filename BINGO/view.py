from tkinter import *

class View(object):
    def __init__(self):
        self.root = Tk()

    def display_initial_view(self, model):
        self.display_initial_bingo_values(model)

    def display_initial_bingo_values(self, model):
        bingo_letters = 'BINGO'
        for row in range(5):
            Label(self.root, text = str(bingo_letters[row]),
                borderwidth = 1 ).grid(row = row, column = 0)
        
        value = 0
        for row in range(5):
            for column in range(1, 16):
                value += 1
                model.bingo_values[value] = Label(self.root, text = str(value), borderwidth = 1 )
                model.bingo_values[value].grid(row = row, column = column)

    def highlight_bingo_value(self, bingo_value):
        bingo_value.configure(bg = "yellow")