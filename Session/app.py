from flask import Flask, session, render_template, redirect, request, g, url_for
import pymongo
import os
app = Flask(__name__)
app.secret_key = "sifat"
myClined = pymongo.MongoClient("mongodb://localhost:27017/gShop")
mydb = myClined["gShop"]
mycol = mydb["user"]
shopProduct = mydb["producat"]
contactMess = mydb["contact"]


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        form_data = request.form
        username = form_data["email"]
        password = form_data["pass"]
        session['user'] = username
        for x in mycol.find({"email": username}):
            for y in mycol.find({"re_pass": password}):
                print(username)
                session['user'] = username
                return redirect(url_for('protected'))
                message = "Hello "+ username
                print(message)
                return render_template('calculator.html', **locals())
        message = "Username or password is incorrect"
        print(message)
        return render_template('calculator.html', **locals())
    return render_template('index.html',**locals())


@app.route('/protected')
def protected():
    if g.user:
        return render_template('protected.html', user=session['user'])
    return redirect(url_for('index'))


@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']


@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)