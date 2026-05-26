import asyncio
import feedparser
from telegram import Bot

TOKEN = "8817301290:AAHjU3WTe2SHdS45mxVUFxCEWs5tVKjE8xI"
CHANNEL_ID = "@kientradeai"

RSS_URL = "https://www.coindesk.com/arc/outboundfeeds/rss/"

async def main():
    bot = Bot(token=TOKEN)

    feed = feedparser.parse(RSS_URL)

    latest = feed.entries[0]

    title = latest.title
    link = latest.link

    message = f"""
🔥 Tin Crypto Mới

📰 {title}

🔗 {link}
"""

    await bot.send_message(
        chat_id=CHANNEL_ID,
        text=message
    )

    print("Đã đăng tin thành công")

asyncio.run(main())