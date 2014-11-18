# Afk Module
# By: Louis <louis@ne02ptzero.me>

from pprint import pprint

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
				"afkLook": self.afkLook
			}
		}
		self.afkList = {}
		return self.config

	def setAfk(self, Morphux, infos):
		self.afkList[infos['nick']] = " ".join(infos['args'])

	def afkLook(self, Morphux, line):
		infos = Morphux.getInfo(line, 1)
		user = infos['command'].translate(None, "!:,?#")
		if (user in self.afkList):
			Morphux.sendMessage(user + " is afk ("+ self.afkList[user] +")", infos['nick'])
		return 1
