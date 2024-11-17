import './Header.css'; // Import the CSS file

function Header() {
    return (
        <header style={{ textAlign: "center", margin: "2rem" }}>
            <h1>CometEats</h1>
            <form>
                <div>
                    <label htmlFor="username" style={{ fontSize: "1.5rem" }}>Username </label>
                    <input type="text" id="username" name="username" placeholder="Enter your username" />
                </div>
                <div style={{ marginTop: "1rem" }}>
                    <label htmlFor="password" style={{ fontSize: "1.5rem" }}>Password </label>
                    <input type="password" id="password" name="password" placeholder="Enter your password" />
                </div>
                <div style={{ marginTop: "1rem" }}>
                    <button type="submit">Login</button>
                </div>
            </form>
        </header>
    );
}

export default Header;