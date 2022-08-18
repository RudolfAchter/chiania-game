import pymongo
from pprint import pprint
import config.secrets
import json

# I use chia-dev-tools for encoding and decoding puzzle hashes
# https://github.com/Chia-Network/chia-dev-tools
from chia.util.bech32m import decode_puzzle_hash, encode_puzzle_hash

# Your Internet IP must be added to MongoDB Atlas Network Access IPs

myuser=config.secrets.dbuser
mypassword=config.secrets.dbpass

dbclient = pymongo.MongoClient("mongodb+srv://"+myuser+":"+mypassword+"@chia-stuff.g7ivxgh.mongodb.net/?retryWrites=true&w=majority")

db = dbclient.chiania
col = db.items

#"0x3cf536f516dadd52dcead0eb4e3d80501d3936a61d9bb6ab76507c5d41b10b42"
decoded_did=decode_puzzle_hash("did:chia:18n6ndagkmtw49h826r45u0vq2qwnjd4xrkdmd2mk2p796sd3pdpqtj4h86")
search_did='0x' + decoded_did.hex()

print(search_did)

items=col.find({"owner_did": search_did})

for dat in items:
    pprint(dat,indent=2)
