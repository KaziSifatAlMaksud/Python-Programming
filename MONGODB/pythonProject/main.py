from flask import Flask, request, render_template
import pymongo
import bcrypt
app = Flask(__name__)
myclient = pymongo.MongoClient("mongodb://localhost:27017/students_info")
mydb = myclient["students"]

mycol =mydb["std"]


@app.route('/', methods = ['GET',"POST"])
def index():

    return 'Hello World!'

@app.route('/form/', methods = ['GET',"POST"])
def form():
    ids = []
    m = []
    mydict= {}
    if request.method == "POST":
        try:
            from_data = request.form
            id = from_data["id"]
            marks = from_data["marks"]
            mydict["user_id"] = id
            mydict["User_marks"] = marks
            x = mycol.insert_one(mydict)

            for x in mycol.find():
                id = x["user_id"]
                mark = x["User_marks"]
                ids.append(id)
                m.append(mark)
            l = len(ids)
        except ValueError:
            print("type Error")
    return render_template("form.html", **locals())


@app.route('/deletForm/', methods=['GET', "POST"])
def deletForm():
    ids = []
    m = []
    mydict = {}
    if request.method == "POST":
        from_data = request.form
        id = from_data["id"]
        mycol.delete_one({"user_id": id})
    return render_template("delet_form.html", **locals())

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=50003)