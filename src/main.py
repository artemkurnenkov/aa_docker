from crypt import methods
import json
from logging import exception
from flask import Flask, request

app = Flask(__name__)


@app.route('/hello', methods=["GET"])
def get_hello():
    return 'Hello, Glowbyte!'


@app.route('/sum', methods=["GET"])
def calc():
    try:
        a = request.args.get('a')
        b = request.args.get('b')
        return "{0}+{1}={2}".format(a, b, int(a) + int(b))
    except TypeError as te:
        return "Error value"


@app.route("/send_data", methods=["POST"])
def data():
    try:
        mydata = request.get_json()
        return mydata
    except Exception as e:
        return json.dumps({"error": str(e)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
