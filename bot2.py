import telebot
from telebot import types

API_TOKEN = "8639264991:AAHmOW-M-WrZ67wsnxi0LU04FJg9zBtiZ9k"
bot = telebot.TeleBot(API_TOKEN)

SPONSOR_LINK = "https://www.bet10linesitegiris.com/"

@bot.message_handler(commands=['güncel', 'bet', 'bet10line', 'adres'])
def send_sponsor_link(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("📌 Siteye Git", url=SPONSOR_LINK)
    markup.add(btn)
    bot.send_message(
        message.chat.id,
        f"⚓️ Kupon Kaptanı Resmi Sponsor Linki\n\n"
        f"📌 Sponsor linkimiz: {SPONSOR_LINK}\n\n"
        f"💎 Üye olurken Promosyon kodu **KAPTAN** yazarak 444 TL FREEBET alabilirsiniz!",
        reply_markup=markup
    )

bot.polling()
