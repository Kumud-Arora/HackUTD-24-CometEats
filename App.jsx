import { Routes, Route } from 'react-router-dom';
import React, { useState } from 'react'
import Header from './Header.jsx'
import Menu from './Menu.jsx'
import Order from './Order.jsx'

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [selectedRestaurant, setSelectedRestaurant] = useState(null);

  return (
    <div style={{ border: "50px solid white", height: "87vh", width: "171vh", margin: "0" }}>
      <Header isLoggedIn={isLoggedIn} setIsLoggedIn={setIsLoggedIn} />
      {isLoggedIn && !selectedRestaurant && (
        <div>
          <h2>Choose a restaurant:</h2>
          <button onClick={() => setSelectedRestaurant('panda')}>Panda Express</button>
          <button onClick={() => setSelectedRestaurant('einstein')}>Einstein Bros. Bagels</button>
        </div>
      )}
      {isLoggedIn && selectedRestaurant && (
        <Routes>
          <Route path="/" element={<Menu restaurant={selectedRestaurant} />} />
          <Route path="/order" element={<Order />} />
        </Routes>
      )}
    </div>
  );
}

export default App;
