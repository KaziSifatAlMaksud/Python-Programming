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
    if request.method == "POST":
        form_data = request.form
        name = form_data["username"]
        email = form_data["email"]
        mobile = form_data["mobile"]
        u_pass = form_data["password"]
        re_pass = form_data["re_password"]
        if u_pass == re_pass:
            d = {"name": name , "email":email ,"mobile":mobile ,"password":re_pass}
            x = mycol.insert_one(d)
        else:
            passmess = "Password is not match"
    return render_template("singup.html",**locals())
@app.route('/login',methods=["GET","POST"])
def login():
    if request.method == "POST":
        form_data = request.form
        email = form_data["email"]
        passw = form_data["enter_pass"]
        user_name = mycol.find_one({"email":email})
        if user_name is None:
            email_mess = "Email was not register, Please Sign Up"
        user_passw = mycol.find_one({"password": passw})
        if user_passw is None:
            pass_mess = "Password not Correct, Try Again "
    return render_template("login.html",**locals())

if __name__ == '__main__':
    app.run(debug=True)
