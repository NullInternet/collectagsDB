# Tan Tran
# CPSC 362-01
# 6/19/17

# getCollectags.py
# This program gets a username from the user's input,
# then prints the names of that user's collectags.

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

# Get command line args as username and collectag name
keyName = str(sys.argv[1])

# Find user and store its data
foundUser = db.users.find_one({"username": keyName})

# Get a list of tags from the user's collectags
collectagList = []

for i in range(len(foundUser['collectags'])):
  collectagList.append(foundUser['collectags'][i]['name'])

# Print all tags in user's collectags
print(collectagList)
