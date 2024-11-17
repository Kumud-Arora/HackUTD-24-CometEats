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


def payment():
    print('Enter your card number: ')
    card_num = input()
    print('Enter your CVV: ')
    cvv = input()
    print("Enter your card's expiry date: ")
    expiry_date = input()
    print('Enter your total amount: ')
    total_amount = input()

    if len(card_num) == 10 and len(cvv) == 3 and float(total_amount) > 0:
        print('Payment of ${total_amount} processed successfully!')
    else:
        print('Payment failed. Please check your details and try again.')

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
        return "Order {status} status updated to '{status}'"
    return "Order not found"



# Main Function
if __name__ == '__main__':
    i = 0

    while i < 4:
        if i == 0:
            if user_authentication():
                i += 1
            else:
                print("Invalid Username or Password")
                break

        elif i == 1:
            payment()
            i += 1

        elif i == 2:
            print("Enter your order number:")
            order_num = int(input())
            print(check_order_status(order_num))
            i += 1

