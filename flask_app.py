from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for flashing error messages

#  MongoDB Atlas connection string (replace with your actual URI)
#MONGO_URI = "mongodb+srv://ankya:12345@cluster1.mongodb.net/mydatabase"
#MONGO_URI = "mongodb+srv://ankya:12345@cluster1.mongodb.net/mydatabase?retryWrites=true&w=majority"
MONGO_URI = "mongodb+srv://ankya:12345@cluster1.maxr1nv.mongodb.net/mydatabase?retryWrites=true&w=majority&appName=Cluster1"


client = MongoClient(MONGO_URI)
db = client["mydatabase"]          # database
collection = db["users"]           # collection

# Show form to insert email and name
@app.route("/", methods=["GET"])
def form():
    return render_template("form.html")

# Handle form submission
@app.route("/submit", methods=["POST"])
def submit():
    try:
        name = request.form.get("name")
        email = request.form.get("email")

        if not name or not email:
            flash("Name and Email are required!")
            return render_template("form.html")

        # Insert into MongoDB
        collection.insert_one({"name": name, "email": email})

        # Redirect to success page
        return redirect(url_for("success"))

    except Exception as e:
        # Show error on the same page
        flash(f"Error: {str(e)}")
        return render_template("form.html")

# Success page
@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
