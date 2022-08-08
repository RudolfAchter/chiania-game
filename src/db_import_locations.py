import pymongo
import dns # required for connecting with SRV
import pprint
import config.secrets
import json

# Your Internet IP must be added to MongoDB Atlas Network Access IPs

myuser=config.secrets.dbuser
mypassword=config.secrets.dbpass

#, server_api=ServerApi('1')
dbclient = pymongo.MongoClient("mongodb+srv://"+myuser+":"+mypassword+"@chia-stuff.g7ivxgh.mongodb.net/?retryWrites=true&w=majority")

#db is "chiania"
db = dbclient.chiania
#collection is locations
col = db.locations

#db and collection are created as needed

location_list = []

#Loading Locations JSON File
with open("src/data/locations.json","r") as file:
    location_data=json.loads(file.read())

#Each Key in Location is one "document"
for key in location_data:
    #Adding Key as "name" in document
    location_data[key]["name"]=key
    #Inserting one document for one location key
    col.insert_one(location_data[key])