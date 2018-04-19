from flask import Flask, render_template, redirect, url_for
import pyrebase

config = {
    "apiKey": "AIzaSyC6ce12c32OpCI7-u5ueRbfYhsw_fBnkwk",
    "authDomain": "vip-ipcrowd.firebaseapp.com",
    "databaseURL": "https://vip-ipcrowd.firebaseio.com",
    "storageBucket": "vip-ipcrowd.appspot.com"
}
firebase = pyrebase.initialize_app(config)

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/<user>')
def homepage(user=None):
    #test = firebase.database().child("users").child("admin").get().val()
    test = '5'
    return render_template("homepage.html", user=user, test=test)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
