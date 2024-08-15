// Toggle Navigation Menu
document.getElementById('toggleMenu').addEventListener('click', function() {
    var navbar = document.getElementById('navbar');
    var ul = navbar.querySelector('ul');
    if (ul.style.display === 'block') {
        ul.style.display = 'none';
    } else {
        ul.style.display = 'block';
    }
});

// Show an Alert
document.getElementById('alertButton').addEventListener('click', function() {
    alert('Button clicked!');
});

// Example of Dynamic Content Update
document.addEventListener('DOMContentLoaded', function() {
    var heroSection = document.querySelector('.hero p');
    heroSection.innerHTML = 'Discover our amazing services and products!';
});

// scripts.js

document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Get the values from the form
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const errorMessage = document.getElementById('error-message');

    // Basic validation (you can expand this with more rules)
    if (username === '' || password === '') {
        errorMessage.textContent = 'Please fill in both fields.';
        errorMessage.style.display = 'block';
    } else {
        // Simulate a login process (replace with real authentication logic)
        if (username === 'user' && password === 'pass') {
            alert('Login successful!');
            errorMessage.style.display = 'none';
            // Redirect or handle successful login here
        } else {
            errorMessage.textContent = 'Invalid username or password.';
            errorMessage.style.display = 'block';
        }
    }
});
