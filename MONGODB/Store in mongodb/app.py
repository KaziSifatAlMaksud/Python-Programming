from flask import Flask, render_template,request
import pymongo
import bcrypt
app = Flask(__name__)
myClined = pymongo.MongoClient("mongodb://localhost:27017/gShop")
mydb = myClined["gShop"]
mycol = mydb["user"]
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'
@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "POST":
        form_data = request.form
        username = form_data["email"]
        password = form_data["password"]
        for x in mycol.find({"email": username},{"re_pass": password}):

            return "hellow sifat"

    return render_template("login.html", **locals())

@app.route('/regestation', methods=["GET","POST"])
def regestation():
    user_d = {}
    if request.method == "POST":
        form_data = request.form
        user_name = form_data["name"]
        user_email = form_data["email"]
        user_mobile = form_data["mobile"]
        user_pass = form_data["password1"]
        user_re_pass =form_data["password2"]
        user_d["name"] = user_name
        user_d["email"] = user_email
        user_d["mobile"]= user_mobile
        user_d["pass"] = user_pass
        user_d["re_pass"] =user_re_pass
        #mycol.insert_one(user_d)
        return render_template("login.html",**locals())
    return render_template("regestation.html",**locals())

if __name__ == '__main__':
    app.run(port="127.0.0.1",host=5003)
