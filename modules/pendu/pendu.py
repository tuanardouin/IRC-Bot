class   Pendu:
    def command(self):
        self.word = ""
        self.hidden = ""
        self.lives = 10
        self.letters = list()
        self.ig = 0
        self.config = {
            "command": {
                "p": {
                    "function": self.letter,
                    "usage": "p <letter>",
                    "help": "Discover a letter. If the letter arg is non existent, print the current discovered word"
                },
                "pendu": {
                    "function": self.pendu,
                    "usage": "pendu <word> <hint>",
                    "help": "Send a new word the game. Might do it in /query though :) Hint is optionnal"
                }
            }
        }
        return self.config

    def pendu(self, Morphux, infos):
        if (len(infos['args']) == 0):
            Morphux.sendMessage("I might need a word", infos['nick']);
        elif self.ig == 1:
            Morphux.sendMessage("Already in game !", infos['nick']);
        else:
            self.word = infos['args'][0];
            print "Word: " + self.word
            self.hidden = "#" * len(self.word)
            print "Hidden: " + self.hidden
            self.hidden = self.word[0] + self.hidden[1:]
            print "Hidden: " + self.hidden
            self.hidden = self.hidden[:-1] + self.word[len(self.word) - 1]
            print "Hidden: " + self.hidden
            Morphux.sendMessage("New word by " + infos['nick'] + ": " + self.hidden);
            self.ig = 1

    def letter(self, Morphux, infos):
        if self.ig == 0:
            Morphux.sendMessage("Not in a game !", infos['nick']);
        elif (len(infos['args']) == 0):
            Morphux.sendMessage(self.hidden, infos['nick']);
        elif (len(infos['args'][0]) == 1):
            found = 0
            for i, c in enumerate(self.word):
                if c == infos['args'][0][0] and i != 0 and i != len(self.word) - 1:
                    self.hidden = list(self.hidden)
                    self.hidden[i] = c
                    self.hidden = "".join(self.hidden)
                    found = found + 1
            if found == 0:
                self.lives -= 1
                if self.lives == 0:
                    Morphux.sendMessage("No lives left, GAME OVER.");
                    self.end(Morphux)
                self.letters.append(infos['args'][0][0])
                Morphux.sendMessage("Nope. " + str(self.lives) + " lives. Letters tested: " + "".join(self.letters), infos['nick']);
            elif self.hidden == self.word:
                Morphux.sendMessage("GG.", infos['nick']);
                self.end(Morphux)
            else:
                Morphux.sendMessage("Nice ! " + self.hidden, infos['nick']);
        else:
            if self.word == infos['args'][0]:
                Morphux.sendMessage("Wow. wp.", infos['nick']);
                self.end(Morphux)
            else:
                self.lives -= 1
                if self.lives == 0:
                    Morphux.sendMessage("No lives left, GAME OVER.");
                    self.end(Morphux)
                else:
                    Morphux.sendMessage("Nope. " + str(self.lives) + " lives. Letters tested: " + "".join(self.letters), infos['nick']);

    def end(self, Morphux):
        Morphux.sendMessage("Word was " + self.word);
        self.lives = 10
        self.word = ""
        self.letters = list()
        self.hidden = ""
        self.ig = 0
