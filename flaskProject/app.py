from flask import Flask, session, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/form')
def form():

    return render_template("form.html",**locals())



if __name__ == '__main__':
    app.run()
