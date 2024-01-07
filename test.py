menu = {
    1: {"name": 'espresso', "price": 1.99},
    2: {"name": 'coffee', "price": 2.50},
    3: {"name": 'cake', "price": 2.79},
    4: {"name": 'soup', "price": 4.50},
    5: {"name": 'sandwich', "price": 4.99}
}

def calculate_subtotal(order):
    """Calculates the subtotal of an order"""
    print('Calculating bill subtotal...')
    subtotal = 0
    for item in order:
        subtotal += item['price']
    return subtotal

def calculate_tax(subtotal):
    """Calculates the tax of an order"""
    print('Calculating tax from subtotal...')
    return round(subtotal * 0.15, 2)

def summarize_order(order):
    """Summarizes the order"""
    subtotal = calculate_subtotal(order)
    tax = calculate_tax(subtotal)
    total = round(subtotal + tax, 2)
    names = [item["name"] for item in order]
    return names, total

def print_order(order):
    """Prints out the items in an order"""
    print('You have ordered ' + str(len(order)) + ' items')
    items = [item["name"] for item in order]
    print(items)

def display_menu():
    """Displays the menu"""
    print("------- Menu -------")
    for selection in menu:
        print(f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")
    print()

def take_order():
    """Creates an order by prompting the user to select menu items"""
    display_menu()
    order = []
    count = 1
    while count <= 3:
        try:
            item = int(input('Select menu item number ' + str(count) + ' (from 1 to 5): '))
            if item in menu:
                order.append(menu[item])
                count += 1
            else:
                print("Invalid selection. Please choose a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    return order

def main():
    order = take_order()
    print_order(order)

    subtotal = calculate_subtotal(order)
    print("Subtotal for the order is: " + str(subtotal))

    tax = calculate_tax(subtotal)
    print("Tax for the order is: " + str(tax))

    names, total = summarize_order(order)
    print("Items ordered:", names)
    print("Total cost (including tax):", total)

if __name__ == "__main__":
    main()
