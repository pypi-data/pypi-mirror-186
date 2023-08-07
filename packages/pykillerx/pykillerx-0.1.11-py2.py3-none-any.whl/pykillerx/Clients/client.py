from pyrogram import Client

from ..config import Var as Variable

Var = Variable()

'''
try:
    import pytgcalls
except ImportError:
    print("'pytgcalls' not found")
    pytgcalls = None
'''


app = (
    Client(
        name="app",
        api_id=Var.API_ID,
        api_hash=Var.API_HASH,
        bot_token=Var.BOT_TOKEN,
    )
)

# For Publik Repository
DARK1 = (
    Client(
        name="DARK1",
        api_id=Var.API_ID,
        api_hash=Var.API_HASH,
        session_string=Var.STRING1,
        in_memory=True,
    )
    if Var.STRING1
    else None
)


DARK2 = (
    Client(
        name="DARK2",
        api_id=Var.API_ID,
        api_hash=Var.API_HASH,
        session_string=Var.STRING2,
        in_memory=True,
    )
    if Var.STRING2
    else None
)
        
DARK3 = (
    Client(
        name="DARK3",
        api_id=Var.API_ID,
        api_hash=Var.API_HASH,
        session_string=Var.STRING3,
        in_memory=True,
    )
    if Var.STRING3
    else None
)

DARK4 = (
    Client(
        name="DARK4",
        api_id=Var.API_ID,
        api_hash=Var.API_HASH,
        session_string=Var.STRING4,
        in_memory=True,
    )
    if Var.STRING4
    else None
)

DARK5 = (
    Client(
        name="DARK5",
        api_id=Var.API_ID,
        api_hash=Var.API_HASH,
        session_string=Var.STRING5,
        in_memory=True,
    )
    if Var.STRING5
    else None
)

DARK6 = (
    Client(
        name="DARK6",
        api_id=Var.API_ID,
        api_hash=Var.API_HASH,
        session_string=Var.STRING6,
        in_memory=True,
    )
    if Var.STRING6
    else None
)


DARK7 = (
    Client(
        name="DARK7",
        api_id=Var.API_ID,
        api_hash=Var.API_HASH,
        session_string=Var.STRING7,
        in_memory=True,
    )
    if Var.STRING7
    else None
)
        
DARK8 = (
    Client(
        name="DARK8",
        api_id=Var.API_ID,
        api_hash=Var.API_HASH,
        session_string=Var.STRING8,
        in_memory=True,
    )
    if Var.STRING8
    else None
)


DARK9 = (
    Client(
        name="DARK9",
        api_id=Var.API_ID,
        api_hash=Var.API_HASH,
        session_string=Var.STRING9,
        in_memory=True,
    )
    if Var.STRING9
    else None
)
DARK10 = (
    Client(
        name="DARK10",
        api_id=Var.API_ID,
        api_hash=Var.API_HASH,
        session_string=Var.STRING10,
        in_memory=True,
    )
    if Var.STRING10
    else None
)


client = [
    client for client in [
        DARK1, 
        DARK2, 
        DARK3, 
        DARK4, 
        DARK5, 
        DARK6, 
        DARK7, 
        DARK8,
        DARK9,
        DARK10,
    ] if client
]

'''
if pytgcalls is not None:
    for client in clients:
        if not hasattr(bot, "group_call"):
            try:
                setattr(bot, "group_call", pytgcalls.GroupCallFactory(bot).get_group_call())
            except AttributeError:
                pass
'''
