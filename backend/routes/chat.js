const express = require("express");
const router = express.Router();
const axios = require("axios");

const { success, failure } = require("../utils/apiResponse");

router.get("/", (req, res) => {
    res.send("Chat API is running. Use POST request.");
});

router.post("/", async (req, res) => {
    
    console.log("CHAT ROUTE HIT");

    try {
        const { question, documentId } = req.body;

        console.log("Request ID:", req.requestId);

        // 1️⃣ Validate input
        if (!question) {
            return res.status(400).json({
                error: "question is required"
            });
        }
        
        console.log("User question:", question);
        console.log("Document ID:", documentId);

        // 2️⃣ Use environment variable
        const PYTHON_SERVICE_URL =
            process.env.PYTHON_SERVICE_URL || "http://localhost:8000";

        const response = await axios.post(
            `${PYTHON_SERVICE_URL}/api/chat/ask`,
            {
                question: question,
                document_id: documentId || null
            },
            {
                timeout: 60000
            }
        );

        console.log("AI RESPONSE RECEIVED");

        return res.json({
            success: true,
            data: response.data,
            error: null,
            requestId: req.requestId
        });

    } catch (error) {
        
        console.error("Error:", error.message);

        // 3️⃣ Better error handling
        const message =
            error?.response?.data?.detail ||
            error.message ||
            "AI service failed to process question";
        
        return res.status(500).json({
            success: false,
            data: null,
            error: message,
            requestId: req.requestId
        });
    }
});

module.exports = router;