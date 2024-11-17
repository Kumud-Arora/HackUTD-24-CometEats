import React, { useState } from 'react';
import { useLocation } from 'react-router-dom';

function Order() {
    const location = useLocation();
    const [orderNumber, setOrderNumber] = useState(null);
    const [orderStatus, setOrderStatus] = useState(null);
    const { cart } = location.state || { cart: [] };

    const placeOrder = async () => {
        const response = await fetch('http://localhost:5000/api/order', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ cart }),
        });
        const data = await response.json();
        if (data.success) {
            setOrderNumber(data.orderNumber);
        } else {
            alert('Failed to place order');
        }
    };

    const checkStatus = async () => {
        if (!orderNumber) return;
        const response = await fetch(`http://localhost:5000/api/order-status?orderNumber=${orderNumber}`);
        const data = await response.json();
        setOrderStatus(data.status);
    };

    return (
        <div>
            <h2>Your Order</h2>
            <ul>
                {cart.map((item, index) => (
                    <li key={index}>{item.name} - ${item.price}</li>
                ))}
            </ul>
            <button onClick={placeOrder}>Place Order</button>
            {orderNumber && (
                <div>
                    <p>Your order number is: {orderNumber}</p>
                    <button onClick={checkStatus}>Check Order Status</button>
                    {orderStatus && <p>Order Status: {orderStatus}</p>}
                </div>
            )}
        </div>
    );
}

export default Order;
