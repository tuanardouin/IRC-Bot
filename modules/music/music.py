# Music Module
# By: abclive <rapasti@student.42.fr>

import random
import json

class Music:

	def 	__init__(self):
		self.websites = ["youtu", "deezer", "soundcloud", "grooveshark"]

	def command(self):
		self.config = {
			"command": {
				"music": {
					"function": self.music,
					"usage": "music <suggest|shake|reset>",
					"help": "Suggest a music or query the music database"
				}
			}
		}
		return self.config;

	def music(self, Morphux, infos):
		if (len(infos['args']) == 0):
			Morphux.sendMessage("Please specify a sub-command: <suggest|shake>", infos['nick'])
		elif (infos['args'][0] == "suggest"):
			if (len(infos['args']) >= 2 and len(infos['args'][1]) > 0):
				if (self.canAddLink(infos['args'][1]) == False):
					Morphux.sendMessage("This website is not supported yet.", infos['nick'])
				else:
					ret = self.addDatabaseEntry({
						'user': infos['nick'],
						'link': infos['args'][1]
						})
					if (ret):
						Morphux.sendMessage("Added your suggestion to the database!", infos['nick'])
					else:
						Morphux.sendMessage("I already know that song!", infos['nick'])
			else:
				Morphux.sendMessage("Sharing emptiness is not that interesting.", infos['nick'])
		elif (infos['args'][0] == "shake"):
			entry = self.readRandomEntry()
			if (entry != False):
				Morphux.sendMessage(entry['user'] + " recommends you " + entry['link'], infos['nick'])
			else:
				Morphux.sendMessage("The music database is empty. It's a shame.", infos['nick'])
		elif (infos['args'][0] == "reset"):
			if (Morphux.isAdmin(infos['nick'])):
				self.resetDatabase()
				Morphux.sendMessage("Database have been cleared :(", infos['nick'])
			else:
				Morphux.sendMessage("Nope nope nope. You're not admin. You will not clear the music database.", infos['nick'])
		else:
			Morphux.sendMessage("Nope I don't know this one.", infos['nick'])

	def canAddLink(self, link):
		for website in self.websites:
			if (link.find(website) != -1):
				return True;
		return False;

	def addDatabaseEntry(self, data):
		fd = open("modules/music/database.json", "r+")
		database = json.load(fd)
		for d in database['entries']:
			if (data['link'] == d['link']):
				fd.close()
				return False
		database['entries'].append(data)
		fd.seek(0)
		fd.write(json.dumps(database, indent = 2))
		fd.truncate()
		fd.close()
		return True

	def readRandomEntry(self):
		fd = open("modules/music/database.json", "r")
		database = json.load(fd)
		if (len(database['entries']) == 0):
			return False
		rand = random.randrange(len(database['entries']))
		return database['entries'][rand]

	def resetDatabase(self):
		fd = open("modules/music/database.json", "r+")
		fd.seek(0)
		fd.truncate()
		fd.write(json.dumps({"entries": []}, indent = 2))
		fd.close()

