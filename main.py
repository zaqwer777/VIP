from flask import Flask, render_template, redirect, url_for, request
import pyrebase
from cogsci import CogSciModule
import json

config = {
    "apiKey": "AIzaSyC6ce12c32OpCI7-u5ueRbfYhsw_fBnkwk",
    "authDomain": "vip-ipcrowd.firebaseapp.com",
    "databaseURL": "https://vip-ipcrowd.firebaseio.com",
    "storageBucket": "vip-ipcrowd.appspot.com"
}
firebase = pyrebase.initialize_app(config)

app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('login.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/<user>', methods=['GET', 'POST'])
def homepage(user=None):
    #test = firebase.database().child("users").child("admin").get().val()
    csm = CogSciModule()
    input_annotations = []
    populated_annos = []
    users = firebase.database().child("users").get()
    for u in users.val():
        print(u)
        if str(u) == user:
            for anno in users.val()[u]:
                input_annotations.append(users.val()[u][anno]['text'])
        else:
            for anno in users.val()[u]:
                print(anno)
                populated_annos.append(users.val()[u][anno])
    bias = csm.updateCurrentAnnotations(input_annotations)
    points = len(input_annotations)
    return render_template("homepage.html", user=user, bias=bias, points=points, populated_annos=populated_annos)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
