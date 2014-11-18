
class Hi:
	def command(self):
		config = {
			"command": {
				"hi": self.hiCommand,
				"cake": self.someCake
			},
			"onJoin": {
				'sayHello' :self.sayHello
			},
			"onLeave": self.sayGoodbye,

		}
		return config

	def hiCommand(self, Morphux, infos):
		Morphux.sendMessage("Hello !", infos['nick'])

	def someCake(self, Morphux, infos):
		if (len(infos['args'][0]) == 0):
			Morphux.sendMessage("Kay fine, i eat my cake alone.", infos['nick']);
		if (Morphux.userExists(infos['args'][0])):
			Morphux.sendMessage(infos['nick'] + " give u some cake :) !" ,infos['args'][0])
		else:
			Morphux.sendMessage("Can't find user " + infos['args'][0], infos['nick']);

	def sayHello(self, Morphux, user):
		Morphux.sendMessage("Hi :)", user)

	def sayGoodbye(self, Morphux, user):
		Morphux.sendMessage(user + " is dead...")
