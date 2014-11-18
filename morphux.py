# Irc Bot Main file
# By: Louis <louis@ne02ptzero.me>

# Includes
import 		json
from core.Core import		Core
from pprint import pprint


class	Morphux:

	# Construct function
	# @param path of the config file (Optional)
	def 	__init__(self, path = "/etc/morphux/configBot.json"):
		fd = open(path)
		self.config = json.load(fd)
		self.currentUsers = {}
		self.join = {}
		self.leave = {}
		self.quit = {}
		self.nickChange = {}
		self.before = {}
		self.after = {}
		self.commands = {}

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
			before = 1
			self.getHeadersLine(line)
			if ("JOIN" in line):
				self.onJoin(line)
			elif ("PART" in line):
				self.onLeave(line)
			elif ("QUIT" in line):
				self.onQuit(line)
			elif ("NICK" in line):
				self.onNickChange(line)
			elif ("PRIVMSG" in line):
				infos = self.getInfo(line)
				for name, function in self.before.items():
					print name
					if (function(self, line) == 0):
						before = 0
				if (before == 0):
					self.s.CorePrint("Aborting treatement");
				elif (infos != False):
					if (infos["command"] in self.commands):
						self.commands[infos["command"]]["function"](self, infos)
						print("New command ["+ infos['nick'] +"]: " + infos["command"])
					else:
						self.sendMessage(self.config["errorMessage"], infos["nick"])
			for name, function in self.after.items():
				function(self, line)

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
	def 	getInfo(self, line, force = 0):
		infos = {}
		infos["fullLine"] = line
		args = line.split(":", 2)[2]
		args = args.split(" ")
		args = filter(None, args)
		if (args[0][0] != self.config["symbol"] and force == 0):
			return False
		if (force == 0):
			args[0] = args[0][1:]
		infos["command"] = args[0]
		args.remove(args[0])
		if (infos["command"] == "help"):
			self.showHelp(args)
			return False
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

	# Get modules in dictionnary
	def getCommands(self):
		commands = {}
		for name, klass in self.modules.items():
			self.s.CorePrint("Loading '"+ name +"' module...")
			klass = klass()
			result = klass.command()
			commands = result["command"]
			pprint(commands)
			if ("onJoin" in result):
				for name, function in result["onJoin"].items():
					self.join[name] = function
			if ("onLeave" in result):
				for name, function in result["onLeave"].items():
					self.leave[name] = function
			if ("onQuit" in result):
				for name, function in result["onQuit"].items():
					self.quit[name] = function
			if ("onNickChange" in result):
				for name, function in result["onNickChange"].items():
					self.nickChange[name] = function
			if ("before" in result):
				for name, function in result["before"].items():
					self.before[name] = function
			if ("after" in result):
				for name, function in result["after"].items():
					self.after[name] = function
			for name, function in commands.items():
				commands[name] = function
			self.s.printOk("OK")
			self.commands.update(commands)


	# On User Join
	# @param: string
	def onJoin(self, line):
		user = line.split(" ")
		user[0] = user[0][1:]
		self.currentUsers[user[0].split("!")[0]] = True
		if (user[0].split("!")[0] == self.config['nick']):
			return
		for name, function in self.join.items():
			function(self, user[0].split("!")[0])

	# On Nick Change
	# @param: string
	def onNickChange(self, line):
		user = line.split(" ")
		user[0] = user[0][1:]
		userName = user[0].split("!")
		newNick = user[2][1:]
		if (userName[0] in self.currentUsers):
			del self.currentUsers[userName[0]]
			self.currentUsers[newNick] = True
		if (newNick == self.config['nick']):
			return
		for name, function in self.nickChange.items():
			function(self, userName[0], newNick)


	# Get Initial list of Users
	# @param: string
	def getHeadersLine(self, line):
		line = line.split("\n")
		for value in line:
			users = value.split(":")
			if (len(users) >= 2):
				details = users[1].split(" ")
				if (len(details) >= 2):
					if (details[1] == "353"):
						users = users[2].split(" ")
						for nickName in users:
							nickName = nickName.split("\r\n")[0]
							nickName = nickName.split("\r")[0]
							if (nickName[0] == '@'):
								nickName = nickName[1:]
								self.currentUsers[nickName] = {"isAdmin": 1}
							else:
								self.currentUsers[nickName] = True

	# On User Leave
	# @param: string
	def onLeave(self, line):
		user = line.split(" ")[0][1:]
		nickName = user.split("!")[0]
		if (nickName in self.currentUsers):
			del self.currentUsers[nickName]
		for name, function in self.leave.items():
			function(self, nickName)

	# On User QUIT
	# @param: string
	def onQuit(self, line):
		user = line.split(" ")[0][1:]
		nickName = user.split("!")[0]
		if (nickName in self.currentUsers):
			del self.currentUsers[nickName]
		for name, function in self.quit.items():
			function(self, nickName)

	# If User is connected
	# @param: string
	def userExists(self, nick):
		if (nick in self.currentUsers):
			return True
		else:
			return False

	# If User is Admin
	# @param: string
	def isAdmin(self, nick):
		if (self.userExists(nick)):
			if (self.currentUsers[nick] != True):
				if ('isAdmin' in self.currentUsers[nick]):
					return True
		return False

	# Show Help for a command
	# @param: list
	def showHelp(self, args):
		if (args[0] in self.commands):
			usage = self.commands[args[0]]["usage"]
			help = self.commands[args[0]]["help"]
			self.sendMessage(args[0] +": <"+ usage +"> ("+help+")")
		else:
			self.sendMessage("Can't find command " + args[0])

	# Kick an user
	def kick(self, user, reason):
		self.s.kick(user, reason)
