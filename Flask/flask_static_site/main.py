from flask import Flask,render_template

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/survices")
def services():
    return render_template("survices.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

app.run(debug=True)