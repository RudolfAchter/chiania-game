import random
import json
import os
from pprint import pprint
import chiania
import config.settings
import inspect
#regular expressions
import re

"""
class player
    the player class represents the person playing this game
    the person:
    - sends commands
        - something like `!go north` `!talk character` `!pickup key`
    - controls a character
"""
class player:
    def __init__(self):
        self.name = "Player1"
        self.character = chiania.character()
    def command(self,line):
        match = re.search('^\!([A-Za-z0-9]+)(| (.*))$',line)
        cmd = None
        param = None
        if not match is None:
            cmd=match.group(1)
            if match.group(3) is None:
                param=""
            else:
                param=match.group(3)
            print("cmd: '" + cmd + "' param: '" + param + "'")
        if cmd == "go":
            self.character.go(param)
        if cmd == "look":
            self.character.look() # has no param


"""
class character
    the character class represents the character the player is
    controlling
    the character:
    - is on a location (room)
    - has a status
    - has equipment
    - has inventory
    - is a species
    - has a class
"""
class character:
    def __init__(self):
        self.location = chiania.room().locate("Kingdom Street")
        self.message = ""
    def go(self,dir):
        if dir in self.location.directions:
            new_here=chiania.room().locate(self.location.directions[dir])
            if isinstance(new_here,chiania.room):
                self.location=new_here
                self.message=self.location.message
            else:
                self.message="You cannot go there"
        else:
            self.message="You cannot go '" + dir + "'. Give direction."
    def look(self):
        out=""
        out+= "You are at: " + self.location.name + "\n"
        out+= "You can go:\n"
        for dir in self.location.directions:
            if isinstance(chiania.room().locate(self.location.directions[dir]),chiania.room): 
                out+= dir + ": " + chiania.room().locate(self.location.directions[dir]).name + "\n"
        self.message=out
            

