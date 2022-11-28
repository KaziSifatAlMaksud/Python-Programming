from flask import Flask,render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET',"POST"])
def hello_world():
    return 'Hello World!'
@app.route('/form', methods=['GET', "POST"])
def form():
    is_post = False
    if request.method == "POST":
        is_post = True
        is_int = True
        form_data = request.form
        number = form_data["Number"]
        try:
            number = int(number)
        except ValueError:
            is_int = False
        if is_int:
            even = False
            if number%2 == 0:
                even = True
    return render_template("form", **locals())

@app.route('/name_age',methods=['GET',"POST"])
def name_age():
    if request.method == 'POST':
        from_data = request.form
        name = from_data['name']
        age = from_data['age']
        return render_template('from_output.html',**locals())
    return render_template("name_age.html",**locals())

@app.route("/same_form",methods=['GET','POST'])
def same_form():
    is_post = False
    if request.method == 'POST':
        from_data = request.form
        name = from_data['name']
        age = from_data['age']
        is_post = True
    return render_template("same_from.html",**locals())


















@app.route('/even_odd',methods=['GET',"POST"])
def even_odd():
    int_sub = False
    if request.method =='POST':
        int_sub = True
        even = False
        form_data = request.form
        try:
            n = int(form_data['number'])
            if n % 2 == 0:
                even = True
        except ValueError:
            s = "Enter a valid number"
    return render_template("even_odd.html",**locals())
if __name__ == '__main__':
    app.run(host="127.0.0.1",port=5004)
