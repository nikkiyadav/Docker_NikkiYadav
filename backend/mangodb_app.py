from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# Connect to MongoDB Atlas
MONGODB_URI = os.getenv("MONGODB_URI")

if not MONGODB_URI:
    raise ValueError("MONGODB_URI is missing from .env file")

client = MongoClient(
    MONGODB_URI,
    serverSelectionTimeoutMS=10000
)

db = client["tutedude"]
collection = db["students"]


# Display frontend form
@app.route("/", methods=["GET"])
def home():
    return render_template("form.html")


# Handle form submission
@app.route("/submit", methods=["POST"])
def submit():

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    course = request.form.get("course", "").strip()

    if not name or not email or not course:
        return render_template(
            "form.html",
            error="Please fill in all fields.",
            name=name,
            email=email,
            course=course
        )

    student_data = {
        "name": name,
        "email": email,
        "course": course
    }

    try:
        # Check MongoDB Atlas connection
        client.admin.command("ping")

        print("MongoDB Atlas connected successfully!")

        # Insert student data
        collection.insert_one(student_data)

        return redirect(url_for("success"))

    except Exception:
        app.logger.exception("MongoDB submission failed")

        return render_template(
            "form.html",
            error="Submission failed. Please try again.",
            name=name,
            email=email,
            course=course
        )


# Success page
@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)