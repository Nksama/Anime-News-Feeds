import os

host = os.environ.get("DB_URL") # get it from redislabs.com
port = os.environ.get("PORT") #numbers after : in the db url

password = os.environ.get("DB_PASSOWORD")
api_id = os.environ.get("API_ID")
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
chat = os.environ.get("CHAT")