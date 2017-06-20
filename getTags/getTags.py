# Tan Tran
# CPSC 362-01
# 6/19/17

# getTags.py
# This function retrieves all tags from one collectag
# belonging to a given user.

import sys
from pymongo import MongoClient

# Open link to MongoDB client
client = MongoClient()

# Connect to Instagram database
db = client.instagram

"""
# Add new users to "users" collection
db.users.insert_many([
  {
    "username": "shelleypham",
    "collectags":[
      {
        "name": "cute",
        "tags": ["dogs", "cats", "buttons"]
      },
      {
        "name": "foody",
        "tags": ["best", "foode", "ever"]
      }
    ]
  },
  {
    "username": "nullinternet",
    "collectags":[
      {
        "name": "ff_restored_v1.0",
        "tags": ["final_fantasy", "ff", "hack"]
      },
      {
        "name": "breadsticks",
        "tags": ["food", "meme"]
      }
    ]
  }
])
"""

# Get command line args as username name
keyUser = str(sys.argv[1])
keyCollectag = str(sys.argv[2])

# Find user and store its data
foundUser = db.users.find_one({"username": keyUser})

# Get a list of tags from the user's collectags
tagList = []

for i in range(len(foundUser['collectags'])):
  if foundUser['collectags'][i]['name'] == keyCollectag:
    tagList.append(foundUser['collectags'][i]['tags'])

# Print all tags in given user's given collectag
print(tagList)
