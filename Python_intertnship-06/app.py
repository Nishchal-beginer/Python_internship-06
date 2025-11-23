from flask import Flask, render_template, request, redirect, url_for, flash
import csv
import os

app = Flask(__name__)
# Replace this with a secure random key in production
app.secret_key = "change-this-to-a-secure-random-string"

@app.route("/")
def index():
    # you could pass dynamic data like projects here
    projects = [
        {"title": "Fresh Vision", "desc": "A Machine Learning project on Fruits classification", "link": "https://github.com/Nishchal-beginer/Fresh-Vision"},
        {"title": "Spoti-fi", "desc": "A Music Library using HTML, CSS, JS", "link": "https://nishchal-beginer.github.io/Spoti-fi/"},
    ]
    return render_template("index.html", projects=projects)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        # simple server-side validation
        if not name or not email or not message:
            flash("Please fill in all fields.", "error")
            return redirect(url_for("contact"))

        # save to CSV (append mode). Create data dir if needed.
        os.makedirs("data", exist_ok=True)
        csv_path = os.path.join("data", "contacts.csv")
        with open(csv_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([name, email, message])

        flash("Thanks — your message was received!", "success")
        return redirect(url_for("index"))

    # GET -> show the contact form
    return render_template("contact.html")

if __name__ == "__main__":
    # debug=True for development only
    app.run(debug=True, host="0.0.0.0", port=5000)
