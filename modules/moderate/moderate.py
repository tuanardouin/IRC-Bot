# Moderation Module
# By: Louis <louis@ne02ptzero.me>

class Moderate:
	def command(self):
		self.config = {
			"command": {
				"kick": {
					"function": self.kick,
					"usage": "kick user",
					"help": "GET REKT"
				}
			}
		}
		return self.config

	def kick(self, Morphux, infos):
		if (Morphux.isAdmin(infos['nick'])):
			if (len(infos['args'])):
				Morphux.kick(infos['args'][0], "GET REKT")
		else:
			Morphux.sendMessage("You're not admin !", infos['nick'])
