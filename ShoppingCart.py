# Shopping cart:
# Write a program to track your items in shopping. First input your balance, followed by 
# adding items to your cart. Whenever an item added to your cart, remove from your list. 
# If the balance is passed, give an error. At last, show a graph of each item using bar 
# graph and display the difference between your list and price of shop.
# Example:
# List = [(milk, 2, 50), (honey, 1, 100), ….]
# Cart = [(milk, 2, 75), (honey, 1, 80), …]
# Output = Milk is xx% expensive, Honey is xx% cheaper, ….
# Total list balance is 5000 with 12 items, cart is 4850 tl with 11 items
import matplotlib.pyplot as plt

class ShoppingCart:
    def __init__(self):
        self.name = 0
        self.quantity = 0
        self.price = 0
        self.balance = 5000
        self.list = [
            ("Milk", 2, 50), # Name - Quantity - Price
            ("Honey", 1, 100),
            ("Bread", 3, 20),
            ("Eggs", 12, 10),
            ("Butter", 1, 70),
            ("Cheese", 2, 90),
            ("Apples", 5, 15),
            ("Bananas", 6, 10),
            ("Chicken", 2, 150),
            ("Rice", 1, 200),
            ("Oil", 1, 250),
            ("Salt", 1, 5)
            ]
        self.cart = []
    
    def add_to_cart(self):
        try:
            self.name = input("Enter the products name: ")
            self.quantity = float(input("Enter the quantity: "))
            self.price = float(input("Enter the price: "))
            self.found_item = None
            for item in self.list:
                if item[0] == self.name and item[1] >= self.quantity:
                    self.found_item = item
                    break

            if self.found_item:
                if self.balance >= self.price:
                    self.cart.append({"name": self.name, "quantity": self.quantity, "price": self.price})
                    self.list.remove(self.found_item)
                    self.balance -= self.price
                    print(f"The item {self.name} is successfully added to cart. New balance is {self.balance}")
                else:
                    print("Insufficient balance. Item not added.")
            else: 
                print(f"Item {self.name} not found in the list. Insufficinet quantity")
        except ValueError:
            print("An errror happend. Try again..")
            self.add_to_cart()
    
    def compare_prices(self):
        print("Price comparison between List and Cart items prices:")
        for cart_item in self.cart:
            for list_item in self.list:
                if cart_item['name'] == list_item['name']:
                    self.difference = ((cart_item['price'] - list_item['price'])/list_item['price'])*100
                    if self.difference > 0:
                        print(f"{cart_item['name']} is {abs(self.difference)} % more expensive then {list_item['name']}")
                    elif self.difference < 0:
                        print(f"{cart_item['name']} is {abs(self.difference)} % cheaper then {list_item['name']}")
                    else:
                        print("Prices are same")
                        break
    
    def plot_prices(self):
        self.items_in_cart = [item["name"] for item in self.cart]
        self.prices_in_cart = [item["price"] for item in self.cart]
        
        # الحصول على الأسعار الأصلية بناءً على العناصر في السلة
        self.original_prices = [next(item["price"] for item in self.list if item["name"] == cart_item["name"]) 
                                for cart_item in self.cart]
        
        # حساب الفرق بين السعر في السلة والسعر الأصلي
        self.price_difference = [cart_price - original_price 
                                for cart_price, original_price in zip(self.prices_in_cart, self.original_prices)]

        # رسم البياني
        plt.bar(self.items_in_cart, self.price_difference)
        plt.xlabel("Items")
        plt.ylabel("Price Difference")
        plt.title("Price Comparison: Cart vs List")
        plt.show()


deneme = ShoppingCart()
while True:
    choise = int(input("1 or 2?"))
    if choise == 1:
        deneme.add_to_cart()
    elif choise == 2:
        break

#deneme.compare_prices()
deneme.plot_prices()