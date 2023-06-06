import tkinter as tk
from tkinter import messagebox

class BankTellerGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Bank Teller")
        
        self.secret_code = tk.StringVar()
        self.cash = 1000

        self.create_widgets()

    def create_widgets(self):
        # Secret Code Entry
        secret_code_label = tk.Label(self.window, text="Enter your secret code:")
        secret_code_label.pack()

        secret_code_entry = tk.Entry(self.window, textvariable=self.secret_code, show="*")
        secret_code_entry.pack()

        identification_button = tk.Button(self.window, text="Enter", command=self.identification)
        identification_button.pack()

        self.window.mainloop()

    def identification(self):
        code = self.secret_code.get()
        if code == "1111":
            self.show_menu()
        else:
            messagebox.showerror("Identification", "Wrong code. Please try again.")

    def show_menu(self):
        menu_window = tk.Toplevel(self.window)
        menu_window.title("Bank Teller Panel")

        # Menu options
        show_cash_button = tk.Button(menu_window, text="Show my cash", command=self.show_cash)
        show_cash_button.pack()

        withdraw_button = tk.Button(menu_window, text="Withdraw money", command=self.withdraw_money)
        withdraw_button.pack()

        deposit_button = tk.Button(menu_window, text="Deposit money", command=self.deposit_money)
        deposit_button.pack()

        send_money_button = tk.Button(menu_window, text="Send money", command=self.send_money)
        send_money_button.pack()

        exit_button = tk.Button(menu_window, text="Exit", command=self.window.destroy)
        exit_button.pack()

    def show_cash(self):
        messagebox.showinfo("Balance", f"Your current balance is: {self.cash} $")

    def withdraw_money(self):
        withdraw_window = tk.Toplevel(self.window)
        withdraw_window.title("Withdraw Money")

        amount_label = tk.Label(withdraw_window, text="Enter the amount to withdraw:")
        amount_label.pack()

        amount_entry = tk.Entry(withdraw_window)
        amount_entry.pack()

        confirm_button = tk.Button(withdraw_window, text="Confirm", command=lambda: self.withdraw(amount_entry.get(), withdraw_window))
        confirm_button.pack()

    def withdraw(self, amount, window):
        try:
            amount = float(amount)
            if amount <= self.cash:
                self.cash -= amount
                messagebox.showinfo("Withdraw", f"Withdrew {amount} $. Remaining balance: {self.cash} $")
            else:
                messagebox.showerror("Error", "Insufficient funds!")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount.")

        window.destroy()

    def deposit_money(self):
        deposit_window = tk.Toplevel(self.window)
        deposit_window.title("Deposit Money")

        amount_label = tk.Label(deposit_window, text="Enter the amount to deposit:")
        amount_label.pack()

        amount_entry = tk.Entry(deposit_window)
        amount_entry.pack()

        confirm_button = tk.Button(deposit_window, text="Confirm", command=lambda: self.deposit(amount_entry.get(), deposit_window))
        confirm_button.pack()

    def deposit(self, amount, window):
        try:
            amount = float(amount)
            self.cash += amount
            messagebox.showinfo("Deposit", f"Deposited {amount} $. New balance: {self.cash} $")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount.")

        window.destroy()

    def send_money(self):
        send_window = tk.Toplevel(self.window)
        send_window.title("Send Money")

        receiver_label = tk.Label(send_window, text="Enter the receiver's card number:")
        receiver_label.pack()

        receiver_entry = tk.Entry(send_window)
        receiver_entry.pack()

        amount_label = tk.Label(send_window, text="Enter the amount to send:")
        amount_label.pack()

        amount_entry = tk.Entry(send_window)
        amount_entry.pack()

        confirm_button = tk.Button(send_window, text="Confirm", command=lambda: self.send(receiver_entry.get(), amount_entry.get(), send_window))
        confirm_button.pack()

    def send(self, receiver, amount, window):
        try:
            receiver = int(receiver)
            amount = float(amount)
            if amount <= self.cash:
                self.cash -= amount
                messagebox.showinfo("Send Money", f"Money sent successfully. New balance: {self.cash} $")
            else:
                messagebox.showerror("Error", "Insufficient funds.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input.")

        window.destroy()

if __name__ == "__main__":
    bank_teller_gui = BankTellerGUI()

