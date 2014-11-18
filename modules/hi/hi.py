
class Hi:
	def command(self):
		self.config = {
			"command": {
				"hi": {
					"function": self.hiCommand,
					"usage": "hi",
					"help": "Say hi to the bot"
				},
				"cake": {
					"function": self.someCake,
					"usage": "cake <user>",
					"help": "Give a piece of cake to someone !"
				}
			},
			"onJoin": {
				'sayHello' :self.sayHello
			},
			"onLeave": { 
				'sayGoodbye': self.sayGoodbye
			},
			"onNickChange": {
				'newNick': self.newNick
			},
			"onQuit": {
				'quit': self.quit
			},
			"before": {
				'before': self.before
			},
			"after": {
				'after': self.after
			}
		}
		return self.config

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

	def newNick(self, Morphux, oldNick, newNick):
		Morphux.sendMessage(oldNick + " change to " + newNick)

	def quit(self, Morphux, nick):
		Morphux.sendMessage(nick + " quit !")

	def before(self, Morphux, line):
		#Morphux.sendMessage("Before: " + line)
		return 1;

	def after(self, Morphux, line):
		print "after YAY " + line
