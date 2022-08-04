import sys
from pprint import pprint
import yaml
import json
import chiania
import inspect
import os

my_here=chiania.room().locate("Kingdom Street")

go_dir=""

#Movement Test
while go_dir != "quit":
    print("You are at: " + my_here.name)
    print("You can go: ")
    for dir in my_here.directions:
        room=chiania.room().locate(my_here.directions[dir])
        if isinstance(room,chiania.room):print(dir + " : " + room.name)
        
    print("write 'quit' to exit")
    go_dir=input("go: ")
    print("----------------------------------")
    if go_dir in my_here.directions:
        new_here=chiania.room().locate(my_here.directions[go_dir])
        print("----------------------------------")
        if isinstance(new_here,chiania.room):
            my_here=new_here
            print(my_here.message)
        else:
            print(new_here)
        print("----------------------------------")
    else:
        print("You cannot go '" + go_dir + "'. Give direction.")
        print("----------------------------------")
