import React, { useState } from 'react';
import './Header.css';

function Header({ isLoggedIn, setIsLoggedIn }) {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleLogin = async (e) => {
        e.preventDefault();
        const response = await fetch('http://localhost:5000/api/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password }),
        });
        const data = await response.json();
        if (data.success) {
            setIsLoggedIn(true);
        } else {
            alert(data.message);
        }
    };

    return (
        <header style={{ textAlign: "center", margin: "2rem" }}>
            <h1>CometEats</h1>
            {!isLoggedIn ? (
                <form onSubmit={handleLogin}>
                    <div>
                        <label htmlFor="username" style={{ fontSize: "1.5rem" }}>Username </label>
                        <input 
                            type="text" 
                            id="username" 
                            name="username" 
                            placeholder="Enter your username" 
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                        />
                    </div>
                    <div style={{ marginTop: "1rem" }}>
                        <label htmlFor="password" style={{ fontSize: "1.5rem" }}>Password </label>
                        <input 
                            type="password" 
                            id="password" 
                            name="password" 
                            placeholder="Enter your password" 
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                        />
                    </div>
                    <div style={{ marginTop: "1rem" }}>
                        <button type="submit">Login</button>
                    </div>
                </form>
            ) : (
                <h2>Welcome, {username}!</h2>
            )}
        </header>
    );
}

export default Header;
