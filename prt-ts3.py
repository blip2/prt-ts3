# PRT TS3 Permission Setting API
# blip2 - 2016

from flask import Flask, jsonify, request, abort
from api import TS3Server
from flask_cors import CORS
from config import *

app = Flask(__name__)
cors = CORS(app)
server = TS3Server()

ALLOWED_ADDR = ['127.0.0.1', '74.55.51.162', '164.132.41.81', ]


@app.before_request
def limit_remote_addr():
    if request.remote_addr not in ALLOWED_ADDR:
        abort(403)  # Forbidden


@app.route('/')
def hello_world():
    return 'Yo.'


def error(json, status):
    response = jsonify(json)
    response.status_code = status
    return response


@app.route('/player/', methods=['OPTIONS'])
def player_get():
    response = {"response": "success", }
    return jsonify(**response)


@app.route('/player/', methods=['PUT'])
def player_update():
    data = request.get_json()
    if not data:
        return error({"response": "no data received", }, 400)
    if "uid" not in data or "team" not in data or "rank" not in data:
        return error({"response": "missing parameters from request", }, 400)
    if data["team"] not in TEAMS:
        return error({"response": "invalid team reference", }, 400)
    team = TEAMS[data["team"]]
    if data["rank"] not in RANKS:
        return error({"response": "invalid rank reference", }, 400)
    rank = RANKS[data["rank"]]

    clientid = server.getClientId(data["uid"])
    if not clientid:
        return error({"response": "UID not found on Teamspeak server", }, 404)

    server.addToServerGroup(clientid, team["groupid"])
    server.addToServerGroup(clientid, rank["groupIdbyTeam"][team["id"]])
    if "additionalgroups" in rank:
        for groupid in rank["additionalgroups"][team["id"]]:
            server.addToServerGroup(clientid, groupid)
    server.changeChannelGroup(clientid, team["channelid"],
                              CHANNEL_GROUPS[rank["channelGroup"]]["groupid"])

    response = {"response": "success", }
    return jsonify(**response)


@app.route('/player/', methods=['DELETE'])
def player_delete():
    data = request.get_json()
    if not data:
        return error({"response": "no data received", }, 400)
    if "uid" not in data:
        return error({"response": "missing parameters from request", }, 400)

    clientid = server.getClientId(data["uid"])
    if not clientid:
        return error({"response": "UID not found on Teamspeak server", }, 404)

    for team in TEAMS:
        team = TEAMS[team]
        for rank in RANKS:
            rank = RANKS[rank]
            server.removeFromServerGroup(clientid, team["groupid"])
            server.removeFromServerGroup(clientid,
                                         rank["groupIdbyTeam"][team["id"]])
            if "additionalgroups" in rank:
                for groupid in rank["additionalgroups"][team["id"]]:
                    server.removeFromServerGroup(clientid, groupid)
            server.changeChannelGroup(clientid, team["channelid"],
                                      CHANNEL_GROUPS[0]["groupid"])

    response = {"response": "success", }
    return jsonify(**response)


@app.route('/battlemode/', methods=['GET'])
def get_battlemode():
    data = request.get_json()
    if "team" not in data:
        return error({"response": "missing parameters from request", }, 400)
    if data["team"] not in TEAMS:
        return error({"response": "invalid team reference", }, 400)
    team = TEAMS[data["team"]]

    subPower = server.getSubscribePower(team["channelid"])
    if int(subPower) == BATTLEMODE_POWER:
        response = {"response": "success", "state": "on", }
    elif int(subPower) == 0:
        response = {"response": "success", "state": "off", }
    else:
        response = {"response": "success", "state": "unknown", }
    return jsonify(**response)


@app.route('/battlemode/', methods=['PUT'])
def set_battlemode():
    data = request.get_json()
    if "team" not in data or "state" not in data:
        return error({"response": "missing parameters from request", }, 400)
    if data["team"] not in TEAMS:
        return error({"response": "invalid team reference", }, 400)
    team = TEAMS[data["team"]]
    if data["state"] not in ["on", "off"]:
        return error({"response": "invalid state", }, 400)

    if data["state"] == "on":
        server.setSubscribePower(team["channelid"], BATTLEMODE_POWER)
        server.sendServerMessage(team["name"] +
                                 " channels are now in BATTLEMODE")

    if data["state"] == "off":
        server.setSubscribePower(team["channelid"], 0)
        server.sendServerMessage(team["name"] +
                                 " channels are no longer in BATTLEMODE")

    response = {"response": "success", }
    return jsonify(**response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7215)
