from flask import Flask, jsonify
from dhillon import dhillon_json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return jsonify(dhillon_json)


# app.run(host='localhost', port=5000, debug=True)
