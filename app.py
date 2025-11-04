import os
import telebot

# قراءة التوكن من المتغيرات البيئية
BOT_TOKEN = os.getenv("8254396920:AAFYyl0qySTlZ1XhQDcXpi6msK2Pt03pbz0")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👋 أهلاً! البوت شغال تمام على Render 🚀")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, f"قلت: {message.text}")

print("✅ البوت بدأ العمل...")
bot.polling(non_stop=True)
