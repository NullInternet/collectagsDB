# Tan Tran
# 6/26/17
# CPSC 362-02

# addTags.py
# This program adds a list of user-generated tags
# to an existing collectag under an existing user.

import sys
from pymongo import MongoClient

# Open link to MongoDB client
client = MongoClient()

# Connect to Instagram database
db = client.instagram

# Get command line args as username name
keyUser = str(sys.argv[1])
keyCollectag = str(sys.argv[2])

# Get remaining command line args as tags to add
keyTags = []

sysArgID = 3
for sysArgID in len(sys.argv)
    keyTags.append(sys.argv[sysArgID])

# Add new tags to collectag
db.users.update(
    {"$and": [
        {"username": keyUser},
        {"collectags.name": keyCollectag}
    ]},
    {"$push": {
        "collectags": [{
            "tags": {"$each": keyTags}
            }]
        }
    }
)

# Print confirmation message
print("Added the following tags to collectag {}:".format(keyCollectag))
print("{}".format(keyTags))
