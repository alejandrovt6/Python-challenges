"""
Ask the user for two numbers, within this range it will print the numbers replacing:

- Multiples of 3 with the word "Hello".
- Multiples of 5 with the word "World".
- Multiples of 3 and 5 at the same time with the word "HelloWorld".
"""

# Libraries
import tkinter as tk

# Program
def game():
    a = int(entry1.get())
    b = int(entry2.get())
    result = ""

    for x in range(a, b+1):
        if x % 3 == 0 and x % 5 == 0:
            result += "Hello World\n"
        elif x % 3 == 0:
            result += "Hello\n"
        elif x % 5 == 0:
            result += "World\n"
        else:
            result += str(x) + "\n"

    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, result)
    result_text.config(state=tk.DISABLED)

# GUI
window = tk.Tk()
window.title("Hello World Game")
window.geometry("400x300")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width - window.winfo_screenmmwidth()) / 2)
y = int((screen_height - window.winfo_screenmmheight()) / 2)

window.geometry("+{}+{}".format(x, y))

label1 = tk.Label(window, text="First number:")
label1.pack()

entry1 = tk.Entry(window)   
entry1.pack()

label2 = tk.Label(window, text="Second number:")
label2.pack()

entry2 = tk.Entry(window)
entry2.pack()

run_button = tk.Button(window, text="Run", command=game)
run_button.pack()

result_text = tk.Text(window, width=30, height=10)
result_text.config(state=tk.DISABLED)

result_text.pack()

window.mainloop()
