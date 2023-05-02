"""
The next program will calculate the ideal weight of a person based on their gender and 
their height using the well-known Lorentz formula.
"""


import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Ideal Weight Calculator")
root.geometry("400x200")

# Center window
window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()
position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
position_down = int(root.winfo_screenheight() / 2 - window_height / 2)
root.geometry("+{}+{}".format(position_right, position_down))

# Create a label for gender selection
gender_label = ttk.Label(root, text="What is your gender? (M/F)")
gender_label.pack(pady=5)

# Create a combobox for gender selection
gender_combobox = ttk.Combobox(root, values=["M", "F"], state="readonly")
gender_combobox.pack()

# Create a label for height input
height_label = ttk.Label(root, text="What is your height? (cm)")
height_label.pack(pady=5)

# Create an entry field for height input
height_entry = ttk.Entry(root)
height_entry.pack()

# Function to calculate ideal weight
def calculate_ideal_weight():
    gender = gender_combobox.get()
    height = height_entry.get()

    # Validate input
    if not gender or not height:
        result_label.config(text="Please enter both gender and height.")
        return

    try:
        height = int(height)
    except ValueError:
        result_label.config(text="Please enter a valid number for height.")
        return

    # Calculate ideal weight based on gender
    if gender == "M":
        ideal_weight = height - 110
    elif gender == "F":
        ideal_weight = height - 120

    # Display the result
    result_label.config(text=f"Your ideal weight is: {ideal_weight}")

# Create a button to calculate the result
calculate_button = ttk.Button(root, text="Calculate", command=calculate_ideal_weight)
calculate_button.pack(pady=10)

# Create a label to display the result
result_label = ttk.Label(root, text="")
result_label.pack()

root.mainloop()
