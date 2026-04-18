const express = require("express");
const router = express.Router();
const axios = require("axios");


router.get("/", (req, res) => {
    res.send("Chat API is running. Use POST request.");
});

router.post("/", async (req, res) => {
    
    console.log("CHAT ROUTE HIT");

    try {
        const { question } = req.body;

        // 1️⃣ Validate input
        if (!question) {
            return res.status(400).json({
                error: "question is required"
            });
        }
        
        console.log("User question:", question);

        // 2️⃣ Use environment variable
        const PYTHON_SERVICE_URL =
            process.env.PYTHON_SERVICE_URL || "http://localhost:8000";

        const response = await axios.post(
            `${PYTHON_SERVICE_URL}/api/chat/ask`,
            {
                question: question
            },
            {
                timeout: 60000
            }
        );

        console.log("AI RESPONSE RECEIVED");

        res.json(response.data);
    } catch (error) {
        
        console.error("Error:", error.message);

        // 3️⃣ Better error handling
        const message =
            error?.response?.data?.detail ||
            error.message ||
            "AI service failed";

        res.status(500).json({ 
            error: message
        })
    }
});

module.exports = router;