from flask import Flask,render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    # name= "KARAN SWARNAKAR"
    # token= 499
    name = request.args["name"]
    token = request.args["tokens"]
    return render_template('index.html',name=name, token=token)



app.run(port=4000,debug=True)