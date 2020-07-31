'''
import os
from flask import Flask, render_template, request
import pickle
import loop

pkl_file = open('patient.pkl', 'rb')
mydict = pickle.load(pkl_file)
pkl_file.close()

from flask_sqlalchemy import SQLAlchemy
import pymysql


pymysql.install_as_MySQLdb()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/sihproject'
db=SQLAlchemy(app)




class user(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(30))
    email = db.Column(db.String(120))
    password = db.Column(db.String(80))

users = user.query.all()
for user in users:
    print(f"<id={user.id}, username={user.username}, gender={user.gender}, email={user.email}>")





app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        mail = request.form["mail"]

        #login = user.query.filter_by(email=mail, password=passw).first()

        if mail not in mydict:
            return render_template("upload.html")
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        uname = request.form['uname']
        age = request.form['age']
        gender = request.form['gender']
        mail = request.form['mail']
        passw = request.form['passw']

        
        
       # db.session.add(register)
       # db.session.commit()
    
        mydict[mail]={}
        mydict[mail]["age"]=age
        mydict[mail]["gender"]=gender
        mydict[mail]["digit"]=[]
        print(uname)
        print(mydict)
        return render_template("login.html")
    return render_template("register.html")


@app.route("/upload", methods=['POST'])
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

    loop.looping()
    
    return render_template("complete.html")


if __name__ == "__main__":
    #db.create_all()
    app.run(debug=True)
    app.run(port=4555, debug=True)
'''

import os
from flask import Flask, render_template, request,Response,redirect,url_for
import pickle
import loop
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
        mydict[mail]["age"]=int(age)
        mydict[mail]["gender"]=gender
        
        output = open('patient.pkl', 'wb')
        pickle.dump(mydict, output)
        output.close()
        print(mydict)
        return redirect(url_for("login"))
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
    loop.looping(xyz)
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