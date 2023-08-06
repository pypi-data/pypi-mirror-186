import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()
answer = messagebox.askyesno("hi stranger", "We all agree life is boring \n Click yes to end it")
if answer == True:
    print("Thank you")
else:
    print("sheeeeesh :/")
