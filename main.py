from flask import Flask, request, render_template, session,redirect,url_for
from dbFunctions import *
import json
from loginPageFunctions import *

app = Flask(__name__)
app.secret_key = "CSE305Team1"

@app.route('/')
# @app.route("/<user>")
def index():
    return render_template("login.html")

@app.route('/checkLogin',methods=['POST'])
def checkLogin():
    recvJson = request.get_json()
    email = recvJson['email']
    password = recvJson['pwd']
    session['email'] = email
    returnValue = checkPassengerCredentials(email,password)
    return str(json.dumps({"login":"true"})) if returnValue else str(json.dumps({"login":"false"}))


@app.route('/home')
def home():
    if 'email' in session:
        print(session['email'])
        return render_template("home.html")
    else:
        return redirect(url_for('index'))


@app.route('/logout')
def logout():
    print(session)
    if 'email' in session:
        print(session['email'])
        session.pop('email', None)
        print(session)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

#Lucy made a comment
#comment
