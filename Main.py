import csv

def user_authentication():
    users = {
        'User1': 'Password1',
        'User2': 'Password2',
    }

    print('Enter your USERNAME')
    username = input()
    print('Enter your PASSWORD')
    password = input()

    if username in users and users[username] == password:
        print('Match. Continue')
        return True
    else:
        print('Invalid Username or Password')
        return False

def payment(total_amount):
    print('Enter your card number: ')
    card_num = input()
    print('Enter your CVV: ')
    cvv = input()
    print("Enter your card's expiry date (MM/YY): ")
    expiry_date = input()

    if len(card_num) == 10 and len(cvv) == 3 and float(total_amount) > 0:
        print(f'Payment of ${total_amount:.2f} processed successfully!')
        return True
    else:
        print('Payment failed. Please check your details and try again.')
        return False

orders = {
    101: "Order received",
    102: "Order completed",
    103: "Order being prepared"
}

def check_order_status(order_num):
    return orders.get(order_num, "Order not found")

def order_status(order_num, status):
    if order_num in orders:
        orders[order_num] = status
        return f"Order {order_num} status updated to '{status}'"
    return "Order not found"



def read_menu_from_csv(filename):
    menu = []
    try:
        with open(filename, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                menu.append({"name": row['name'], "price": float(row['price'])})
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    except csv.Error as e:
        print(f"Error reading CSV file: {e}")
    return menu

def display_menu(menu):
    print("Available Menu:")
    for i, item in enumerate(menu):
        print(f"{i + 1}. {item['name']} - ${item['price']:.2f}")

def select_items(menu):
    cart = []
    while True:
        display_menu(menu)
        choice = input("Enter the item number to add to cart (or 'done' to finish): ").strip().lower()
        if choice == "done":
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(menu):
            cart.append(menu[int(choice) - 1])
            print(f"{menu[int(choice) - 1]['name']} added to cart.")
        else:
            print("Invalid choice. Please try again.")
    return cart

def calculate_total(cart):
    total = sum(item["price"] for item in cart)
    return total

# Main Function
if __name__ == '__main__':
    print("Welcome to the Food Ordering System!")

    if not user_authentication():
        exit()

    # Read menus from CSV files
    panda_menu = read_menu_from_csv('panda_menu.csv')
    einstein_menu = read_menu_from_csv('einstein_menu.csv')

    # Let user choose restaurant
    while True:
        restaurant_choice = input("Choose a restaurant (1 for Panda Express, 2 for Einstein Bros. Bagels): ").strip()
        if restaurant_choice == '1':
            chosen_menu = panda_menu
            restaurant_name = "Panda Express"
            break
        elif restaurant_choice == '2':
            chosen_menu = einstein_menu
            restaurant_name = "Einstein Bros. Bagels"
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    print(f"\nYou've chosen to order from {restaurant_name}.")
    user_cart = select_items(chosen_menu)

    if user_cart:
        total_amount = calculate_total(user_cart)
        print("\nYour Order Summary:")
        for item in user_cart:
            print(f"- {item['name']} (${item['price']:.2f})")
        print(f"Total Amount: ${total_amount:.2f}")

        if payment(total_amount):
            print("Thank you for your order!")
            print("Your order number is 101.")
            order_num = int(input("Enter your order number to check status: "))
            print(check_order_status(order_num))
        else:
            print("Payment was not successful. Please try again.")
    else:
        print("No items selected.")
