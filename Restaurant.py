# Restaurant Bill Calculator
# - Simulate a restaurant ordering system where the user selects items from a menu.
# - Calculate the total bill, including tax and tip.
# - Optionally, split the bill between multiple people.

menu = { 
    "hamburger": {"price": 5, "quantity": 10, "sales": 0},
    "pizza": {"price": 6, "quantity": 10, "sales": 0},
    "chicken": {"price": 3, "quantity": 10, "sales": 0},
    "beef": {"price": 7, "quantity": 10, "sales": 0}, 
}

def display_menu():
    print(f"   The Menu")
    print(f"Hamburger -- {menu['hamburger']['price']} $")
    print(f"Chicken ---- {menu['chicken']['price']} $")
    print(f"Pizza ------ {menu['pizza']['price']} $")
    print(f"Beef ------- {menu['beef']['price']} $")

def sell_item():
    print("Please select what you will take form the menu below..")
    display_menu()
    selection = input("Please enter the name of the food you will take: ").lower()
    if selection not in menu:
        print(f"No {selection} available in our menu.")
    else:
        while True:
            quantity = int(input(f"How many {selection}s do you want? "))
            if quantity > 0:
                break
            else:
                print("Quantity must be a positive number")
    if selection in menu:
        if selection == "hamburger":
            if quantity <= menu["hamburger"]['quantity']:
                menu["hamburger"]['quantity'] -= quantity
                menu["hamburger"]['sales'] += quantity
                print(f"Ordered successfully. You ordered {quantity} pieces of {selection}")
            else: 
                print(f"No Hamburger enough. The quantity of Hamburgers we have is {menu['hamburger']['quantity']}")
        elif selection == "chicken":
            if quantity <= menu["chicken"]['quantity']:
                menu["chicken"]['quantity'] -= quantity
                menu["chicken"]['sales'] += quantity
                print(f"Ordered successfully. You ordered {quantity} pieces of {selection}")
            else: 
                print(f"No ckicken enough. The quantity of chicken we have is {menu['chicken']['quantity']}")
        elif selection == "pizza":
            if quantity <= menu["pizza"]['quantity']:
                menu["pizza"]['quantity'] -= quantity
                menu["pizza"]['sales'] += quantity
                print(f"Ordered successfully. You ordered {quantity} pieces of {selection}")
            else: 
                print(f"No pizza enough. The quantity of pizza we have is {menu['pizza']['quantity']}")
        elif selection == "beef":
            if quantity <= menu["beef"]['quantity']:
                menu["beef"]['quantity'] -= quantity
                menu["beef"]['sales'] += quantity
                print(f"Ordered successfully. You ordered {quantity} pieces of {selection}")

            else: 
                print(f"No beef enough. The quantity of beef we have is {menu['beef']['quantity']}")
        else:
            print("Invalid selection. Please try again.")
        if quantity <= menu["hamburger"]['quantity']:
            total_price = menu[selection]['price']*quantity
            print("Order Summary: ")
            print("Item Name -- Quantity -- Price")
            print(f"{selection} ----- {quantity} ----- {menu[selection]['price']}$")
            print(f"Your total price is {total_price}$")

def main():
    while True:
        print("Welcome To Cesim Restuarant! Take a look to our menu")
        display_menu()
        print()
        while True:
            choice = input("Please Choose Your Operation:\n1.) Order\n2.) Exit\n")
            if choice == "1":
                sell_item()
            elif choice == "2":
                print(f"Thank you for choosing us! Have a nice day.")
                break
            else: 
                print("Invalid Selection! Please try again")
        another_order = input("Do you want to do another order? (yes or no) ").lower()
        if another_order != "yes":
            print(f"Thank you! Goodbye.")
            break

main()