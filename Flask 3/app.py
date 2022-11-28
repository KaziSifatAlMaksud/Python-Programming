from flask import Flask,request,render_template
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

@app.route('/pas_name')
def pass_name():
    name = "Jone"
    return render_template("pas_name.html",**locals())

@app.route('/pass_danamic/<string:name>', methods =['GET','POST'])
def pass_danamic(name):
    return render_template("pass_danamic.html", **locals())

@app.route('/incriment/<string:n>')
def incriment(n):

    return "the name is %s"%n

@app.route('/print_odd/<string:h>',methods=['GET','POST'])
def print_odd(h):
     h = int(h)
     return render_template("print_odd.html",**locals())

@app.route('/table',methods=['GET','POST'])
def table():
   d = {"a":1,"b":3,"c":8}
   return render_template("Table.html",**locals())

@app.route('/file',methods=['GET','POST'])
def file():
    a = []
    f = open("Templates/main.txt").readlines()
    for line in f:
        a.append(line)
    x = len(a)
    return render_template("file.html", **locals())

@app.route('/dicsonay',methods=['GET','POST'])
def dicsonay():
    w={}
    f = open('Templates/main.txt').readlines()
    for line in f:
        line = line.replace("\n","")
        key, val = line.split(" ")
        w[key] = val
    return render_template("dicsonay.html", **locals())

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5001)