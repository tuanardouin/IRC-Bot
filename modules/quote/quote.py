# Morphux-IRC-BOT
# Quote save system
# By Noich

import	json

class Quote:
		def command(self):
			self.config = {
				"command": {
					"quote": {
						"function": self.fetchQuote,
						"usage": "quote [number]",
						"help": "fetches a quote from previously saved quotes"
					},
					"savequote": {
						"function": self.saveQuote,
						"usage": "savequote #author [quote]",
						"help": "saves a quote with its author"
					},
					"qsearch": {
						"function": self.searchQuote,
						"usage": "qsearch [args]",
						"help": "searches a quote based on given args"
					}
				}
			}
			json_data = open('quote.json')
			self.quoteList = json.load(json_data)
			self.quote = [None, None, None]

		def fetchQuote(self, Morphux, infos):
			if (len(infos['args']) == 0):
				Morphux.sendMessage("I have " + str(len(self.quoteList))  +" quotes available. Choose one", infos['nick']);
			elif (infos['args'][0].isdigit() == False):
				Morphux.sendMessage("No such quote - Nice Try!", infos['nick']);
			elif (int(infos['args'][0]) < len(self.quoteList)):
				Morphux.sendMessage("Quote #" + infos['args'][0] + ", By: " + str(self.quoteList[int(infos['args'][0])][1]) + ", " + str(quoteList[int(infos['args'][0])][0]), infos['nick']);
				Morphux.sendMessage(str(self.quoteList[int(infos['args'][0])][2]));
			else:
				Morphux.sendMessage("No such quote - Nice Try!", infos['nick']);

		def saveQuote(self, Morphux, infos):
			if (len(info['args']) == 0):
				Morphux.sendMessage("I dont have anything to save, cmon!", infos['nick']);
			else:
				if (infos['args'][0] == ""):
					Morphux.sendMessage("OMG BUG");
				elif (infos['args'][0][0] != '#'):
					Morphux.sendMessage("Your first argument is supposed to be #author. God you're stupid.", infos['nick']);
				else:
					self.quote = [None, None, None];
					i = 0
					self.quote[0] = time.strftime("%d/%m/%Y")
					self.quote[1] = str(infos['args'][0][1:])
					for arg in infos['args']:
						if (i > 0):
							if self.quote[2] is None:
								self.quote[2] = str(arg);
							else:
								self.quote[2] += str(' ')
								self.quote[2] += str(arg);
						else:
							i = 1;
					self.quoteList[len(self.quoteList):] = [self.quote]
					with open('quote.json', 'w') as f:
						json.dump(self.quoteList, f);
					f.close()
					Morphux.sendMessage("Quote saved as #" + self.quoteList[len(self.quoteList):-1], infos['nick'])

		def searchQuote(self, Morphux, infos):
			if (len(args) == 0):
				Morphux.sendMessage("Need a keyword", infos['nick']);
			else:
				i = 0
				result = ""
				while i < len(quote_list):
					if (args[0] in quote_list[i][2]):
						result = result + str(i) + ","
					i = i + 1
				if (result == ""):
					Morphux.sendMessage("No quote found.", infos['nick']);
				else:
					Morphux.sendMessage("Quote(s) found: " + result[:-1], infos['nick']);

