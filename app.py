from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    message = "Welcome to my app"
    return render_template("index.html", message=message)

@app.route("/upload", methods = ["GET", "POST"])
def upload():
    message = "this is my app"
    artwork = None
    
    if request.method == "POST":
        photo = request.files.get["photo"]
        title = request.form.get["title"]
        medium = request.form.get["medium"]
        filename = ""

        message = "this is my app"
        artwork = {
            "title": title,
            "medium": medium,
            "photo": filename
        }
        message = "UPLOADED!!"
    return render_template("form.html", message=message, artwork=artwork)


