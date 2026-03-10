from flask import Flask, render_template, request
import os
import uuid
import csv

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
CSV_FILE = "submissions.csv"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Create CSV file if it doesn't exist
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "ApplicationID",
            "Name",
            "Email",
            "Phone",
            "Position",
            "ResumeFile"
        ])


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    position = request.form["position"]

    file = request.files["resume"]

    application_id = str(uuid.uuid4())[:8]

    filename = application_id + "_" + file.filename
    filepath = os.path.join(UPLOAD_FOLDER, filename)

    file.save(filepath)

    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            application_id,
            name,
            email,
            phone,
            position,
            filename
        ])

    return render_template(
        "success.html",
        application_id=application_id
    )


@app.route("/dashboard")
def dashboard():

    data = []

    with open(CSV_FILE, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            data.append(row)

    return render_template("dashboard.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
