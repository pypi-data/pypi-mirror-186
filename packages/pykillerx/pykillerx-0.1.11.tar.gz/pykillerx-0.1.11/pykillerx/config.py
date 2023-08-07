import sys

from os import getenv

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

def getConfig(name: str):
    try:
        return environ[name]
    except:
        return ""


class Var(object):
    # mandatory
    API_ID = int(getenv("API_ID", 0))
    API_HASH = str(getenv("API_HASH"))
    BOT_TOKEN = str(getenv("BOT_TOKEN"))
    # Extras
    ALIVE_PIC = getenv("ALIVE_PIC", "")
    ALIVE_TEXT = getenv("ALIVE_TEXT", "Dark Userbot")
    DB_URL = getenv("DATABASE_URL", "postgresql://postgres:cXnFDqamxUeuACQZ2glC@containers-us-west-143.railway.app:7582/railway")
    
    # chatbot api
    OPENAI_API = getConfig("OPENAI_API")

    # onwer sudo // group log 
    OWNER_ID = int(getenv("OWNER_ID", 5505822896))
    LOG_CHAT = int(getenv("LOG_CHAT") or 0)

    # version branch 
    BOT_VER = "0.3.0@dev"
    BRANCH = getenv("BRANCH", "hacker")

    # pyrogram session
    STRING1 = getenv("STRING1", "")
    STRING2 = getenv("STRING2", "")
    STRING3 = getenv("STRING3", "")
    STRING4 = getenv("STRING4", "")
    STRING5 = getenv("STRING5", "")
    STRING6 = getenv("STRING6", "")
    STRING7 = getenv("STRING7", "")
    STRING8 = getenv("STRING8", "")
    STRING9 = getenv("STRING9", "")
    STRING10 = getenv("STRING10", "")
