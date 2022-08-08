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

location=col.find_one({"name":"Kingdom Street"})

pprint.pprint(location)