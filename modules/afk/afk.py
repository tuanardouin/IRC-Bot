# Afk Module
# By: Louis <louis@ne02ptzero.me>

from pprint import pprint
import re

class Afk:
    def command(self):
        self.config = {
                "command": {
                        "afk": {
                                "function": self.setAfk,
                                "usage": "afk reason",
                                "help": "Set yourself as afk"
                        }
                },
                "before": {
                        "afkLook": self.afkLook,
                        "ls": self.lsLook,
                        "exit": self.exitLook,
                        "regex": self.regexLook,
                }
        }
        self.afkList = {}
        self.say = {}
        return self.config

    def setAfk(self, Morphux, infos):
        self.afkList[infos['nick']] = " ".join(infos['args'])

    def afkLook(self, Morphux, line):
        infos = Morphux.getInfo(line, 1)
        if (infos == False):
            return 1;
        print(infos['nick'])
        print(self.afkList)
        user = re.sub("[!:,?#]", '', infos['command'])
        if (infos['nick'] in self.afkList):
            del self.afkList[infos['nick']]
        elif (user in self.afkList):
            Morphux.sendMessage(user + " is afk ("+ self.afkList[user][:20] +")", infos['nick'])
        return 1

    def lsLook(self, Morphux, line):
        infos = Morphux.getInfo(line, 1)
        if (type(infos) != type(True) and type(infos) != type(False) and infos['command'] == 'ls'):
            Morphux.sendMessage("ls: cannot access 'brain': No such file or directory", infos['nick']);

    def exitLook(self, Morphux, line):
        infos = Morphux.getInfo(line, 1)
        if (type(infos) != type(True) and type(infos) != type(False) and infos['command'] == 'exit'):
            Morphux.sendMessage("k.", infos['nick']);
            Morphux.kick(infos['nick'], "k.")

    def regexLook(self, Morphux, line):
        infos = Morphux.getInfo(line, 1)
        if (type(infos) != type(True) and len(infos['command']) > 2 and infos['command'][0] == '.' and infos['command'][1] == '/'):
            line = infos['fullLine'].split(":")
            regex = line[len(line) - 1][1:]
            regex = regex.split("/")
            regex.pop(0)
            if (len(regex) == 2 and infos['nick'] in self.say):
                result = self.say[infos['nick']].replace(regex[0], regex[1])
                if (len(result) < 100 and result != self.say[infos['nick']]):
                    Morphux.sendMessage(result, infos['nick'])
        elif (type(infos) != type(True)):
            line = line.split(":")
            line = line[len(line) - 1]
            self.say[infos['nick']] = line
