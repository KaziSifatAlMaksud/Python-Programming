from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/', methods =['GET',"POST"])
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/form/', methods =['GET',"POST"])
def form():
    a = []
    post_in = False
    if request.method == "POST":
      post_in = True
      form_data = request.form
      user_id = form_data['id']
      try:
        file = open("templates/data.txt").readlines()
        find_da = False
        for line in file:
          line = line.replace("\n", "")
          id, marks = line.split(" ")
          if user_id == id:
              find_da = True
              m_marks = marks
      except FileExistsError:
         print("there is a file problem")

    return render_template("form.html",**locals())

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5002)
