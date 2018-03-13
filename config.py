HOST = '127.0.0.1'
PORT = 10011
USER = 'serveradmin'
PASS = 'FAKEPASS'
SERVER = 1

TEAMS = {
    "emc": {
        "id": 0,
        "name": "EMC",
        "groupid": 18,
        "channelid": 13,
    },
    "apn": {
        "id": 1,
        "name": "APN",
        "groupid": 22,
        "channelid": 14,
    },
}

RANKS = {
    "reserve": {
        "groupIdbyTeam": {0: 41, 1: 42},
        "channelGroup": 1,
    },
    "grunt": {
        "groupIdbyTeam": {0: 24, 1: 25},
        "channelGroup": 1,
    },
    "nco": {
        "groupIdbyTeam": {0: 27, 1: 26},
        "channelGroup": 3,
    },
    "sl": {
        "groupIdbyTeam": {0: 29, 1: 28},
        "channelGroup": 3,
    },
    "hco": {
        "groupIdbyTeam": {0: 30, 1: 31},
        "channelGroup": 4,
    },
    "xo": {
        "groupIdbyTeam": {0: 32, 1: 33},
        "channelGroup": 2,
    },
    "co": {
        "groupIdbyTeam": {0: 35, 1: 34},
        "additionalgroups": {0: [43,], 1: [46,]},
        "channelGroup": 2,
    },
    "sco": {
        "groupIdbyTeam": {0: 37, 1: 36},
        "additionalgroups": {0: [43,44,], 1: [45,46,]},
        "channelGroup": 2,
    },
}

CHANNEL_GROUPS = {
    0: {
        "name": "User",
        "groupid": 8,
    },
    1: {
        "name": "Regular",
        "groupid": 12,
    },
    2: {
        "name": "Leader",
        "groupid": 11,
    },
    3: {
        "name": "Officer",
        "groupid": 13,
    },
    4: {
        "name": "High Command",
        "groupid": 14,
    },
}

BATTLEMODE_POWER = 20

try:
    config_module = __import__('config_local',
                               globals(), locals())

    for setting in dir(config_module):
        if setting == setting.upper():
            locals()[setting] = getattr(config_module, setting)
except Exception:
    pass
