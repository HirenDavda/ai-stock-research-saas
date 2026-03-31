const express = require("express");
const router = express.Router();
const axios = require("axios");

router.get("/", (req, res) => {
    res.send("Chat API is running. Use POST request.");
});

router.post("/", async (req, res) => {
    
    console.log("CHAT ROUTE HIT");

    try {
        const question = req.body.question;
        
        console.log("User question:", question);

        const response = await axios.post(
            "http://localhost:8000/chat",
            {
                question: question
            }
        );
        console.log("AI RESPONSE RECEIVED"); 
        res.json(response.data);
    } catch (error) {
        console.error("Error:", error.message);
        res.status(500).json({ error: "AI service failed to process question" })
    }
});

module.exports = router;