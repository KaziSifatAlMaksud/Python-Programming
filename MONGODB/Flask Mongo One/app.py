from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)



app.config["MONGO_URL"] = "mongodb://localhost:27017/mydatabase"
mongo = PyMongo(app)
@app.route("/user/<username>")
def user_profile(username):
    user = mongo.db.users.find_one_or_404({"_id": username})
    return render_template("user.html", **locals())
if __name__ == '__main__':
    app.run()
