from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/', methods =['GET',"POST"])
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/form/', methods =['GET',"POST"])
def form():
    a = []
    if request.method == "POST":
      form_data = request.form
      name = form_data['name']
      try:
        file = open("templates/data.txt").readlines()
        for line in file:
          line = line.replace("\n", "")
          name2, age, dep, edu = line.split(", ")
          if name == name2:
              a.append(name2)
              a.append(age)
              a.append(dep)
              a.append(edu)
        l = len(a)
      except FileExistsError:
         print("there is a file problem")

    return render_template("form.html",**locals())

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5003)
