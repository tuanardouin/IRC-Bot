# Base Module
# By: Louis <louis@ne02ptzero>

import urllib.request
import lxml.etree
import random
import re

class Base:

    def ping(self, Morphux, infos):
        Morphux.sendMessage("Pong !", infos['nick'])

    def join(self, Morphux, user):
        Morphux.sendMessage("Hey, howr u doin :) ?", user)

    def nyan(self, Morphux, infos):
        Morphux.sendMessage(str("telnet nyancat.dakko.us"), infos['nick'])

    def ah(self, Morphux, infos):
        Morphux.sendMessage("https://youtu.be/XE6YaLtctcI", infos['nick'])

    def wow(self, Morphux, infos):
        Morphux.sendMessage("https://www.youtube.com/embed/jUy9_0M3bVk?autoplay=1", infos['nick'])

    @staticmethod
    def youtube_url_validation(url):
        youtube_regex = (
            r'(https?://)?(www\.)?'
            '(youtube|youtu|youtube-nocookie)\.(com|be)/'
            '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
        youtube_regex_match = re.match(youtube_regex, url)
        if youtube_regex_match:
            return youtube_regex_match.group(6)
        return youtube_regex_match

    def youtube(self, Morphux):
        if "https://www.youtube.com/watch" in line:
            urls = [t for t in line.split() if self.youtube_url_validation(t)]
            for url in urls:
                youtube = lxml.etree.HTML(urllib.request.urlopen(url).read())
                video_title = youtube.xpath("//span[@id='eow-title']/@title")
                if video_title:
                    Morphux.sendMessage(video_title)


    def command(self):
        self.config = {
            "command": {
                "ping": {
                    "function": self.ping,
                    "usage": "ping",
                    "help": "Make a ping to the bot"
                },
                "nyan": {
                    "function": self.nyan,
                    "usage": "nyan",
                    "help": "nyannyannyannyannyan"
                },
                "ah": {
                    "function": self.ah,
                    "usage": "ah",
                    "help": "AH !"
                },
                "wow": {
                    "function": self.wow,
                    "usage": "wow",
                    "help": "Wooow !"
                }
            },
            "onJoin": {
                "join": self.join
            }
        }
        return self.config
