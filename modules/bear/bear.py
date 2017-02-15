#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Bear Module
# By: Enerdhil <hezardj@gmail.com>

class Bear:

	def command(self):
		self.config = {
			"command": {
				"bear": {
					"function": self.bear,
					"usage": "bear",
					"help": "Hey, you can make bears"
				}
			}
		}
		return self.config

	def bear(self, Morphux, infos):
		Morphux.sendMessage("ʕ•ᴥ•ʔ", infos['nick'])
