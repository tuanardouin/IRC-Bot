# Irc Bot Main file
# By: Louis <louis@ne02ptzero.me>

# Includes
import 		json
from core.Core import		Core


class	Morphux:

	# Construct function
	# @param path of the config file (Optional)
	def 	__init__(self, path = "/etc/morphux/configBot.json"):
		fd = open(path)
		self.config = json.load(fd)

	# Connect the bot to the server and the chan
	def 	connect(self):
		self.s = Core(self.config)
		if (self.config["identify"] != 0):
			self.s.identify()
		self.s.join()
		self.s.send(self.config["welcomeMessage"])

	# Main Loop
	def 	loop(self):
		while 1:
			line = self.s.getLine()
			# Treat Line
			if ("PRIVMSG" in line):
				infos = self.getInfo(line)
				if (infos != False):
					if (infos["command"] in self.commands):
						self.commands[infos["command"]](self, infos)
					else:
						self.sendMessage("Don't know this command :(", infos["nick"])

	# Send message
	# @param: string
	# @param: string (Optional)
	def 	sendMessage(self, string, user = False):
		if (user != False):
			self.s.send(user + ": " + string)
		else:
			self.s.send(string)

	# Get Line Information
	# @param: string
	def 	getInfo(self, line):
		infos = {}
		infos["fullLine"] = line
		args = line.split(":", 2)[2]
		args = args.split(" ")
		args = filter(None, args)
		if (args[0][0] != self.config["symbol"]):
			return False
		args[0] = args[0][1:]
		infos["command"] = args[0]
		args.remove(args[0])
		infos["args"] = args
		user = line.split(":", 2)[1]
		infos["fullUser"] = user.split(" ")[0]
		infos["nick"] = user.split("!", 2)[0]
		return infos;

	# Load Modules
	# @param: path (Optional)
	def loadModules(self, path = "modules"):
		res = {}
		import os
		lst = os.listdir(path)
		dir = []
		for d in lst:
			s = os.path.abspath(path) + os.sep + d
			if os.path.isdir(s) and os.path.exists(s + os.sep + "__init__.py"):
				dir.append(d)
		for d in dir:
			res[d] = __import__(path + "." + d + "." + d, fromlist = ["*"])
			res[d] = getattr(res[d], d.title())
		self.modules = res
		self.getCommands()

	def getCommands(self):
		result = {}
		for name, klass in self.modules.items():
			self.s.CorePrint("Loading '"+ name +"' module...")
			klass = klass()
			commands = klass.command()
			for name, function in commands.items():
				result[name] = function
			self.s.printOk("OK")
		self.commands = result
