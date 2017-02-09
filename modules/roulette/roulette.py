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
					"usage": "rinit",
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
				}
			}
		}
		self.users = {}
		self.onGame = 0
		self.count = 0
		self.base = 3
		self.bullet = 6
		return self.config

	def init(self, Morphux, infos):
		if (self.onGame == 0):
			Morphux.sendMessage(infos['nick'] + " just init the Russian Roulette ! Type !rjoin if you want to die :)")
			self.users[self.count] = infos['nick']
			self.onGame = 1
			self.count = 1
		elif (self.onGame == 1):
			Morphux.sendMessage("Game Already launch, type !rjoin", infos['nick'])
		else:
			Morphux.sendMessage("Already IG", infos['nick'])

	def join(self, Morphux, infos):
		if (self.onGame == 1):
			if (infos['nick'] not in self.users):
				self.users[self.count] = infos['nick']
				self.count += 1
				if (self.count != self.base):
					Morphux.sendMessage("<- BALLS HERE, need "+ str(self.base - self.count) +" more fools !", infos['nick'])
				else:
					Morphux.sendMessage("Let's begin...")
					self.onGame = 2
					self.count = 0
					Morphux.sendMessage("Your turn, type !rshot", self.users[self.count])
		else:
			Morphux.sendMessage("Init the roulette first !", infos['nick'])

	def shot(self, Morphux, infos):
		if (self.onGame == 2):
			if (infos['nick'] != self.users[self.count]):
				Morphux.sendMessage("Not your turn !", infos['nick'])
			else:
				bullet = random.randint(1, self.bullet)
				if (bullet == 1):
					Morphux.sendMessage("Ur so lucky.", infos['nick'])
					time.sleep(0.5)
					Morphux.sendMessage("JUST KIDDING U DED", infos['nick'])
					self.onGame = 0
					self.bullet = 6
					self.count = 0
					Morphux.kick(infos['nick'], "You shoot me down, bang bang")
				else:
					Morphux.sendMessage("Ur so lucky.", infos['nick'])
					self.bullet -= 1
					self.count += 1
					if (self.count == self.base):
						self.count = 0
					Morphux.sendMessage("Your turn ! ("+ str(self.bullet)+" bullets)", self.users[self.count])
