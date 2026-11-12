
const express = require("express");
const path = require("path");

const app = express();
const PORT = 3000;

// Parse form data
app.use(express.urlencoded({ extended: true }));

// Serve frontend files
app.use(express.static(path.join(__dirname, "public")));

// Flask backend URL
    const BACKEND_URL =
    process.env.BACKEND_URL || "http://127.0.0.1:5000";

// Handle form submission
app.post("/submit", async (req, res) => {
    try {
        const { name, email, course } = req.body;

        const response = await fetch(`${BACKEND_URL}/submit`, {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: new URLSearchParams({
                name,
                email,
                course
            })
        });

        // Flask redirects to /success after successful insertion
        if (response.ok && response.url.endsWith("/success")) {
            return res.send(`
                <h2>Student details submitted successfully!</h2>
                <a href="/">Go Back</a>
            `);
        }

        return res.status(400).send(`
            <h2>Submission failed. Please try again.</h2>
            <a href="/">Go Back</a>
        `);

    } catch (error) {
        console.error("Backend connection error:", error);

        res.status(500).send("Unable to connect to Flask backend.");
    }
});

// Start Express server
app.listen(PORT, "0.0.0.0", () => {
    console.log(`Frontend running on port ${PORT}`);
});
