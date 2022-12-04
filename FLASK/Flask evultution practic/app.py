from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods = ['GET',"POST"])
def index():
    return 'Hello World!'

@app.route('/form/', methods = ['GET',"POST"])
def form():
    if request.method == "POST":
        try:
            from_data = request.form
            number = int(from_data["number"])
        except ValueError:
            print("type Error")
    return render_template("form.html", **locals())
@app.route('/file/',methods = ['GET',"POST"])
def file():

    a = []
    b =[]
    file  = open("templates/data.txt").readlines()
    sum = 0
    for line in file:
        name, mark = line.split(" ")
        mark = int(mark)
        a.append(name)
        b.append(mark)
        l = len(a)
        sum = sum + mark
    return render_template("table.html",**locals())

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=50003)
