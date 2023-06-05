# Program in process...
# This program simulate a bank teller 
# TODO: exits, GUI


# Program
class BankTeller:
    def __init__(self):
        self.cash = 1000

    def show_cash(self):
        print(f"Your current balance is: {self.cash} $")
        op = input("Do you want to do another action? (Y/N): ")
        if op.lower() == "y":
            return True
        elif op.lower() == "n":
            print("Exiting the program...")
            exit()
        else:
            print("ERROR: Invalid choice.")
            print("ERROR: Invalid choice.")
            return False

    def withdraw_money(self):
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= self.cash:
            self.cash -= amount
            print(f"Withdrew {amount} $. Remaining balance: {self.cash} $")
        else:
            print("Insufficient funds!")

    def deposit_money(self):
        amount = float(input("Enter the amount to deposit: "))
        self.cash += amount
        print(f"Deposited {amount} $. New balance: {self.cash} $")

    def send_money(self):
        receiver = int(input("Enter the receiver's card number: "))
        amount_send = int(input("Enter the amount you want to send: "))
        if amount_send > self.cash:
            print("ERROR: Insufficient funds.")
        else:
            self.cash -= amount_send
            print(f"Money sent successfully. New balance: {self.cash} $")
            exit()

    # Run bank teller
    def run(self):
        secret = 0
        print("Welcome to Bank Teller.")
        print("Enter your secret code code to continue: ")
        print("***Default code: 1111***")

        # Identification
        attemps = 0
        max_attemps = 3
        while secret != 1111:
            secret = int(input("Enter your secret code to continue: "))
            if secret == 1111:
                attemps +=1
                print("Accepted identification.")
            else:
                attemps +=1
                print("Wrong code. Please try again.")
                print(max_attemps - attemps , "Attemps left.")
                if attemps == 3:
                    print("Maximum attempts allowed. The card has been locked.")
                    exit()
         
        # Options
        while True:
            print("Bank Teller Panel")
            print("1. Show my cash")
            print("2. Withdraw money")
            print("3. Deposit money")
            print("4. Send money")
            print("5. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                self.show_cash()
            elif choice == "2":
                self.withdraw_money()
            elif choice == "3":
                self.deposit_money()
            elif choice =="4":
                self.send_money()
            elif choice == "5":
                print("Thank you for using the Bank Teller. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    teller = BankTeller()
    teller.run()
