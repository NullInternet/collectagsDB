# Tan Tran
# 6/26/17
# CPSC 362-01

# addCollectag.py
# This function adds a new 'collectag' (with tags)
# under an existing user in the Instagram database.

import sys
from pymongo import MongoClient

# Open link to MongoDB client
client = MongoClient()

# Connect to Instagram database
db = client.instagram

# Get command line args as username and collectag name
keyUser = str(sys.argv[1])
keyCollectag = str(sys.argv[2])

# Get remaining command line args as tags to add
keyTags = []

sysArgID = 3
for sysArgID in len(sys.argv):
    keyTags.append(str(sys.argv[sysArgID]))

# Add new collectag (including its tags)
db.users.update_one(
    {"username": keyUser},
    {"$push": {
        "collectags": [{
            "name": keyCollectag,
            "tags": {"$each": keyTags}
            }]
        }
    }
)

# Print confirmation message
print("Collectag {} added with the following tags:".format(keyCollectag))
print("{}".format(keyTags))
