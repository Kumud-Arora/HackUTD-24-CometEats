from flask import Flask, request, jsonify
from flask_cors import CORS
import csv

app = Flask(__name__)
CORS(app)

# Copy all your existing functions here (user_authentication, payment, check_order_status, etc.)

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    users = {
        'User1': 'Password1',
        'User2': 'Password2',
    }
    
    if username in users and users[username] == password:
        return jsonify({"success": True, "message": "Login successful"})
    else:
        return jsonify({"success": False, "message": "Invalid username or password"}), 401

@app.route('/api/menu', methods=['GET'])
def get_menu():
    restaurant = request.args.get('restaurant')
    if restaurant == 'panda':
        menu = read_menu_from_csv('panda_menu.csv')
    elif restaurant == 'einstein':
        menu = read_menu_from_csv('einstein_menu.csv')
    else:
        return jsonify({"error": "Invalid restaurant"}), 400
    return jsonify(menu)

@app.route('/api/order', methods=['POST'])
def place_order():
    data = request.json
    cart = data.get('cart')
    total_amount = calculate_total(cart)
    
    # Here you would typically process the payment and create an order
    # For this example, we'll just return a success message
    return jsonify({
        "success": True,
        "message": f"Order placed successfully. Total amount: ${total_amount:.2f}",
        "orderNumber": 101
    })

@app.route('/api/order-status', methods=['GET'])
def get_order_status():
    order_num = int(request.args.get('orderNumber'))
    status = check_order_status(order_num)
    return jsonify({"status": status})

if __name__ == '__main__':
    app.run(debug=True)
