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
        name = form_data["username"]
        email = form_data["email"]
        mobile = form_data["mobile"]
        u_pass = form_data["password"]
        re_pass = form_data["re_password"]
        d = {"name": name,"email":email,"mobile": mobile,"password":re_pass}
        x = mycol.insert_one(d)
    return render_template("singup.html",**locals())
@app.route('/login',methods=["GET","POST"])
def login():
    return render_template("login.html",**locals())

if __name__ == '__main__':
    app.run(debug=True)
