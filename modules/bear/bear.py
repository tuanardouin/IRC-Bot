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
					"usage": "bears",
					"help": "Hey, you can make many bears"
				}
			}
		}
		return self.config

	def bear(self, Morphux, infos):
		Morphux.sendMessage("ʕ•ᴥ•ʔ", infos['nick'])

	def bears(self, Morphux, infos):
		Morphux.sendMessage("ʕ•ᴥʕ•ᴥʕ•ᴥ•ʔᴥ•ʔᴥ•ʔ", infos['nick'])
