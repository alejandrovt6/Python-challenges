"""
This program will generate a random password between 8 and 16 characters. The user can choose the options they want to include, 
such as digits, uppercase letters, lowercase letters, and special characters, as well as the length.
"""
import tkinter as tk
import random

def build_password():
    length = int(length_var.get())
    final = ""
    if length < 8 or length > 16:
        error_label.config(text="Error: Password length must be between 8 and 16.")
    else:
        r_lower = lower_var.get()
        r_upper = upper_var.get()
        r_digit = digit_var.get()
        r_special = special_var.get()
        char_pool = ""
        if r_lower:
            char_pool += "abcdefghijklmnopqrstuvwxyz"
        if r_upper:
            char_pool += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if r_digit:
            char_pool += "0123456789"
        if r_special:
            char_pool += "!@#$%^&*()_+"
        if len(char_pool) == 0:
            error_label.config(text="Error: You must select at least one type of character.")
        else:
            for i in range(length):
                final += random.choice(char_pool)
            password_label.config(text=final)
            error_label.config(text="")

# GUI
window = tk.Tk()
window.title("Password Generator")
window.geometry("500x400")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width - window.winfo_screenmmwidth()) / 2)
y = int((screen_height - window.winfo_screenmmheight()) / 2)

window.geometry("+{}+{}".format(x, y))

# Password length
options = ["8", "9", "10", "11", "12", "13", "14", "15", "16"]
length_var = tk.StringVar(window)
length_var.set(options[0])  
length_label = tk.Label(window, text="Password length (8-16):")
length_label.pack()
length_menu = tk.OptionMenu(window, length_var, *options)
length_menu.pack()


# Lowercase characters
lower_label = tk.Label(window, text="Include lowercase characters:")
lower_label.pack()
lower_var = tk.BooleanVar()
lower_check = tk.Checkbutton(window, variable=lower_var)
lower_check.pack()

# Uppercase characters
upper_label = tk.Label(window, text="Include uppercase characters:")
upper_label.pack()
upper_var = tk.BooleanVar()
upper_check = tk.Checkbutton(window, variable=upper_var)
upper_check.pack()

# Digits
digit_label = tk.Label(window, text="Include digits:")
digit_label.pack()
digit_var = tk.BooleanVar()
digit_check = tk.Checkbutton(window, variable=digit_var)
digit_check.pack()

# Special characters
special_label = tk.Label(window, text="Include special characters:")
special_label.pack()
special_var = tk.BooleanVar()
special_check = tk.Checkbutton(window, variable=special_var)
special_check.pack()

# Generate password button
generate_button = tk.Button(window, text="Generate Password", command=build_password)
generate_button.pack(pady=10)

# Password display label
password_label = tk.Label(window, text="")
password_label.pack(pady=10)

# password_label.pack()

# Error label
error_label = tk.Label(window, text="", fg="red")
error_label.pack()

window.mainloop()