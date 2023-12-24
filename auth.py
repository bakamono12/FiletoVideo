import pyrogram
import os
from time import sleep

# set the environment variables

api_id = os.environ.get("API_ID", None)
api_hash = os.environ.get("API_HASH", None)
bot_token = os.environ.get("BOT_TOKEN", None)

# create a pyrogram session
app = pyrogram.Client("File-To-Video", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# start the pyrogram app
app.start()
print(app.export_session_string())
app.stop()

# This file is provided for the convenience of the user
# if you are not comfortable with the session string generation
# on replit you can use this file to generate the session string
# and then copy it to the environment variable
# this code is provided by github.com/bakamono12
