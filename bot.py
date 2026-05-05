import telebot
import re
from datetime import datetime, timedelta

API_TOKEN = "8798011503:AAEfB21cgpzfAhpLFyjHe6U7VejxB1I9v3M"
bot = telebot.TeleBot(API_TOKEN)
bot.remove_webhook()

# --- Özel mesaj komutları ---
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Merhaba Özgür! Kupon Kaptanı botu çalışıyor.")

@bot.message_handler(commands=['kupon'])
def send_coupon(message):
    bot.reply_to(message, "📋 Bugünün kuponu hazır!")

# --- Kanal kontrol sistemi ---
LIGHT_BAD_WORDS = ["salak", "aptal", "mal", "şapşal"]
HEAVY_BAD_WORDS = ["orospu","piç","sürtük","fuck","shit","bitch","asshole","motherfucker","cunt"]
LINK_PATTERN = re.compile(r"(https?://\S+|www\.\S+)")
warnings = {}

@bot.message_handler(func=lambda message: True)
def monitor_chat(message):
    text = message.text.lower()
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    if any(word in text for word in HEAVY_BAD_WORDS):
        handle_violation(message, user_id, user_name, "ağır küfür")
        return
    if LINK_PATTERN.search(text):
        handle_violation(message, user_id, user_name, "link")
        return
    if any(word in text for word in LIGHT_BAD_WORDS):
        bot.send_message(message.chat.id, f"ℹ️ {user_name}, lütfen daha nazik olalım.")

def handle_violation(message, user_id, user_name, violation_type):
    try:
        bot.delete_message(message.chat.id, message.message_id)
    except:
        pass
    warnings[user_id] = warnings.get(user_id, 0) + 1
    count = warnings[user_id]
    if count < 3:
        bot.send_message(message.chat.id, f"⚠️ {user_name}, {violation_type} yasak! ({count}/3)")
    else:
        bot.send_message(message.chat.id, f"🚫 {user_name}, 3 uyarı aldın! 6 saat mute.")
        until_date = datetime.now() + timedelta(hours=6)
        permissions = telebot.types.ChatPermissions(can_send_messages=False)
        bot.restrict_chat_member(message.chat.id, user_id, permissions=permissions, until_date=until_date)

# --- Botu çalıştır ---
bot.polling()
