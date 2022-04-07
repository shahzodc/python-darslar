from translate import translate
import telebot # pyTelegramBotAPI ning nomi  

TOKEN ="5243750937:AAEICRsqRST7ynZs9dyFJYA8X9knQfUAsLc"
tarjimonbot = telebot.TeleBot(token=TOKEN)

# start komandasi uchun mas'ul funksiya
@tarjimonbot.message_handler(commands=["start"])
def salom(message):
    xabar = "Assalomu alaykum, tarjimon botga xush kelibsiz."
    xabar += "\nMatningizni yuboring."
    tarjimonbot.reply_to(message, xabar)

# matnlar uchun mas'ul funksiya
@tarjimonbot.message_handler(func=lambda msg: msg. text is not None)
def tarjima(message):
    msg = message.text
    tarjimonbot.reply_to(message, translate(msg))
    
# botni ishga tushiramiz
tarjimonbot.polling()






