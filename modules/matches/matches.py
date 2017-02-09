# Morphux-IRC-BOT
# Matches game
# By Noich

import	random

class Matches:
		def command(self):
			self.config = {
				"command": {
					"matches": {
						"function": self.matchesCommand,
						"usage": "matches [user]",
						"help": "Duel another user in a matches game"
					},
					"game": {
						"function": self.gameCommand,
						"usage": "game",
						"help": "Starts the matches fight"
					},
					"decline": {
						"function": self.declineCommand,
						"usage": "decline",
						"help": "Refuses the matches fight"
					},
					"remove": {
						"function": self.removeMatches,
						"usage": "remove [1-2-3]",
						"help": "Removes a number of matches"
					},
					"abort": {
						"function": self.abortMatch,
						"usage": "abort",
						"help": "Aborts the current game before it starts"
					},
					"forfeit": {
						"function": self.resetGame,
						"usage": "forfeit",
						"help": "Resets the game if one of the players is afk or not playing"
					},
					"confirm": {
						"function": self.botGame,
						"usage": "confirm",
						"help": "confirms that you wanna play vs a bot"
					}
				}
			}
			self.botPlayer = 0
			self.matchStarted = 0
			self.firstPlayer = 0
			self.secondPlayer = 0
			self.currentPlayer = 0
			self.matchesNumber = 0
			self.waitingPlayer = 0
			return self.config
		def matchesCommand(self, Morphux, infos):
			if (self.matchStarted == 0):
				if (len(infos['args']) == 0):
					Morphux.sendMessage("Type !confirm to play against me!", infos['nick'])
					self.firstPlayer = infos['nick']
				elif (infos['args'][0] == infos['nick']):
					Morphux.sendMessage("Choose ANOTHER player", infos['nick'])
				elif (Morphux.userExists(infos['args'][0])):
					Morphux.sendMessage("Hey " + infos['args'][0] + ", " + infos['nick'] + " wants to play a game of matches with you! !game or !decline")
					self.secondPlayer = infos['args'][0]
					self.firstPlayer = infos['nick']
					self.matchStarted = 1
					self.waitingPlayer = 1
				else:
					Morphux.sendMessage("No such user " + infos['args'][0] + " :(", infos['nick'])
			else:
				Morphux.sendMessage("A match is already started")
		def gameCommand(self, Morphux, infos):
			if (self.secondPlayer != infos['nick']):
				Morphux.sendMessage("Not you!")
			else:
				self.waitingPlayer = 0;
				self.matchesNumber = random.randint(15, 25)
				Morphux.sendMessage("There are " + str(self.matchesNumber) + " matches on the board.")
				randFirst = random.randint(1, 2)
				if (randFirst == 1):
					self.currentPlayer = self.firstPlayer
				else:
					self.currentPlayer = self.secondPlayer
				Morphux.sendMessage("Its " + str(self.currentPlayer) + " time to play.")
		def declineCommand(self, Morphux, infos):
			if (self.secondPlayer == infos['nick']):
				Morphux.sendMessage("No time to play, I see...", infos['nick'])
				self.matchStarted = 0
		def abortMatch(self, Morphux, infos):
			if (self.matchStarted == 0):
				Morphux.sendMessage("No matches game running yet", infos['nick'])
			elif (self.matchStarted == 1 and self.waitingPlayer == 0):
				Morphux.sendMessage("The match is already started")
			elif (self.matchStarted == 1 and self.waitingPlayer == 1):
				Morphux.sendMessage("Cancelling current matches game")
				self.waitingPlayer = 0
				self.matchStarted = 0
				self.firstPlayer = 0
				self.secondPlayer = 0
		def removeMatches(self, Morphux, infos):
			if (self.matchStarted == 1):
				if (self.currentPlayer != infos['nick']):
					Morphux.sendMessage("Not you!")
				else:
					if (len(infos['args']) > 0 and infos['args'][0].isdigit() and int(infos['args'][0]) >= 1 and int(infos['args'][0]) <= 3):
						self.matchesNumber -= int(infos['args'][0])
						if (self.matchesNumber <= 0):
							Morphux.sendMessage(infos['nick'] + " just lost the game!")
							Morphux.kick(infos['nick'], "No noobs in my chan")
							self.waitingPlayer = 0
							self.matchStarted = 0
							self.firstPlayer = 0
							self.secondPlayer = 0
						else:
							if (int(infos['args'][0]) > 1):
								Morphux.sendMessage(infos['nick'] + " removed " + str(infos['args'][0]) + " matches, " + str(self.matchesNumber) + " remaining")
							else:
								Morphux.sendMessage(infos['nick'] + " removed " + str(infos['args'][0]) + " match, " + str(self.matchesNumber) + " remaining")
							if (self.currentPlayer == self.firstPlayer):
								self.currentPlayer = self.secondPlayer
							else:
								self.currentPlayer = self.firstPlayer
							if (self.botPlayer == 1):
								self.matchesNumber -= int(4 - int(infos['args'][0]))
								if (4 - int(infos['args'][0]) == 1):
									Morphux.sendMessage("I'm removing 1 match, " + str(self.matchesNumber) + " remaining")
								else:
									Morphux.sendMessage("I'm removing " + str(4 - int(infos['args'][0])) + " matches, " + str(self.matchesNumber) + " remaining")
								self.currentPlayer = self.firstPlayer
					else:
						Morphux.sendMessage("1 to 3 matches only!")
			else:
				Morphux.sendMessage("Not in playmode!")
		def resetGame(self, Morphux, infos):
			if ((infos['nick'] == self.firstPlayer or infos['nick'] == self.secondPlayer) and (self.matchStarted == 1 or self.waitingPlayer == 1)):
				self.botPlayer = 0
				self.waitingPlayer = 0
				self.matchStarted = 0
				self.firstPlayer = 0
				self.secondPlayer = 0
				Morphux.sendMessage("Game have been cancelled by " + infos['nick'] + ". Kick him for me if he was gonna lose!")
			elif(self.matchStarted == 1 or self.waitingPlayer == 1):
				Morphux.sendMessage("Not you!", infos['nick'])
			else:
				Morphux.sendMessage("Not ingame!", infos['nick'])
		def botGame(self, Morphux, infos):
			if (self.waitingPlayer == 1):
				Morphux.sendMessage("You already dueled a real human (and thus have better chances of winning)", infos['nick'])
			if (self.matchStarted == 1):
				Morphux.sendMessage("A game is already running", infos['nick'])
			if (0 == 1):
				Morphux.sendMessage("Not you!", infos['nick'])
			else:
				self.botPlayer = 1
				self.secondPlayer = 0
				self.matchesNumber = random.randint(15, 25)
				self.currentPlayer = self.firstPlayer
				Morphux.sendMessage("There are " + str(self.matchesNumber) + " matches on the board.")
				if ((self.matchesNumber % 4) != 1):
					self.currentPlayer = self.firstPlayer
					Morphux.sendMessage("May I start? Thank you.")
					if (((self.matchesNumber - 1) % 4) == 1):
						Morphux.sendMessage("I'm removing 1 match, " + str(self.matchesNumber - 1) + " remaining")
						self.matchesNumber = self.matchesNumber - 1
					elif (((self.matchesNumber - 2) % 4) == 1):
						Morphux.sendMessage("I'm removing 2 matches, " + str(self.matchesNumber - 2) + " remaining")
						self.matchesNumber = self.matchesNumber - 2
					elif (((self.matchesNumber - 3) % 4) == 1):
						Morphux.sendMessage("I'm removing 3 matches, " + str(self.matchesNumber - 3) + " remaining")
						self.matchesNumber = self.matchesNumber - 3
				else:
					Morphux.sendMessage("Its " + str(self.currentPlayer) + " time to play.")
				self.matchStarted = 1
