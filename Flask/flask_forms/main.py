from flask import Flask,render_template,request
import os
app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def hello_world():
    # print(request.method)
    # print(request.form)

    if(request.method == 'POST'):
       # Semulating Database
       if(os.path.exists("database.md") != True):
            with open("database.md", "w") as f:
                f.write("| Name | Email |\n")
                f.write("| --------------------- | -------------------------- |\n")
                f.write(f"| {request.form['name']} | {request.form['email']}|")
            return render_template('contact.html')
       else:
            with open("database.md", "a") as f:
                f.write(f"\n| {request.form['name']} | {request.form['email']}|")
    else:
        return render_template('contact.html')

app.run(debug=True)