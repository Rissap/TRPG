from world import World


class Message():
    """docstring for Message"""
    def __init__(self):
        self.playerID = 0
        self.playerText = ""
        self.new = False

        self.sendText = ""
        self.sendKeyboard = ""
        self.sendAttachments = ""

    def getMessage(self):
        self.playerID = 219124437
        self.playerText = input("<$: ")
        self.new = True

    def sendMessage(self):
        print(">>", self.sendText, "\n")
        
        self.new = False
        self.sendText = ""
        self.sendKeyboard = ""
        self.sendAttachments = ""

    def setText(self, data):
        self.sendText = str(data)

    def setKeyboard(self, data):
        self.sendKeyboard = data

    def setAttachments(self, data):
        self.sendAttachments = data
        

class Control():
    """docstring for Control"""
    def __init__(self, _Message, _Database, _World):
        self.Message = _Message
        self.Database = _Database
        self.World = _World

    def start(self):
        work = True
        while work:
            self.Message.getMessage()
        
            if self.Message.new:
                #set special AdminClass that can operate special foo and stop game process

                self.World.raisePlayerData(self.Message.playerID, self.Message.playerText)
                self.World.handlePlayerAction()
                self.World.updatePlayerAction()

                self.Message.setText(self.World.ConcretePlayer.getAnswer())
                self.Message.setKeyboard(self.World.ConcretePlayer.getKeyboard())
                
                #self.Message.setAttachments(self.Database.getAttachments())

                self.Message.sendMessage()
            else:
                pass

