from flask import Flask,request, render_template

app = Flask(__name__)
@app.route('/',methods= ['GET',"POST"])
def index():  # put application's code here
    return 'Hello World!'

@app.route('/singUp/',methods= ['GET',"POST"])
def singUp():
    a = []
    b = []
    c = []
    if request.method == "POST":
        form_data = request.form
        name = form_data['name']
        email = form_data['email']
        password = form_data['password']
        try:
            file = open("templates/data.txt", "a")
            file.write( name + " " + email + " " + password + "\n")
            file.close()
        except FileExistsError:
            print("there is a file problem")

    return render_template('sing_up.html',**locals())
@app.route("/logIn/",methods=['GET',"POST"])
def logIn():
    if request.method == "POST":
        try:
            form_data = request.form
            user_email = form_data['email']
            user_pass = form_data['password']
            user_pass = str(user_pass)
            file1 = open("templates/data.txt").readlines()
            for line1 in file1:
                line1.replace("\n", "")
                name,email,password = line1.split("#")
                print(email)
                print(password)
                print(user_email)
                print(user_pass)
                if user_pass == password:
                    print("Thank you password is correct"+name)


                else:
                    print("sorry password is in correct")
            file1.close()
        except TypeError:
            print("I am sorry")
    return render_template('logIn.html',**locals())



if __name__ == '__main__':
    app.run(host="127.0.0.1",port= 50005)
