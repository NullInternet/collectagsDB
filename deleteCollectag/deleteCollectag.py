# Tan Tran
# 6/19/17
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
keyUser = str(sys.argv[1])
keyCollectag = str(sys.argv[2])

# Delete collectag (including its tags)
db.users.update(
    {"$and": [
        {"username": keyUser},
        {"collectags.name": keyCollectag}
    ]},
    {"$pull": {
        "collectags": {
            "$and": [
                {"name": keyCollectag},
                {"tags": {"$exists": True}}
            ]}
        }
    }
)

# Print confirmation message
print("Collectag {} deleted.".format(keyCollectag))
