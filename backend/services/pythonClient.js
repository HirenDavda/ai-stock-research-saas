const axios = require("axios");

const PYTHON_SERVICE_URL =
  process.env.PYTHON_SERVICE_URL || "http://localhost:8000";

 /**
 * Send question to Python RAG service
 */

 async function askPython(question, documentId = null) {
    try {
        const response = await axios.post(
            `${PYTHON_SERVICE_URL}/api/ask`,
            {
                question,
                document_id: documentId,
            },
            {
                timeout: 60000,
            }
        );
        return response.data;
    } catch (error) {
        console.error(
            "Python service error:",
            error?.response?.data || error.message
        )
        throw new Error("AI service unavailable");
    }
 }

 module.exports = {
    askPython,
 }