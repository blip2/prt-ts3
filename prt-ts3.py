# PRT TS3 Permission Setting API
# blip2 - 2016

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Yo.'


@app.route('/player/', methods=['UPDATE'])
def player_update():
    response = {"success": "api call not implemented", }
    return jsonify(**response)


@app.route('/player/', methods=['DELETE'])
def player_delete():
    response = {"success": "api call not implemented", }
    return jsonify(**response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7215)
