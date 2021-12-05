import telebot, config
from TRANS import to_cyrillic, to_latin

TOKEN = "Sizning_Tokingiz"

bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	javob = "Hush Kelibsiz !!!"
	javob += "\nIstalgan So'z Kiriting >>> "
	bot.reply_to(message, javob)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	msg = message.text
	javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
	bot.reply_to(message, javob(msg))

bot.polling()
