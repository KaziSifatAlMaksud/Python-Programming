from flask import Flask, request, render_template

app = Flask("__name__")

@app.route("/bold/<string:n>",methods=['GET',"POST"])
def bold(n):
    n = int(n)
    return render_template('bold.html',**locals())
@app.route("/list/<string:n>",methods=['GET',"POST"])
def list(n):
    n = int(n)
    return render_template('list.html',**locals())

@app.route("/sum/<string:n>",methods=['GET',"POST"])
def sum(n):
    n = int(n)
    return render_template("sum.html",**locals())
@app.route("/table/<string:n>",methods=['GET',"POST"])
def table(n):
    n = int(n)
    return render_template("table.html",**locals())

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5003)