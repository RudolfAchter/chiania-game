import pymongo
import dns # required for connecting with SRV
import pprint

myuser="rudi"
mypassword="mypass"

#, server_api=ServerApi('1')
myclient = pymongo.MongoClient("mongodb+srv://"+myuser+":"+mypassword+"@chia-stuff.g7ivxgh.mongodb.net/?retryWrites=true&w=majority")
db = myclient.test
print(db)

mydb = myclient.mydatabase
mycol = mydb.customers
mydict = { "name": "Herbert", "address": "Trafalgar Square" }
result = mycol.insert_one(mydict)

doc=mycol.find_one({"name": "John"})

pprint.pprint(doc)