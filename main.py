import os, telebot
from datetime import datetime
TOKEN = os.getenv('TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "Hai! Kirim menfes lo disini. Anonim 100%.")
@bot.message_handler(content_types=['text','photo','video','document'])
def handle(m):
    try:
        jam = datetime.now().strftime('%H:%M')
        footer = f"\n\n— {jam}"
        cid = int(CHANNEL_ID)
        if m.content_type == 'text':
            bot.send_message(cid, m.text + footer)
        elif m.content_type == 'photo':
            bot.send_photo(cid, m.photo[-1].file_id, caption=(m.caption or "") + footer)
        elif m.content_type == 'video':
            bot.send_video(cid, m.video.file_id, caption=(m.caption or "") + footer)
        else:
            bot.send_document(cid, m.document.file_id, caption=(m.caption or "") + footer)
        bot.reply_to(m, "✅ Menfes lo udah naik di @arsipneraka!")
    except Exception as e:
        bot.reply_to(m, f"Error: {e}")
print("Bot jalan...")
bot.infinity_polling()
