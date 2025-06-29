import os
from telethon import TelegramClient

# קבלת משתני סביבה מהמערכת
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")
chat_id = int(os.getenv("CHAT_ID"))

# התחברות לטלגרם כבוט
client = TelegramClient("bot", api_id, api_hash).start(bot_token=bot_token)

async def main():
    await client.send_message(chat_id, "✅ הבוט פועל בהצלחה מ־Render!")

with client:
    client.loop.run_until_complete(main())
