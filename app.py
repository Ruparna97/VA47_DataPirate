
import os
from flask import Flask, render_template, request,Response,redirect,url_for
import pickle
import loop1
import graph
import time
import shutil

global xyz
xyz=0
pkl_file = open('patient.pkl', 'rb')
mydict = pickle.load(pkl_file)
pkl_file.close()

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("index.html")

response=Response()
@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        mail = request.form["mail"]

        #login = user.query.filter_by(email=mail, password=passw).first()
        global xyz
        xyz=int(mail)
        print(mydict)
        if mail not in mydict:
            return render_template("upload.html")
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        #uname = request.form['uname']
        age = request.form['age']
        gender = request.form['gender']
        mail = request.form['mail']
        #passw = request.form['passw']

        
        '''
        db.session.add(register)
        db.session.commit()
        '''
        mail=int(mail)
        global xyz
        xyz=mail
        print("xyzz",xyz)
        mydict[mail]={}
        mydict[mail]["digit"]=[]
        mydict[mail]["digit_creatinine"]=[]
        mydict[mail]["digit_glucose"]=[]
        mydict[mail]["age"]=int(age)
        mydict[mail]["gender"]=gender
        
        output = open('patient.pkl', 'wb')
        pickle.dump(mydict, output)
        output.close()
        print(mydict)
        return redirect(url_for("index"))
    return render_template("register.html")


@app.route("/upload", methods=['GET','POST'])
def upload():
    #creates a folder where ur images will be saved
    target = os.path.join(APP_ROOT, 'images/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)
    global xyz
    print(mydict)
    loop1.looping(xyz)
    graph.graphing(xyz)
    shutil.rmtree('images')
    return render_template("complete.html",graph="chart.png")
@app.route("/test", methods=['GET','POST'])
def test():
    return render_template("test.html")

if __name__ == "__main__":
    #db.create_all()
    app.run(debug=True)
    app.run(port=4555, debug=True)