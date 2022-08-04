import random
import json
import os
from pprint import pprint
import chiania
import config.settings

class room:
    def __init__(self):
        self.location = ""
        self.name = ""
        self.description = ""
        self.monsters = []
        self.directions = {}
        self.message=""
        self.type = "Wild"

    
    def locate(self,location, location_file="world.json"):

        location_file='world.json'
        move_type = "walk"

        if(type(location) is dict):
            if 'name' in location: location_name = location['name']
            if 'file' in location: location_file = location['file']
            if 'move' in location: move_type = location['move']

        else:
            location_name=location
        location_path=config.settings.dungeon_data_dir + "/" + location_file

        data = None
        location_data = None
        
        with open(location_path) as file:
            data = json.load(file)
            file.close()
        
        if(data['settings']['type'])=='static':
            location_data=data
        
        if data['settings']['type'] == "random_dungeon":
            location_data = chiania.random_dungeon(location_name,location_path)

        # Error Handling: Aborts and returns None if no Data was returned
        if location_data is None:
            return None

        if location_name in location_data['locations']:
            #print(data['locations'][location])
            ldat=location_data['locations'][location_name]
            self.name=location_name
            if 'description' in ldat: self.description = ldat['description']
            if 'directions' in ldat: self.directions = ldat['directions']
            self.message = "You " + move_type + " to '"+ location_name + "'"

            if "area_type" in ldat:
                self.type = ldat['area_type']
            if "monsters" in ldat:
                for monster in ldat['monsters']:
                    for i in range(monster['count']):
                        self.monsters.append(monster['name'])
            return self
        else:
            return False