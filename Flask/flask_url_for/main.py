from flask import Flask,render_template

# app = Flask(__name__, static_url_path='/public') # this is how you change static url path
app = Flask(__name__, static_folder='assets',static_url_path='/static') # this is how you static folder location

@app.route("/")
def hello_world():
    return render_template('index.html')

app.run(port=4000,debug=True)