from flask import Flask,jsonify

app = Flask(__name__) 



@app.route("/")
def hello_world():
    marks = {
        "Karan": 90,
        "Pradip": 58,
        "Jesmine": 59,
        "Payal":55
    }
    my_list= []
    for i in range(20):
        my_list.append(i)
    return jsonify(my_list)

app.run(port=4000,debug=True)