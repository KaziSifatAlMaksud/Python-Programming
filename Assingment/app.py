from flask import Flask, request,render_template
import pymongo
app = Flask(__name__)
mycliend = pymongo.MongoClient("mongodb://localhost:27017/assingment")
mydb = mycliend["usersingup"]
mycol = mydb["data"]

@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/singup',methods=["GET","POST"])
def singup():
    if request.method == "post":
        form_data = request.form()
        username = form_data["username"]
        email = form_data["email"]
        password = form_data["password"]
        re_password = form_data["re_password"]
    return render_template("singup.html",**locals())
@app.route('/login',methods=["GET","POST"])
def login():
    return render_template("login.html",**locals())

if __name__ == '__main__':
    app.run(debug=True)
