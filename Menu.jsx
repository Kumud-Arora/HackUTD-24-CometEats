import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

function Menu({ restaurant }) {
    const [menu, setMenu] = useState([]);
    const [cart, setCart] = useState([]);
    const navigate = useNavigate();

    useEffect(() => {
        fetch(`http://localhost:5000/api/menu?restaurant=${restaurant}`)
            .then(response => response.json())
            .then(data => setMenu(data));
    }, [restaurant]);

    const addToCart = (item) => {
        setCart([...cart, item]);
    };

    const checkout = () => {
        // Here you would typically send the cart to the backend
        // For this example, we'll just navigate to the order page
        navigate('/order', { state: { cart } });
    };

    return (
        <div>
            <h2>{restaurant === 'panda' ? 'Panda Express' : 'Einstein Bros. Bagels'} Menu</h2>
            <ul>
                {menu.map((item, index) => (
                    <li key={index}>
                        {item.name} - ${item.price}
                        <button onClick={() => addToCart(item)}>Add to Cart</button>
                    </li>
                ))}
            </ul>
            <h3>Cart</h3>
            <ul>
                {cart.map((item, index) => (
                    <li key={index}>{item.name} - ${item.price}</li>
                ))}
            </ul>
            <button onClick={checkout}>Checkout</button>
        </div>
    );
}

export default Menu;
