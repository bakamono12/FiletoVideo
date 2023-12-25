import os

# this file is provided for the configuration of the Environment variables
# this variable will be used to generate the session string
# this variable will be used to allow bot to work in the group or chat


session_string = os.environ.get("SESSION_STRING", None)
allowed_group = os.environ.get("ALLOWED_GROUP", None)
owner = os.environ.get("OWNER", None)
