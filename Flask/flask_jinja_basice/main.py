from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():

    marks = {
        'Karan': 20,
        'Pradip': 18,
        'Jesmine': 20,
        'Sathi': 14,
        'Payal': 11,
        'Sona': 20,
    }

    return render_template('index.html',marks=marks)

app.run(debug=True)