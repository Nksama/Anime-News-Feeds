from os import link
import time
from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
import redis
from feedparser import parse
import config
from pyrogram import Client , filters


bot = Client(
    "news",
    api_id=config.api_id,
    api_hash=config.api_hash,
    bot_token=config.bot_token
)

r = redis.Redis(
    host=config.host,
    port=config.port,
    password=config.password,
    decode_responses=True
)


async def getnews():
    async with bot:
        while True:
            feeds = parse(
            "https://www.animenewsnetwork.com/all/atom.xml?ann-edition=us"
            )
            link_ = feeds.entries[0]['link']
            summary = feeds.entries[0]['summary']

            feedx = feeds.entries[0].title_detail
            prev = r.get("LATEST") or ""        
            
            if link_ != prev:
                await bot.send_message(config.chat , f"**{feedx.value}**\n\n{summary}" , 
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("More Info" , url=link_)],
                    ]

                ))

                r.set("LATEST" , link_)
                time.sleep(300)

bot.run(getnews())
