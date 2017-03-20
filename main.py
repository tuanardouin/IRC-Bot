#!/usr/bin/python
# -*- coding: utf8 -*-
# IRC MORPHUX BOT v2
# By: Louis <louis@ne02ptzero.me>
#18:09  @Ne02ptzero: !ascii CL4P_TP 
#18:09  @CL4P_TP:    _____ _   _  _   _____     _______ _____
#18:09  @CL4P_TP:   / ____| | | || | |  __ \   \__   __|  __ \
#18:09  @CL4P_TP:  | |    | | | || |_| |__) |     | |  | |__) |
#18:09  @CL4P_TP:  | |    | | |__   _|  ___/      | |  |  ___/
#18:09  @CL4P_TP:  | |____| |____| | | |          | |  | |
#18:09  @CL4P_TP:   \_____|______|_| |_|          |_|  |_|
#18:09  @CL4P_TP:                        ________
#18:09  @CL4P_TP:                       |________|


from morphux 	import		Morphux
import time
import imp
import sys
# sys.setdefaultencoding() does not exist, here!
imp.reload(sys)  # Reload does the trick!
#sys.setdefaultencoding('UTF8')

main = Morphux("config.json")
main.connect()
main.loadModules()
main.loop()
