# -*- coding: utf-8 -*-

# Bear Module
# By: Enerdhil <hezardj@gmail.com>

class Bear:

    def command(self):
        self.config = {
                "command": {
                        "bear": {
                                "function": self.bear,
                                "usage": "bear",
                                "help": "Hey, I'm a bear !"
                        },
                        "bears": {
                                "function": self.bears,
                                "usage": "bears [number of bears]",
                                "help": "Hey, you can make many bears"
                        }
                }
        }
        return self.config

    def bear(self, Morphux, infos):
        Morphux.sendMessage("ʕ•ᴥ•ʔ", infos['nick'])

    def bears(self, Morphux, infos):
        manyBears = 1
        bearString = "ʕ•ᴥ•ʔ"
        if len(infos['args']) > 0 and infos['args'][0].isdigit() == False:
            Morphux.sendMessage("Don't mess with the bears !", infos['nick'])
            Morphux.sendMessage(self.config['command']['bears']['usage'], infos['nick'])
            return
        elif (len(infos['args']) > 0 and infos['args'][0].isdigit() == True):
            manyBears = int(infos['args'][0])
        if manyBears <= 0:
            Morphux.sendMessage("Oh noooo, there is no bear :(", infos['nick'])
        elif manyBears > 20:
            Morphux.sendMessage("You are mad, this is way too many bears !", infos['nick'])
        else:
            while manyBears > 1:
                bearString = "ʕ•" + bearString
                manyBears -= 1
                if manyBears > 1:
                    bearString = bearString + "•ʔ"
                    manyBears -= 1
            Morphux.sendMessage(bearString, infos['nick'])
