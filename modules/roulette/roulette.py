# Russian Roulette
# By: Louis <louis@ne02ptzero.me>

import 		random
import 		time

class Roulette:
	def command(self):
		self.config = {
			"command": {
				"rinit": {
					"function": self.init,
					"usage": "rinit players bullets",
					"help": "Init the Russian Roulette"
				},
				"rjoin": {
					"function": self.join,
					"usage": "rjoin",
					"help": "Join the Russian Roulette"
				},
				"rshot": {
					"function": self.shot,
					"usage": "rshot",
					"help": "Shot yourself, or not."
				},
				"rpass": {
				"function": self.passTheGun,
			"usage": "rpass",
				"help": "Pass the gun"
				}
			}
		}
		self.users = []
		self.onGame = 0
		self.count = 0
		self.base = 3
		self.bullet = 6
		return self.config

	def init(self, Morphux, infos):
		if (self.onGame == 0):
			Morphux.sendMessage(infos['nick'] + " just started the Russian Roulette ! Type !rjoin if you want to die :)")
			if len(infos['args']) > 0:
				if infos['args'][0].isdigit() == True and int(infos['args'][0]) > 0:
					self.base = int(infos['args'][0])
			if len(infos['args']) > 1:
				if infos['args'][1].isdigit == True and int(infos['args'][1]) > 0:
					self.bullet = int(infos['args'][1])
			self.users.append(infos['nick'])

			self.onGame = 1
			self.count = 1
		elif (self.onGame == 1):
			Morphux.sendMessage("Game Already launched, type !rjoin", infos['nick'])
		else:
			Morphux.sendMessage("Already IG", infos['nick'])

	def join(self, Morphux, infos):
		if (self.onGame == 1):
			if (infos['nick'] not in self.users):
				self.users.append(infos['nick'])
				self.count += 1
				if (self.count != self.base):
					Morphux.sendMessage("<- BALLS HERE, need "+ str(self.base - self.count) +" more fools !", infos['nick'])
				else:
					Morphux.sendMessage("Let's begin...")
					self.onGame = 2
					self.count = 0
					Morphux.sendMessage("Your turn, type !rshot", self.users[self.count])
			else:
				Morphux.sendMessage("You're already in!", infos['nick'])


	def start(self, Morphux, infos):
		Morphux.sendMessage("Let's begin...")
		self.base = self.count
		self.onGame = 2
		self.count = 0
		Morphux.sendMessage("Your turn, type !rshot", self.users[self.count])
		if self.onGame == 0:
			Morphux.sendMessage("Init the roulette first !", infos['nick'])

	def shot(self, Morphux, infos):
		if (self.onGame == 2):
			if (infos['nick'] != self.users[self.count]):
				Morphux.sendMessage("Not your turn !", infos['nick'])
			else:
				bullet = random.randint(1, self.bullet)
				if (bullet == 1):
					Morphux.sendMessage("SO BAD IT HURTS", infos['nick'])
					self.onGame = 0
					self.base = 3
					self.bullet = 6
					self.count = 0
					self.users = []
					Morphux.kick(infos['nick'], "You shoot me down, bang bang")
				else:
					self.bullet -= 1
					self.count += 1
					if (self.count == self.base):
						self.count = 0
					Morphux.sendMessage("Your turn ! ("+ str(self.bullet)+" bullets)", self.users[self.count])

	def passTheGun(self, Morphux, infos):
		if self.onGame == 2:
			if infos['nick'] == self.users[self.count]:
				self.count += 1
				if (self.count >= self.base):
					self.count = 0
				Morphux.sendMessage("Your turn ! ("+ str(self.bullet)+" bullets)", self.users[self.count])
			else:
				Morphux.sendMessage("Not your turn! Currently playing is "+self.users[self.count], infos['nick'])
		else:
			Morphux.sendMessage("You need to init/start the roulette first", infos['nick'])
