# Tan Tran
# CPSC 362-01
# 6/26/17

# getTags.py
# This function retrieves all tags from one collectag
# belonging to a given user.

import sys
from pymongo import MongoClient

# Open link to MongoDB client
client = MongoClient()

# Connect to Instagram database
db = client.instagram

# Get command line args as username name
keyUser = str(sys.argv[1])
keyCollectag = str(sys.argv[2])

# Find user and store its data
foundTags = db.users.find_one(
    {"$and": [
        {"username": keyUser},
        {"collectags.name": keyCollectag}
    ]},
    {"_id": 0, "username": 0, "collectags.name": 0}
)

# Print all tags in given user's given collectag
print(foundTags)
