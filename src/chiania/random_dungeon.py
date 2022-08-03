import random
import json
import config.settings
import os
import datetime
from pprint import pprint

"""
  Coordinates
  xy  xy  xy  xy  xy
  00  10  20  30  40
  01  11  21  31  41
  02  12  22  32  42
  03  13  23  33  43
"""

directions={
    "1":{ "name":"north",  "x" : 0, "y" : -1, "opp" : "2"},
    "2":{ "name":"south",  "x" : 0, "y" :  1, "opp" : "1"},
    "3":{ "name":"east" ,  "x" : 1, "y" :  0, "opp" : "4"},
    "4":{ "name":"west" ,  "x" :-1, "y" :  0, "opp" : "3"}
}

def random_dungeon(location,location_file):
    #print("random dungeon. location_file:" + location_file)
    json_path=location_file
    with open(json_path) as file:
        data = json.load(file)
        file.close()
    
    now=datetime.datetime.now()
    datestr=now.strftime("%Y-%m-%d")
    
    if data["settings"]["random_dungeon"]["generate"]=="daily":
        dungeon_out_json=config.settings.dungeon_data_dir + "/random_dungeon/" + data["settings"]["random_dungeon"]["filename"]+ "_" + datestr + ".json"
        dungeon_out_relative= "random_dungeon/" + data["settings"]["random_dungeon"]["filename"]+ "_" + datestr + ".json"
        dungeon_out_html=config.settings.dungeon_data_dir + "/random_dungeon/" + data["settings"]["random_dungeon"]["filename"]+ "_" + datestr + ".html"
    #if we have generated this dungeon already
    if os.path.exists(dungeon_out_json):
        with open(dungeon_out_json) as file:
            dout = json.load(file)
        file.close()
        return dout
        
    #DungeonData
    duda={}
    #DungeonEntryData
    ed=data["locations"][location]
    x=ed["x"]
    y=ed["y"]
    #Create x dict if it doesn't exist'
    if not x in duda: duda[x]={}
    
    #just initialize opposite direction with non direction
    odir=5
    cdir=0
    
    duda[x][y]=ed
    duda[x][y]["name"]=location
    prev_room_name=location
    
    noreturn=data["settings"]["random_dungeon"]["noreturn"]

    for i in range(data["settings"]["random_dungeon"]["steps"]):
        #print("room " + str(i))
        #possible directions
        pdir=[]
        for dir in directions:
            #print("direction: " + directions[dir]["name"])
            ny=y + directions[dir]["y"]
            nx=x + directions[dir]["x"]
            if (ny) in range(data["settings"]["random_dungeon"]["height"]) and ( #not out of y coordinates
                nx) in range(data["settings"]["random_dungeon"]["width"])  and ( #not out of x coordinates
                dir != odir ):# not in opposite direction
                doappend=True
                
                #Check if Room already exists
                if nx in duda:
                    if ny in duda[nx] and len(pdir) > 0 and noreturn <=0: #allow direction if there is no other possible direction (would end in error then)
                        doappend=False #if Room already exists do not go this direction
                    else:
                        noreturn=data["settings"]["random_dungeon"]["noreturn"] #reset noreturn
                if doappend:
                    #more weight for same direction
                    if dir == cdir:
                        for j in range(data["settings"]["random_dungeon"]["samedirection"]):
                            pdir.append(dir) #append multiple times
                    else:
                        pdir.append(dir)
        noreturn-=1
                
        #print("possible directions: " +','.join(pdir))
        #print("possible directions len: " + str(len(pdir)))
        #chosen direction
        cdir=pdir[random.randint(0,len(pdir)-1)]
        #opposite direction
        odir=directions[cdir]["opp"]
        #print("chosen direction: " + str(cdir))
        
        px = x
        py = y
        x = x + directions[cdir]["x"]
        y = y + directions[cdir]["y"]
        
        #corridor from previous room to new room
        duda[px][py][directions[cdir]["name"]]={
            "name" : (data["settings"]["random_dungeon"]["name"] + " " + str(x) + " " + str(y)),
            "type" : "random_dungeon",
            "file" : dungeon_out_relative
        }
        
    
        if not x in duda: duda[x]={}
        
        #If room already exists make an additional direction there
        if y in duda[x]:
            oppDirName=directions[odir]["name"]
            duda[x][y][oppDirName]={
                "name" : duda[px][py]["name"],
                "type" : "random_dungeon",
                "file" : dungeon_out_relative
            }
        else:
            duda[x][y]={
                "x": x,
                "y": y,
                "name" : (data["settings"]["random_dungeon"]["name"] + " " + str(x) + " " + str(y)),
                "description" : (data["settings"]["random_dungeon"]["name"] + " " + str(x) + " " + str(y)),
                directions[odir]["name"] : {
                    "name" : prev_room_name,
                    "type" : "random_dungeon",
                    "file" : dungeon_out_relative
                }
            }
        
        prev_room_name=(data["settings"]["random_dungeon"]["name"] + " " + str(x) + " " + str(y))

        #save number of step for showing in debug render
        if 'stepnr' in duda[x][y]:
            duda[x][y]['stepnr'].append(i)
        else:
            duda[x][y]['stepnr']=[i]
    
    #Dumping and writing File is for testing purposes now
    #want to visually see if dungeon makes sense
    #print(json.dumps(duda,indent=2))
    #Json Data for checking
    outfile=open("output/random_dungeon.duda.json","w")
    outfile.write(json.dumps(duda,indent=2))
    outfile.close()
    
    out=''
    out+="""
    <html>
        <head>
        <title>Random Dungeon</title>
        <style>
            body {
                background: black;
            }
            table {
                border-spacing: 1px;
                /*border-collapse: collapse;*/
            }
            td{
                height:100px;
                width:100px;
            }
            td.block {
                border: 20px solid black;
                background-color: #111111;
                height:100px;
                width:100px;

            }
            td.room {
                border: 20px solid black;
                background-color: #cccccc;
                height:100px;
                width:100px;

            }
            td.north {
                border-top: 20px solid #cccccc;
            }
            td.south {
                border-bottom: 20px solid #cccccc;
            }
            td.east {
                border-right: 20px solid #cccccc;
            }
            td.west {
                border-left: 20px solid #cccccc;
            }
        </style>
    </html>
    """
    
    out+='<table>'
    for y in range(data["settings"]["random_dungeon"]["height"]):
        out+='<tr>'
        for x in range(data["settings"]["random_dungeon"]["width"]):
            if x in duda and y in duda[x]:
                classes=['room']
                for key in duda[x][y]:
                    if key in ["north","south","east","west"]:
                        classes.append(key)
                #cell content
                if 'stepnr' in duda[x][y]:
                    cont=str(duda[x][y]['stepnr'])
                cont+="<br>"
                if 'name' in duda[x][y]:
                    cont+=duda[x][y]['name']
            else:
                classes=['block']
                cont=""
            out+='<td class="' + ' '.join(classes) + '">'
            out+=cont
            out+='</td>'
            
        out+='</tr>'
    out+='</table>'
    
    outfile=open(dungeon_out_html,"w")
    outfile.write(out)
    outfile.close()
    
    #Dictionary to return
    dout={
        "locations": {},
        "settings":{
            "type": "static",
            "continent": data["settings"]["continent"]
        }
    }
    
    for x in duda:
        for y in duda[x]:
            dout['locations'][duda[x][y]['name']] = duda[x][y]
    with open(dungeon_out_json,"w") as file:
        data = file.write(json.dumps(dout,indent=2))
        file.close()
    return dout