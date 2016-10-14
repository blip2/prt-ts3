import ts3
from config import *

class TS3Server():
    server = None

    def __init__(self):
        self.server = ts3.TS3Server(HOST, PORT)
        self.server.login(USER, PASS)
        self.server.use(SERVER)

    def check_server(self):
        if not self.server:
            self.__init__()

    def getClientId(self, uid):
        self.check_server()
        response = self.server.send_command('clientgetdbidfromuid', keys={'cluid': uid,})
        if 'cldbid' not in response.data[0]:
            return None
        return response.data[0]['cldbid']


    def addToServerGroup(self, clientid, groupid):
        self.check_server()
        response = self.server.send_command('servergroupaddclient', keys={'sgid': groupid, 'cldbid': clientid,})
        return response.data[0]

    
    def removeFromServerGroup(self, clientid, groupid):
        self.check_server()
        response = self.server.send_command('servergroupdelclient', keys={'sgid': groupid, 'cldbid': clientid,})
        return response.data[0]
    

    def changeChannelGroup(self, clientid, channelid, groupid):
        self.check_server()
        response = self.server.send_command('setclientchannelgroup', keys={'cgid': groupid, 'cid': channelid, 'cldbid': clientid,})
        return response.data[0]

    def getSubscribePower(self, channelid):
        self.check_server()
        response = self.server.send_command('permidgetbyname', keys={'permsid': "i_channel_needed_subscribe_power", })
        permid = response.data[0]["permid"]
        response = self.server.send_command('channelpermlist', keys={'cid': channelid, })
        for perm in response.data:
            if perm['permid'] == permid:
                return perm['permvalue']
        return -1

    def setSubscribePower(self, channelid, value):
        self.check_server()
        response = self.server.send_command('channeladdperm', keys={'cid': channelid, 'permsid': "i_channel_needed_subscribe_power", "permvalue": value,})
        return response.data[0]


    def sendServerMessage(self, message):
        self.check_server()
        response = self.server.send_command('sendtextmessage', keys={'targetmode': 3, 'target': SERVER, "msg": message,})
        return response.data[0]

