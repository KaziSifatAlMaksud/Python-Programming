from flask import Flask, request, redirect, render_template, session
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
users_table = mydb["users"]

app = Flask(__name__)

app.secret_key = 'super secret key'


@app.route('/login', methods=['GET', "POST"])
def login():
    if request.method == "POST":
        form_data = dict(request.form)
        form_username = form_data["username"]
        form_password = form_data["password"]
        db_user = users_table.find_one({"username": form_username})
        if db_user is None:
            return "Username not found"
        if form_password != db_user["password"]:
            return "password did not match"
        session["logged_in"] = True
        session["username"] = form_username
    if "logged_in" in session:
        return 'logged in <br> <a href="/logout">logout</a>'
    return render_template("login.html", **locals())


@app.route('/logout', methods=['GET', "POST"])
def logout():
    session.clear()
    return redirect("/login")


@app.route('/', methods=['GET', "POST"])
def home():
    if "logged_in" in session:
        return "hello " + session["username"]
    return "hello"


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5002)
    # serve(app, host='127.0.0.1', port=5002)
    # serve(app, host='0.0.0.0', port=80)

