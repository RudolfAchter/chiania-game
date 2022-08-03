import random
import json
import os.path
from pprint import pprint
import chiania
import config.settings

class room:
    def __init__(self, location):
        self.location = location
        self.description = ""
        self.monsters = []
        self.east = None
        self.west = None
        self.south = None
        self.north = None
        self.area_type = "Wild"

def locate(location):

    here=None

    location_type="static"
    location_file='locations.viridis.world.json'

    if(type(location) is dict):
        if 'name' in location: location_name = location['name']
        if 'type' in location: location_type = location['type']
        if 'file' in location: location_file = location['file']
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


    # Error Handling: Aborts and returns False if no Data was returned
    if location_data is None:
        return None

    if location_name in location_data['locations']:
        #print(data['locations'][location])
        ldat=location_data['locations'][location_name]
        here = room(location_name)
        here.description = ldat['description']
        #TODO should be able to write this shorter. iterate through all simple strings ['east','north','area_type'] and so on
        if "east" in ldat:
            here.east = ldat['east']
        if "north" in ldat:
            here.north = ldat['north']
        if "south" in ldat:
            here.south = ldat['south']
        if "west" in ldat:
            here.west = ldat['west']
        if "area_type" in ldat:
            here.area_type = ldat['area_type']
        if "monsters" in ldat:
            for monster in ldat['monsters']:
                for i in range(monster['count']):
                    here.monsters.append(monster['name'])
    return here

        
        

    
