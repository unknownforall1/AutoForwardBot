# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(lineno)d - %(module)s - %(levelname)s - %(message)s'
)
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

import uvloop
uvloop.install()
from config import Config
from pyrogram import Client 


class channelforward(Client, Config):
    def __init__(self):
        super().__init__(
            name="CHANNELFORWARD",
            session_string=self.session_string,
            api_id=self.API_ID,
            api_hash=self.API_HASH,
            workers=20,
            plugins={'root': 'Plugins'}
        )
class channelforwardbot(Client, Config):
    def __init__(xself):
        super().__init__(
            name="CHANNELFORWARDBOT",
            session_string=xself.session_strings,
            api_id=xself.API_ID,
            api_hash=xself.API_HASH,
            workers=20,
            plugins={'root': 'Plugins'}
        )
        
    async def start(self):
        await super().start()
        me = await self.get_me()
        print(f"New session started for {me.first_name}({me.username})")
    async def start(xself):
        await super().start()
        me = await xself.get_me()
        print(f"New session started for {me.first_name}({me.username})")
    async def stop(self):
        await super().stop()
        print("Session stopped. Bye!!")
    async def stop(xself):
        await super().stop()
        print("Session stopped. Bye!!")

if __name__ == "__main__" :
    channelforward().run()
