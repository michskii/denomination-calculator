import tkinter as tk
from tkinter import messagebox

def calculate_notes():
    try:
        amount= int(entry_amount.get())
        if amount%50!=0:
            messagebox.showerror("Error", "Amount must be a multiple of 50.")
            return
        notes_1000 = amount // 1000
        remainder = amount % 1000
        notes_500 = remainder // 500
        remainder = remainder % 500
        notes_100 = remainder // 100
        remainder = remainder % 100
        notes_50 = remainder // 50

        result=(
            f"1000s: {notes_1000}\n"
            f"500s: {notes_500}\n"
            f"100s: {notes_100}\n"
            f"50s: {notes_50}\n"
        )
        Label_result.config(text=result)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer amount.")
root= tk.Tk()
root.title("Denomination Calculator")
tk.Label(root, text="Enter amount").grid(row=0, column=0, padx=10, pady=10)
entry_amount= tk.Entry(root)
entry_amount.grid(row=0, column=1, padx=10, pady=10) 
tk.Button(root, text="calculate", command=calculate_notes).grid(row=1, column=0, columnspan=2, pady=10)

Label_result= tk.Label(root, text="", font=("lexend", 12))
Label_result.grid(row=2, column=0, columnspan=2, pady=10)
root.mainloop()
# This code creates a simple GUI application using Tkinter to calculate the number of notes of different denominations (1000, 500, 100, and 50) needed to make up a given amount. The user inputs an amount, and the application checks if it is a multiple of 50 before calculating and displaying the number of each denomination required. If the input is invalid, an error message is shown.