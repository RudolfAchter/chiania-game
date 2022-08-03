import sys
from pprint import pprint
import yaml
import json
import chiania

with open("src/config/settings.yaml", "r") as config:
    try:
        print(yaml.safe_load(config))
        settings=config
    except yaml.YAMLError as exc:
        print(exc)


my_here=chiania.locate("Kingdom Street")
if my_here:
    pprint(vars(my_here))

print("\n\n--------------------------------------\n\n")

my_here=chiania.locate("Tavern")
if my_here:
    pprint(vars(my_here))

print("\n\n--------------------------------------\n\n")

my_here=chiania.locate("Deep Slime Forest")
if my_here:
    pprint(vars(my_here))


print("\n\n--------------------------------------\n\n")

my_loc={
    "name": "entry",
    "file": "deep_slime_forest.random_dungeon.json",
    "type": "random_dungeon"
}

my_here=chiania.locate(my_loc)
if my_here:
    pprint(vars(my_here))

for dir in ["north","south","east","west"]:
    if(hasattr(my_here,dir)):
        if(not getattr(my_here, dir) is None):
            look=chiania.locate(getattr(my_here, dir))
            pprint(vars(look))
            print("\n\n--------------------------------------\n\n")

go_dir=""
if my_here:
    pprint(vars(my_here))
    print("\n\n--------------------------------------\n\n")

#Movement Test
while go_dir != "quit":
    pprint(vars(my_here))
    print("\n\n--------------------------------------\n\n")
    go_dir=input("go: ")
    if go_dir in ["north","south","east","west"]:
        new_here=chiania.locate(getattr(my_here,go_dir))
        if(new_here is None):
            print("you cannot go there\n")
        else:
            my_here=new_here