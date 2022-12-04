from flask import Flask,request,render_template

app = Flask(__name__)


# @app.route('/login', methods=['GET','POST'])
# def login():
#     uname = request.form['uname']
#     passwrd = request.form['pass']
#     if uname == "sifat" and passwrd == "123":
#         return "Welcome %s" % uname
@app.route('/Home1/<string:n>', methods=['GET', "POST"])
def home1(s):
    n = int(s)
    return render_template("home1.html", **locals())

if __name__ == '__main__':
    app.run(debug=True)