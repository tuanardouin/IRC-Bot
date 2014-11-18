
class Hi:
	def command(self):
		command = {"hi": self.hiCommand, "set": self.hiSet, "show": self.show}
		return command

	def hiCommand(self, Morphux, infos):
		Morphux.sendMessage("Hello !", infos['nick'])

	def hiSet(self, Morphux, infos):
		self.i = infos['args'][0]

	def show (self, Morphux, infos):
		Morphux.sendMessage(self.i)
