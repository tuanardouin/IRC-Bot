# Core functions
# By: Louis <louis@ne02ptzero.me>

# Includes
import socket
import sys
import time

class   Core:

        # Construct functions
        # @param: config file (json.load)
        def __init__(self, config):
                self.config = config
                self.socket =   socket.socket()
                self.CorePrint("Connection to " + config["host"] + " at port " + config["port"] + "...");
                try:
                        self.socket.connect((config["host"], int(config["port"])))
                except socket.gaierror:
                        self.printError("Error at connection.", 1)
                self.coreSend("NICK " + config["nick"])
                self.coreSend("USER " + config["nick"] + " " + config["nick"] + " " + config["nick"] + " :Bot")
                self.printOk("OK")

        # Print Core Function, without \n
        # @param: string
        def CorePrint(self, string):
                if (self.config["debug"] == 1):
                        print(string)

        # Print Ok function in green color
        # @param: string
        def printOk(self, string):
                if (self.config["debug"] == 1):
                        print("\033[0;32m"+ string +"\033[0m");

        # Print Error function, in red
        # @param: int (Optional)
        def printError(self, string, die = False):
                if (self.config["debug"] == 1):
                        print("\033[0;31m"+ string +"\033[0m");
                if (die != False):
                        sys.exit(die)

        # Send a message to server, w/ \r\n
        # @param: string
        def coreSend(self, string):
                self.socket.send(str.encode(string + "\r\n"));

        # Send a message to channel
        # @param: string
        def send(self, string):
                self.coreSend("PRIVMSG " + self.config["chan"] + " :" + string)

        # Identify bot to the server
        def identify(self):
                self.coreSend("PRIVMSG NickServ :identify " + self.config["password"])

        # Kick someone of the channel
        # @param: string
        # @param: string (Optional)
        def kick(self, user, message = ""):
                if (message == ""):
                        message = self.config["banMessage"]
                self.coreSend("KICK " + self.config["chan"] + " " + user + " : " + message)

        # Join a channel
        def join(self):
                self.CorePrint("Join " + self.config["chan"]);
                self.coreSend("JOIN " + self.config["chan"])
                self.printOk("OK");

        def getLine(self):
                line = self.socket.recv(4096)
                try:
                    l_str = line.decode("utf-8", "strict")
                except UnicodeError:
                    l_str = line.decode("latin-1", "strict").encode("utf-8").decode("utf-8")
                # If that's a ping from server
                if ("PING :" in l_str):
                        self.coreSend("PONG " + l_str.split(" ")[1])
                print(">>>" + l_str)
                return l_str.strip("\r\n")
