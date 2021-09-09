from flask import Flask, app, render_template, request

app = Flask(__name__)

@app.router("/")
def index():
    name = request.args.get("name")
    return render_template("index.html", name = name)