# Compile C modules
# By: Louis <louis@ne02ptzero.me>

from subprocess import call
from subprocess import Popen, PIPE

class C:
	def command(self):
		self.config = {
			"command": {
				"c": {
					"function": self.compile,
					"usage": "code",
					"help": "Compile some code"
				}
			}
		}
		self.begin = "#include <stdio.h> \n \
		#include <stdlib.h> \n \
		int main(void) {\n"
		return self.config

	def compile(self, Morphux, infos):
		str = ""
		f = open("/tmp/irc.c", 'w')
		for args in infos["args"]:
			if (str == ""):
				str = args
			else:
				str = str + " " + args
		if ("malloc" in str or "calloc" in str or "write" in str or "fork" in str or "realloc" in str or "open" in str):
			Morphux.sendMessage("Unauthorized operation.", infos["nick"])
			return
		f.write(self.begin + str + " }")
		f.close();
		cmd = Popen(['/usr/bin/gcc', '-Wall', '-Wextra', '-Werror', '/tmp/irc.c', '-o', '/tmp/bin'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
		output = cmd.communicate(b"input data that is passed to subprocess' stdin")
		rc = cmd.returncode
		if (rc != 0):
			for err in output[1].splitlines():
				Morphux.sendMessage(err, infos["nick"]);
		else:
			cmd = Popen(['/usr/bin/timeout', '1', '/tmp/bin'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
			output = cmd.communicate(b"input data that is passed to subprocess' stdin")
			i = int(0)
			for err in output[0].splitlines():
				if (i >= 5):
					break
				Morphux.sendMessage(err, infos["nick"]);
				i += 1
