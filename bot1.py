import telebot
import time

API_TOKEN = "8798011503:AAEfB21cgpzfAhpLFyjHe6U7VejxB1I9v3M"
bot = telebot.TeleBot(API_TOKEN)

def delete_messages(chat_id, start_id, count):
    for i in range(count):
        try:
            bot.delete_message(chat_id, start_id - i)
            time.sleep(0.05)  # Telegram rate limit için küçük bekleme
        except:
            pass

@bot.message_handler(commands=['temizle'])
def clean_100(message):
    delete_messages(message.chat.id, message.message_id, 100)
    bot.send_message(message.chat.id, "✅ 100 mesaj silindi.")

@bot.message_handler(commands=['temizle500'])
def clean_500(message):
    # 500 mesajı 100’erlik bloklarla sil
    for block in range(5):
        delete_messages(message.chat.id, message.message_id - (block*100), 100)
    bot.send_message(message.chat.id, "✅ 500 mesaj silindi.")

@bot.message_handler(commands=['temizle1000'])
def clean_1000(message):
    # 1000 mesajı 100’erlik bloklarla sil
    for block in range(10):
        delete_messages(message.chat.id, message.message_id - (block*100), 100)
    bot.send_message(message.chat.id, "✅ 1000 mesaj silindi.")

bot.polling()
