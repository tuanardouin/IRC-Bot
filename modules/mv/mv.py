class Mv:
  def command(self):
    self.config = {
      "command": {
        "mv": {
          "function": self.mvScreams,
          "usage": "mv <user>",
          "help": "Le clavier y colle!"
        }
      }}
    return self.config

  def mvScreams(self, Morphux, infos):
    print(infos)
    if (len(infos['args']) == 0 and infos['nick'] == "valouche"):
      Morphux.sendMessage("Ta mere la chauve", infos['nick'])
    elif (len(infos['args']) == 0 and infos['nick'] == "Ne02ptzero"):
      Morphux.sendMessage("TU VAS LA CHIER TA CHIASSE?", infos['nick'])
    elif (len(infos['args']) == 0):
      Morphux.sendMessage("SARACE BOULBA", infos['nick'])
    elif (Morphux.userExists(infos['args'][0])):
      Morphux.sendMessage("Respecte toi " + infos['nick'] + "!", infos['args'][0])
    elif (infos['args'][0] == "allow"):
      Morphux.sendMessage("ALLOW?", infos['nick'])
    elif (infos['args'][0] == "thunes"):
      Morphux.sendMessage("Money equals power", infos['nick'])
    elif (infos['args'][0] == "theodule"):
      Morphux.sendMessage("THEODUUULE", infos['nick'])
    elif (infos['args'][0] == "gg"):
      Morphux.sendMessage("Le beau jeu le beau geste.", infos['nick'])
