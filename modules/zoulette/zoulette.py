class Zoulette:
    def command(self):
        self.config = {
            "command": {
                "zoulette": {
                    "function": self.zouletteMain,
                    "usage": "zoulette [user]",
                    "help": "zoulette someone"
                }
            }
        }
        self.zouletteLaunched = 0
        self.zouletteCount = 0
        self.zouletteName = ""
        self.votes = []
        self.uniq_id = []
        return self.config
    def zouletteMain(self, Morphux, infos):
        self.uniq_id = infos["fullUser"].split("!")
        if (len(self.uniq_id) > 1):
            if (self.zouletteLaunched == 0):
                if (len(infos['args']) == 0):
                    Morphux.sendMessage("You have to target someone !", infos['nick'])
                elif ((infos['args'][0] == infos['nick'])):
                    Morphux.kick(infos['nick'], "You're right.")
                elif (Morphux.userExists(infos["args"][0]) == False):
                    self.zouletteLaunched = 1
                    self.zouletteCount = 1
                    self.votes.append(self.uniq_id[1])
                    self.zouletteName = infos['args'][0]
                    Morphux.sendMessage("You just launched a zoulette against " + infos['args'][0], infos['nick'])
                else:
                    Morphux.sendMessage("User '" + infos['args'][0] + "' does not exists" , infos['nick'])
            else:
                if (self.uniq_id[1] not in self.votes):
                    Morphux.sendMessage("You just voted against " + self.zouletteName, infos['nick'])
                    self.zouletteCount += 1
                    self.votes.append(self.uniq_id[1])
                else:
                    Morphux.sendMessage("You can't vote twice little filou !", infos['nick'])
                if (self.zouletteCount > len(Morphux.currentUsers) / 2):
                    Morphux.kick(self.zouletteName, "We call it democracy.")
                    self.zouletteLaunched = 0
                    self.zouletteCount = 0
                    self.zouletteName = ""
                    self.votes = []
