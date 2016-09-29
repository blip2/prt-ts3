# PRT TS3 Permission Setting API
# blip2 - 2016

ALLOWED_ADDR = ['127.0.0.1', '74.55.51.162',]

from flask import Flask, jsonify, request, abort

app = Flask(__name__)

@app.before_request
def limit_remote_addr():
    if request.remote_addr not in ALLOWED_ADDR:
        abort(403)  # Forbidden


@app.route('/')
def hello_world():
    return 'Yo.'


@app.route('/player/', methods=['PUT'])
def player_update():
    response = {"response": "api call not implemented", }
    return jsonify(**response)


@app.route('/player/', methods=['DELETE'])
def player_delete():
    response = {"response": "api call not implemented", }
    return jsonify(**response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7215)
