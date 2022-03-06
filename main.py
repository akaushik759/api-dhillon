from flask import Flask, request, jsonify
from dhillon import dhillon_json
from dhillon_lyrics import dhillon_lyrics_json

app = Flask(__name__)


@ app.route('/', methods=['GET'])
def index():
    return jsonify(dhillon_json)


@ app.route('/lyrics', methods=['GET'])
def with_lyrics():
    return jsonify(dhillon_lyrics_json)


# app.run(host='localhost', port=5000, debug=True)
