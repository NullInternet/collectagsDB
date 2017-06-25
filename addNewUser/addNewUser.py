# Tan Tran
# CPSC 362-01
# 6/25/17

# addNewUser.py
# This function creates a new user (w/o collectags)
# to the Instagram database.

import sys
from pymongo import MongoClient

# Open link to MongoDB client
client = MongoClient()

# Connect to Instagram database
db = client.instagram

# Get command line args as username name
keyUser = str(sys.argv[1])

# Add new user to "users" collection
db.users.insert_one(
  {
    "username": keyUser,
    "collectags": [ ]
  }
)

# Print confirmation message
print("User {} created.".format(keyUser))
