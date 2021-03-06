# Base Module
# By: Louis <louis@ne02ptzero>

import random

class Base:

    def ping(self, Morphux, infos):
        Morphux.sendMessage("Pong !", infos['nick'])

    def join(self, Morphux, user):
        Morphux.sendMessage("Hey, howr u doin :) ?", user)

    def nyan(self, Morphux, infos):
        Morphux.sendMessage(str("telnet nyancat.dakko.us"), infos['nick'])

    def ah(self, Morphux, infos):
        Morphux.sendMessage("https://youtu.be/XE6YaLtctcI", infos['nick'])

    def wow(self, Morphux, infos):
        Morphux.sendMessage("https://www.youtube.com/embed/jUy9_0M3bVk?autoplay=1", infos['nick'])

    def command(self):
        self.config = {
            "command": {
                "ping": {
                    "function": self.ping,
                    "usage": "ping",
                    "help": "Make a ping to the bot"
                },
                "nyan": {
                    "function": self.nyan,
                    "usage": "nyan",
                    "help": "nyannyannyannyannyan"
                },
                "ah": {
                    "function": self.ah,
                    "usage": "ah",
                    "help": "AH !"
                },
                "wow": {
                    "function": self.wow,
                    "usage": "wow",
                    "help": "Wooow !"
                }
            },
            "onJoin": {
                "join": self.join
            }
        }
        return self.config
