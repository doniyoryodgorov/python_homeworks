class BankAccount:
    def __init__(self):
        self.account = 0  # Initial balance is 0

    def deposit(self, amount):
        if amount > 0:
            self.account += amount
            print(f"Deposited: ${amount}. New balance: ${self.account}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if amount > self.account:
            print("Not enough money in balance!")
        elif amount > 0:
            self.account -= amount
            print(f"Withdrawn: ${amount}. New balance: ${self.account}")
        else:
            print("Withdrawal amount must be positive!")

    def check_balance(self):
        print(f"Current balance: ${self.account}")



def sum_of_digits(number):
    total = 0
    for digit in str(abs(number)):
        total += int(digit)
    return total

# Example Usage:
num = 12345
print(f"Sum of digits of {num} is {sum_of_digits(num)}")

