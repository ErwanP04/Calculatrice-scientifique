import tkinter as tk
from tkinter import ttk
from calculator import ScientificCalculator

def main():
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
