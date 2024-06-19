import tkinter as tk
from tkinter import ttk
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculatrice Scientifique")
        self.current_input = ""
        self.create_widgets()

    def create_widgets(self):
        # Écran d'affichage
        self.display = ttk.Entry(self.root, font=('Arial', 20), justify='right')
        self.display.grid(row=0, column=0, columnspan=8)

        # Boutons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('sin', 1, 4), ('cos', 1, 5), ('tan', 1, 6), ('sqrt', 1, 7),
            ('log', 2, 4), ('ln', 2, 5), ('(', 2, 6), (')', 2, 7),
            ('^', 3, 4), ('C', 3, 5), ('%', 3, 6), ('pi', 3, 7)
        ]

        for (text, row, col) in buttons:
            self.create_button(text, row, col)

        # Configuration des boutons pour s'étendre uniformément
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(8):
            self.root.grid_columnconfigure(i, weight=1)

    def create_button(self, text, row, col):
        button = ttk.Button(self.root, text=text, command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col, sticky='nsew')

    def on_button_click(self, char):
        if char == '=':
            self.calculate()
        elif char == 'C':
            self.current_input = ""
            self.display.delete(0, tk.END)
        else:
            self.current_input += str(char)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.current_input)

    def calculate(self):
        try:
            # Remplacer les fonctions mathématiques par celles du module math
            expression = self.current_input.replace('^', '**').replace('pi', 'math.pi')
            expression = expression.replace('sin', 'math.sin').replace('cos', 'math.cos')
            expression = expression.replace('tan', 'math.tan').replace('sqrt', 'math.sqrt')
            expression = expression.replace('log', 'math.log10').replace('ln', 'math.log')
            result = eval(expression)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Erreur")
