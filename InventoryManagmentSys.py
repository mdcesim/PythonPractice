# Inventory Management System
# - Create a program that manages a list of items with their prices and stock levels.
# - Add functionality to restock, sell items, and generate sales reports.
# - Use dictionaries to store item details.

inventory = {
    "apple": {"price": 1.0, "stock": 3, "sales": 2},
    "banana": {"price": 1.5, "stock": 5, "sales": 5},
    "orange": {"price": 0.5, "stock": 8, "sales":4},
}

def display_inventory():
    print(f"Current Inventory: ")
    for item, details in inventory.items():
        print(f"{item.title()}: Price: ${details['price']}, Stock: {details['stock']} kg, Sales: {details['sales']}")

def restock_item():
    item_name = input("Enter the item name you want to restock: ")
    if item_name in inventory:
        quantity = int(input(f"Enter the number of itmes you want to add to {item_name} stock: "))
        if quantity > 0:
            inventory[item_name]["stock"] += quantity
            print(f"Successfully added {quantity} to {item_name}. New stock: {inventory[item_name]['stock']}")
        else: 
            print(f"Quantity must be a positive number.")
    else: 
        print(f"{item_name} is not in the inventory")
    display_inventory()

def sell_items():
    item_name = input("Enter the item name you want to sell: ")
    quantity = int(input("Enter the quantitiy of items you want to sell: "))
    if item_name in inventory:
        if quantity > 0 and inventory[item_name]['stock'] >= quantity:       
            inventory[item_name]['sales'] += quantity
            inventory[item_name]['stock'] -= quantity
            total = quantity*(inventory[item_name]['price'])
            print(f"Successfully sold {quantity} of {item_name}. Total = ${total}")
        else: 
            print(f"No enough {item_name} available..")
    else:
        print(f"{item_name} is not in the inventory")
    display_inventory()

def sales_report():
    print(f"Total Sales Report: \n")
    total_revenue = 0
    items_sold = 0
    for item, detail in inventory.items():
        item_sales = detail["sales"]
        item_revenue = item_sales*detail["price"]
        total_revenue += item_revenue
        items_sold += item_sales
        print(f"{item.title()} -- Sold: {item_sales}, Revenue: {item_revenue}")
    print("\n")
    print(f"Total Sales: {items_sold}, Total Revenue: {total_revenue}")
    print("\n")

def main():
    while True:
        print("Inventory Management System")
        print("1. Display Inventory")
        print("2. Restock an Item")
        print("3. Sell an Item")
        print("4. Generate Sales Report")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            display_inventory()
        elif choice == "2":
            restock_item()
        elif choice == "3":
            sell_items()
        elif choice == "4":
            sales_report()
        elif choice == "5":
            print("Exiting the Inventory Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

main()