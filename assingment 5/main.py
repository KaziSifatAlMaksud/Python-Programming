from flask import Flask, request, render_template, redirect, session
import pymongo
from bson.objectid import ObjectId 
db_client = pymongo.MongoClient("mongodb://localhost:27017")
db = db_client["Authentication"]

app = Flask(__name__)

app.secret_key = 'super secret key'


@app.route('/', methods=['GET', "POST"])
def register():
    caseA = False
    caseB = False
    caseBB = False
    caseC = False
    caseD = False
    caseDD = False

    if request.method == "POST" :
        form_data = dict(request.form)
        username = form_data["username"]
        password = form_data["pass"]
        password2 = form_data["pass2"]
        email = form_data["email"]
        phone = form_data["phone"]
        userName = db.users.find_one({"username": username})
        userEmail = db.users.find_one({"email": email})
        userPhone = db.users.find_one({"phone": phone})
        newUser = {"username": username, "password": password, "email": email, "phone": phone}
        if userName is not None:
            caseA = True
            return " User Already Exist "
        if password != password2:
            return " Password Did Not Matched "
        if len(password) < 6:
            return " Password must be atleast 6 "
        if userEmail is not None:
            return " Email Already Exist "
        if userPhone is not None:
            return " Phone Already Exist "
        if len(phone) != 11:
            return " Invalid Phone "

        if caseA == False and caseB == False  and caseC == False and caseD == False and caseBB == False:
            db.users.insert_one(newUser)
            return "Registration Successsfull"


    return render_template("register.html", **locals())




if __name__ == "__main__":
    app.run(host='127.0.0.1', port=50010)
    #serve(app, host='127.0.0.1', port=5002)
    #serve(app, host='0.0.0.0', port=80)


