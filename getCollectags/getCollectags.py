# Tan Tran
# CPSC 362-01
# 6/26/17

# getCollectags.py
# This program gets a username from the user's input,
# then prints the names of that user's collectags.

import sys
from pymongo import MongoClient

# Open link to MongoDB client
client = MongoClient()

# Connect to Instagram database
db = client.instagram

# Get command line args as username and collectag name
keyUser = str(sys.argv[1])

# Find user and store their collectag names
foundCollectags = db.users.find_one({"username": keyUser},
  {"_id": 0, "username": 0, "collectags.tags": 0}
)

# Print all tags in user's collectags
print(foundCollectags)
