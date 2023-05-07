"""
Write a program that takes text and transforms natural language into "hacker language" (actually known as "leet" or "1337"). This language is characterized by substituting alphanumeric 
characters. Use this table (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) with the alphabet and numbers in "leet".
"""

# Libraries
import tkinter as tk

HACKER_CODE = {
    "a": "4", "b": "I3", "c": "[", "d": ")", "e": "3", "f": "|=", "g": "&", "h": "#", "i": "1", "j": ",_|", "k": ">|",
    "l": "1", "m": "/\/\\", "n": "^/", "o": "0", "p": "|*", "q": "(_,)", "r": "|2", "s": "5", "t": "7", "u": "(_)",
    "v": "\/", "w": "\/\/", "x": "><", "y": "j", "z": "2", "1": "L", "2": "R", "3": "E", "4": "A", "5": "S", "6": "b",
    "7": "T", "8": "B", "9": "g", "0": "o", " ":" "
}

# Program
def hacker_encode(message):
    hacker_code = []
    
    for char in message:
        if char.lower() in HACKER_CODE:
            hacker_code.append(HACKER_CODE[char.lower()])
        else:
            return "ERROR: Character not found in dictionary."
        
    return "".join(hacker_code)


def codify_message():
    message = entry.get()
    result = hacker_encode(message)
    result_label.config(text=result)


# GUI
window = tk.Tk()
window.geometry("400x150")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width - window.winfo_screenmmwidth()) / 2)
y = int((screen_height - window.winfo_screenmmheight()) / 2)

window.geometry("+{}+{}".format(x, y))

label = tk.Label(window, text="Type a message to codify:")
label.pack()

entry = tk.Entry(window)
entry.pack()

run_button = tk.Button(window, text="Run", command=codify_message)
run_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
