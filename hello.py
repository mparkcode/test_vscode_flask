from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/testing")
def testing():
    return "Testing"

if __name__ == "__main__":
    app.run()   