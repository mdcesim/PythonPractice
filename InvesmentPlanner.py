# 1. Investment planner:
# Write a program to calculate investment value of 10 years. Calculator should ask user 
# for initial balance, compound interest ratio, and monthly added balance and yearly 
# withdraw values. Draw a plot graph of balance.
# Initial balance = 10000 TRY, yearly withdraw is 5000 TRY, monthly added balance is 500 
# TRY, using the compound interest of 10% (monthly)
import matplotlib.pyplot as plt

class InvesmentPlanner: 
    def __init__(self, initial_balance, faiz, mnthly_added, yrly_withdrow):
        self.balance = initial_balance
        self.faiz = faiz
        self.mnthly_addded = mnthly_added
        self.yrly_withdrow = yrly_withdrow
        self.months = 0
    
    def get_user_info(self):
        try:
            self.balance = int(input("What is your current balance? "))
            self.faiz = float(input("What is the compound interest ratio? "))
            self.mnthly_addded = int(input("How much do you want to add monthly? "))
            self.yrly_withdrow = int(input("How much do you withdrow yearly? "))
            years = int(input("How many years do you want to see growth over? "))
            self.months = years*12
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            self.get_user_info()

    def calc_mnthly_balance(self, months):
        balances = []
        for month in range(1, months +1):
            self.balance += self.balance*self.faiz
            self.balance += self.mnthly_addded
            if month % 12 == 0:
                self.balance -= self.yrly_withdrow
            balances.append(self.balance)
        return balances

    def visulize_graph(self, balances):
        plt.plot(range(1,len(balances) +1), balances, label= "Invesment balance")
        plt.title("Investment Growth Over 10 Years")
        plt.xlabel("Months")
        plt.ylabel("Balance (TRY)")
        plt.legend()
        plt.grid(True)
        plt.show()

planner = InvesmentPlanner(0,0,0,0)
planner.get_user_info()
balances = planner.calc_mnthly_balance(planner.months)
print("Balances for first 12 month", balances)
planner.visulize_graph(balances)
