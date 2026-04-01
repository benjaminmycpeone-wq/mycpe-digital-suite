from flask import Flask, send_file, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def index():
    return send_file("index.html")

@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory(".", filename)

@app.route("/health")
def health():
    return {"status": "ok"}
