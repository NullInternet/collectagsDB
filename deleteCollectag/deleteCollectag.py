# Tan Tran
# 6/26/17
# CPSC 362-01

# deleteCollectag.py
# This function deletes a 'collectag' (both its name and its tags)
# from a document in the Instagram database.

import sys
from pymongo import MongoClient

# Open link to MongoDB client
client = MongoClient()

# Connect to Instagram database
db = client.instagram

# Get command line args as username and collectag name
keyUser = str(sys.argv[1])
keyCollectag = str(sys.argv[2])

# Delete collectag (including its tags)
db.users.update(
    {"$and": [
        {"username": keyUser},
        {"collectags.name": keyCollectag}
    ]},
    {"$pull": {
        "collectags": [{
            "$and": [
                {"name": keyCollectag},
                {"tags": {"$exists": True}}
            ]
            }]
        }
    }
)

# Print confirmation message
print("Collectag {} deleted.".format(keyCollectag))
