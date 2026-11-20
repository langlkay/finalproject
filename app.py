from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    message = "Welcome to my app"
    return render_template("index.html", message=message)

@app.route("/upload")
def upload():
    photo = request.files["photo"]
    title = request.form["title"]
    medium = request.form["medium"]
    filename = request.form["filename"]
    message = "this is my app"
    artwork = {
        "title": title,
        "medium": medium,
        "photo": filename
    }
    return render_template("uploads.html", message=message)


