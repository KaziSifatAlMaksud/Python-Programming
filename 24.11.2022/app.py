from flask import Flask, render_template

app = Flask(__name__)


@app.route('/table/<string:n>', methods=['GET',"POST"])
def table(n):
    n = int(n)
    return render_template("table.html", **locals())


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5004)
