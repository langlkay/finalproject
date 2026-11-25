import os
import json
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename


app = Flask(__name__)

@app.route("/")
def home():
    message = "Welcome to my app"
    artworks = load_art()
    return render_template("index.html", message=message, artworks=artworks)

@app.route("/upload", methods = ["GET", "POST"])
def upload():
    message = "Upload Artwork!"
    artwork = None
    artworks = []

    if request.method == "POST":
       

        photo = request.files.get("artwork-image")
        title = request.form.get("name")
        medium = request.form.get("medium")

        filename = secure_filename(photo.filename)
        photo.save(os.path.join("static/uploadedArt", filename))

        message = "this is my app"
        artwork = {
            "title": title,
            "medium": medium,
            "photo": filename
        }
        
        artworks.append(artwork)

        message = "UPLOADED!!"
        return render_template("index.html", message=message, artwork=artwork, artworks=artworks)
    return render_template("form.html", message=message, artwork=artwork, artworks=artworks)


def load_art():
    with open("artworks.json", "r") as file:
        artworks = json.load(file)

    return artworks