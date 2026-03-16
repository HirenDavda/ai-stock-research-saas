// Express helps us create a web server easily
const express = require('express');

// CORS allows our frontend (website) to talk to our backend
const cors = require('cors');

// Create a new Express application
const app = express();

// Allow requests from other applications (like our frontend)
app.use(cors());

// Allow server to understand JSON data sent in requests
app.use(express.json());

// This is a simple test route
// When someone visits http://localhost:5000
// the server will send a message back to the browser
app.get('/', (req, res) => {
    res.send("Stock AI Backend Running");
});

// Start the server on port 5000
// Port is like a door where requests enter the server
app.listen(5000, () => {
    console.log("Server running on port 5000")
});