# Moderation Module
# By: Louis <louis@ne02ptzero.me>

from            subprocess      import call
import          random

class Moderate:
    def command(self):
        self.config = {
                "command": {
                        "kick": {
                                "function": self.kick,
                                "usage": "kick user",
                                "help": "GET REKT"
                        },
                        "restart": {
                                "function": self.restart,
                                "usage": "restart",
                                "help": "Restart the bot"
                        },
                        "insult": {
                                "function": self.insult,
                                "usage": "nick",
                                "help": "Insult someome"
                        },
                        "pizza": {
                                "function": self.pizza,
                                "usage": "nick",
                                "help": "Give pizza to someone"
                        },
                        "beer": {
                                "function": self.beer,
                                "usage": "nick",
                                "help": "Give beer to someone"
                        },
                        "louis": {
                                "function": self.louis,
                                "usage": "",
                                "help": "..."
                        },
                        "code": {
                                "function": self.code,
                                "usage": "nick",
                                "help": "Politely ask someone for code"
                        },
                        "lol": {
                                "function": self.lol,
                                "usage": "",
                                "help": "XD"
                        },
                        "marvin": {
                                "function": self.marvin,
                                "usage": "",
                                "help": "PHP <3"
                        },
                        "coro": {
                                "function": self.coro,
                                "usage": "",
                                "help": "Coro <3"
                        },
                        "noich" : {
                                "function": self.noich,
                                "usage": "",
                                "help": ":3"
                        }


                }
        }
        return self.config

    def kick(self, Morphux, infos):
        if (Morphux.isAdmin(infos['nick'])):
            if (len(infos['args'])):
                if (infos['args'][0] == "CL4P_TP"):
                    Morphux.kick(infos['nick'], ".")
                else:
                    Morphux.kick(infos['args'][0], "GET REKT")
        else:
            Morphux.sendMessage("You're not admin !", infos['nick'])

    def restart(self, Morphux, infos):
        if (Morphux.isAdmin(infos['nick'])):
            Morphux.sendMessage("THIS IS NOT THE END");
            call(["/usr/bin/supervisorctl", "restart", "mrdoe"]);
        else:
            Morphux.sendMessage("...", infos['nick'])

    def insult(self, Morphux, infos):
        if (len(infos["args"]) == 0):
            Morphux.sendMessage("Need someone to insult, u moron", infos["nick"])
        elif (Morphux.userExists(infos["args"][0])):
            Morphux.sendMessage("Can't insult " + infos["args"][0] + ", is not here.", infos["nick"])
        else:
            r = random.randint(1, 5)
            if (r == 1): Morphux.sendMessage("You piece of shit", infos["args"][0])
            if (r == 2): Morphux.sendMessage("You suck", infos["args"][0])
            if (r == 3): Morphux.sendMessage("You godamn moron", infos["args"][0])
            if (r == 4): Morphux.sendMessage("You asshole", infos["args"][0])
            if (r == 5): Morphux.sendMessage("You are a bad bitch, a very bad bitch", infos["args"][0])

    def pizza(self, Morphux, infos):
        if (len(infos["args"]) == 0):
            Morphux.sendMessage("I ate the pizza :/", infos["nick"])
        elif (Morphux.userExists(infos["args"][0])):
            Morphux.sendMessage(infos["args"][0] + " is not here, but don't worry, i keep the pizza warm :)", infos["nick"])
        else:
            Morphux.sendMessage(infos["nick"] + " give you some pizza !", infos["args"][0])
    def beer(self, Morphux, infos):
        if (len(infos["args"]) == 0):
            Morphux.sendMessage("I drink the beer :/", infos["nick"])
        elif (Morphux.userExists(infos["args"][0])):
            Morphux.sendMessage(infos["args"][0] + " is not here", infos["nick"])
        else:
            Morphux.sendMessage(infos["nick"] + " give you some beer ! Bottom'up !", infos["args"][0])

    def louis(self, Morphux, infos):
        Morphux.sendMessage("*sigh*");

    def code(self, Morphux, infos):
        if (len(infos["args"]) == 0):
            Morphux.sendMessage("Code by yourself", infos["nick"])
        elif (Morphux.userExists(infos["args"][0])):
            Morphux.sendMessage(infos["args"][0] + " should be coding, but since he's not here, we'll never know !", infos["nick"])
        else:
            Morphux.sendMessage(infos["args"][0] + " is a little bitch and sould start coding instead of complaining")

    def lol(self, Morphux, infos):
        Morphux.sendMessage("TAMER");

    def marvin(self, Morphux, infos):
        Morphux.sendMessage("Aaaaaaaah");

    def coro(self, Morphux, infos):
        Morphux.sendMessage("Nikouli Makouli ?");

    def noich(self, Morphux, infos):
        Morphux.sendMessage("goo.gl/IiBBg1", infos['nick']);
