from flask import Flask, session, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/form',methods = ["GET","POST"])
def form():
    if request.method == "POST":
        form_data = request.form
        input = form_data["input"]
        number = form_data["number"]
        if input:
            return "input is :" + input
        if number:
            return "Number is :" + number

        else:
            return "numbar is: "+ number +"input is:" +input


    return render_template("form.html",**locals())



if __name__ == '__main__':
    app.run()
