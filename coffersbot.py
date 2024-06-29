menu = {
    "1": {"item": "Burger", "price": 5.99},
    "2": {"item": "Pizza", "price": 8.99},
    "3": {"item": "Pasta", "price": 7.49},
    "4": {"item": "Salad", "price": 4.99},
    "5": {"item": "Soda", "price": 1.99}
}


def print_menu():
    print("Menu:")
    for item_num, item_data in menu.items():
        print(f"{item_num}: {item_data['item']} - ${item_data['price']}")


def take_order():
    order = []
    print_menu()

    while True:
        item_choice = input("Enter the number of the item you want to order (or 'q' to quit):\n " )

        if item_choice.lower() == 'q':
            break

        if item_choice in menu:
            order.append(menu[item_choice]["item"])
        else:
            print("Invalid item number. Please choose a valid item from the menu.")

    return order


def calculate_total(order):
    total = sum(menu[item_choice]["price"] for item_choice in order)
    return total


print("Welcome to Coffee Coffers cafe! Am Bee ready to take yur order.")
customer_order = take_order()

if customer_order:
    print("\nYour order:")
    for item in customer_order:
        print(item)

    total_price = calculate_total(customer_order)
    print(f"Total: ${total_price:.2f}")
else:
    print("No items ordered. Have a great day!")
