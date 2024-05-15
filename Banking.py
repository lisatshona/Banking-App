class BankingApplication:
    def __init__(self):
        self.bank_data_file = "BankData.txt"
        self.transaction_log_file = "TransactionLog.txt"

    def read_balance(self):
        try:
            with open(self.bank_data_file, "r") as file:
                balance = float(file.read())
                return balance
        except FileNotFoundError:
            with open(self.bank_data_file, "w") as file:
                file.write("0.00")
                return 0.00

    def write_balance(self, balance):
        with open(self.bank_data_file, "w") as file:
            file.write(str(balance))

    def log_transaction(self, transaction_type, amount):
        with open(self.transaction_log_file, "a") as file:
            file.write(f"{transaction_type}: ${amount}\n")

    def make_deposit(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError
            balance = self.read_balance()
            balance += amount
            self.write_balance(balance)
            self.log_transaction("Deposit", amount)
            print(f"Successfully deposited ${amount}. Current balance: ${balance}")
        except ValueError:
            print("You provided an invalid input.")

    def make_withdrawal(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError
            balance = self.read_balance()
            if amount > balance:
                print("Insufficient funds.")
                return
            balance -= amount
            self.write_balance(balance)
            self.log_transaction("Withdrawal", amount)
            print(f"Successfully withdrew ${amount}. Current balance: ${balance}")
        except ValueError:
            print("You provided an invalid input.")

    def main(self):
        print("Welcome to the PocketGuard Banking Application 😊")
        while True:
            make_transaction = input("Would you like to make a transaction? (Yes or No): ").lower()
            if make_transaction != "yes":
                print("Thank you for using the PocketGuard Banking Application 😊")
                break

            current_balance = self.read_balance()
            print(f"Current balance: ${current_balance}")

            transaction_type = input("Would you like to make a deposit or withdrawal? (Deposit or Withdrawal): ").lower()
            if transaction_type == "deposit":
                amount = input("How much would you like to deposit? $")
                self.make_deposit(amount)
            elif transaction_type == "withdrawal":
                amount = input("How much would you like to withdraw? $")
                self.make_withdrawal(amount)
            else:
                print("You provided an invalid input.")
                continue


if __name__ == "__main__":
    banking_app = BankingApplication()
    banking_app.main()
