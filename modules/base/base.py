# Base Module
# By: Louis <louis@ne02ptzero>

class Base:

	def command(self):
		self.config = {
			"command": {
				"ping": {
					"function": self.ping,
					"usage": "ping",
					"help": "Make a ping to the bot"
				}
			},
			"onJoin": {
				"join": self.join
			}
		}
		return self.config

	def ping(self, Morphux, infos):
		Morphux.sendMessage("Pong !", infos['nick'])

	def join(self, Morphux, user):
		Morphux.sendMessage("Hey, howr u doin :) ?", user)
