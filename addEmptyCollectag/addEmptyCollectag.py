# Tan Tran
# 6/23/17
# CPSC 362-01

# addEmptyCollectag.py
# This function adds a new 'collectag' (without tags)
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

# Add new collectag (without tags)
db.users.update_one(
    {"username": keyUser},
    {"$push": {
        "collectags": {
            "name": keyCollectag
            }
        }
    }
)

# Print confirmation message
print("Collectag {} added.".format(keyCollectag))
