# 4. Monthly payments:
# Write a program to track your expenses, such as market, clothing, car (gas, insurance, 
# maintenance), monthly fee of subscriptions, house rent, etc. Divide them to several 
# categories and show with a pie chart to visualize your monthly payments.

# Program should have a main screen, where you add payments, add incomes, display 
# a list of records and a display section. There should be a section of left balance, if it is 
# negative, inform user.

# Example: 
# payment input: grocery, 1000, daily
# payment input: Spotify, 100, subscriptions
# payment input: gas, 1000, car
# payment input: tshirt, 500, clothing
# income input: salary, 10000
# income input: promotion, 5000

# add_income(), add_payment(), display_list(), display_graph()
import matplotlib.pyplot as plt

class MonthlyPayments:
    def __init__(self):
        self.payments = []
        self.incomes = []
        self.balance = 0
    
    def add_income(self):
        try:
            self.income_amount = float(input("Enter income amount: "))
            self.balance += self.income_amount
            self.income_type = input("Enter the income type: ")
            self.incomes.append({"type": self.income_type, "amount": self.income_amount})
            print(f"{self.income_amount} TL added as {self.income_type}. New Balance {self.balance}")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            self.add_income()

    def add_payment(self):
        try:
            self.payment_category = input("Enter the payment category: ")
            self.payment_type = input("Enter the payments type: ")
            self.payment_amount = int(input("How much the payment is? "))
            if self.balance >= self.payment_amount:
                self.payments.append({"category": self.payment_category, 
                                      "type": self.payment_type, 
                                      "amount": self.payment_amount})
                self.balance -= self.payment_amount
                print(f"Category: {self.payment_category}\nType: {self.payment_type}\nPayment succefully added. New Balance is {self.balance} TL")
            else: 
                print("Insufficient balance. Payment not added, try again")
        except ValueError:
            print("Invalid Input.Try again")
            self.add_payment()
    
    def display_list(self):
        print("PAYMENTS LIST:")
        for payment in self.payments:
            print(f"{payment['type']}, {payment['amount']} TL")
        print("\nINCOMES LIST:")
        for income in self.incomes:
            print(f"{income['type']}, {income['amount']} TL")
    
    def display_graph(self):
        categories = [payment['type'] for payment in self.payments]
        amounts = [payment['amount'] for payment in self.payments]
        plt.pie(amounts, labels=categories, autopct='%1.1f%%')
        plt.title("Payments Distribution")
        plt.show()

def main():
    trucker = MonthlyPayments()
    print("Welocme to the Monthly Payments program!")
    while True:  
        print("How can I help you? Please chose an operation.")
        print("Operation Menu:")
        print("1. Add Income\n2. Add Payment\n3. Display lists\n4. Display Payments Distribution\n5. Exit")
        choice = int(input("Choice: "))
        try:    
            if choice == 1:
                trucker.add_income()
            elif choice == 2:
                trucker.add_payment()
            elif choice == 3:
                trucker.display_list()
            elif choice == 4:
                trucker.display_graph()
            elif choice == 5:
                print("Existing program.. please press Enter")
                input()
                break
            else: print("Invalid choice.")
        except ValueError:
            print("An error happened.. try again")

main()