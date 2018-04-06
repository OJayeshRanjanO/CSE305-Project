from flask import Flask, request, render_template
from dbFunctions import *
import json
from loginPageFunctions import *

app = Flask(__name__)

@app.route('/')
# @app.route("/<user>")
def index():
    return render_template("login.html")

@app.route('/checkLogin',methods=['POST'])
def checkLogin():
    recvJson = request.get_json()
    email = recvJson['email']
    password = recvJson['pwd']
    returnValue = checkPassengerCredentials(email,password)
    return str(json.dumps({"login":"true"})) if returnValue else str(json.dumps({"login":"false"}))


@app.route('/home')
def home():
    return render_template("profile.html")


if __name__ == '__main__':
    app.run(debug=True)

#Lucy made a comment
#comment
