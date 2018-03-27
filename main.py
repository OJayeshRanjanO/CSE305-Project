from flask import Flask, request, render_template
from dbFunctions import *

app = Flask(__name__)

@app.route('/')
# @app.route("/<user>")
def index():
    return render_template("login.html")
    # return "Method used: %s" % request.method


if __name__ == '__main__':
    app.run(debug=True)