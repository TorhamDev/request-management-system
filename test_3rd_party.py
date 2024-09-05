
# run pip install flask before run it
# run it by just runing this file e.g: python test_3rd_party.py

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    print("[X] Request received!")
    return "<p>Hello, World!</p>"


app.run(port=8080, debug=True)