"""
This module allows people to votekick someone, if half of the people in the 
chan vote, the target will be kicked
"""

class Zoulette:
    def command(self):
        # Set config needed for a module
        self.config = {
            "command": {
                "zoulette": {
                    "function": self.zouletteMain,
                    "usage": "zoulette [user]",
                    "help": "zoulette someone"
                }
            }
        }
        # Define all variables ill need
        # For information, these variables will persists, don't forget to reset them

        # Is the zoulette launched ?
        self.zouletteLaunched = 0
        # How many people already voted ?
        self.zouletteCount = 0
        # Name of the zouletted guy
        self.zouletteName = ""
        # Identities of voters, so they can't vote twice
        self.votes = []
        # Identity of the last voter (I need an array because i split a string)
        # May not be the best method, but it works
        self.uniq_id = []
        return self.config

    def zouletteMain(self, Morphux, infos):
        """
        Split IRC message line to get user host mask
        for info an IRC line looks like this
        :Tracey`^!me@68.178.52.73 PRIVMSG #game1 :She's dead. Keep laughing.
        we want this part : me@68.178.52.73 to identify an user and make sure
        he can't vote twice
        """
        self.uniq_id = infos["fullUser"].split("!")
        # Checking if we got something, we don't want to crash
        if (len(self.uniq_id) > 1):
            # Checking if zoulette is already launched
            if (self.zouletteLaunched == 0):
                # If zoulette is not launched, checking if an arg is passed
                if (len(infos['args']) == 0):
                    Morphux.sendMessage("You have to target someone !", infos['nick'])
                # If user wants to zoulette himslef, fuck him right in the pussy
                elif ((infos['args'][0] == infos['nick'])):
                    Morphux.kick(infos['nick'], "You're right.")
                # If user wants to zoulette someone else, check if this guy exists
                elif (Morphux.userExists(infos["args"][0]) == False):
                    # Set the zoulette state as launched
                    self.zouletteLaunched = 1
                    # Set the number of votes to one
                    self.zouletteCount = 1
                    # Append the voter identity to our array
                    self.votes.append(self.uniq_id[1])
                    # Get the name of the zouletted guy
                    self.zouletteName = infos['args'][0]
                    # Announce what we've done
                    Morphux.sendMessage("You just launched a zoulette against " + infos['args'][0], infos['nick'])
                else:
                    Morphux.sendMessage("User '" + infos['args'][0] + "' does not exists" , infos['nick'])
            # If zoulette is already launched
            else:
                # If the voter didn't vote yet
                if (self.uniq_id[1] not in self.votes):
                    # Announce what we do
                    Morphux.sendMessage("You just voted against " + self.zouletteName, infos['nick'])
                    # Increment number of votes
                    self.zouletteCount += 1
                    # Append the voter identity to our array
                    self.votes.append(self.uniq_id[1])
                # If the voter already voted, tell him to GTFO
                else:
                    Morphux.sendMessage("You can't vote twice little filou !", infos['nick'])
                # If the number of vote exceed half of the people presents in the chan
                if (self.zouletteCount > len(Morphux.currentUsers) / 2):
                    # Kick the target
                    Morphux.kick(self.zouletteName, "We call it democracy.")
                    # Reset variables
                    self.zouletteLaunched = 0
                    self.zouletteCount = 0
                    self.zouletteName = ""
                    self.votes = []
