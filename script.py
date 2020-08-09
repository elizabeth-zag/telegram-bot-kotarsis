import requests
import telebot
import os
from flask import Flask, request

token = '1165655525:AAEQVHu34L1tqYfSSySSSNgBDQ5833hi7Ck'
bot = telebot.TeleBot(token=token)
server = Flask(__name__)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Какой ты сегодня котик?")


@bot.message_handler(regexp='хлеб')
def sad_cat(message):
    photo = open('img/bred.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)


# SERVER SIDE

@server.route('/' + token, methods=['POST'])
def getMessage():
   bot.process_new_updates(
       [telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
   return "!", 200


@server.route("/")
def webhook():
   bot.remove_webhook()
   bot.set_webhook(url='<HEROKU Web URL>' + token)
   return "!", 200


if __name__ == "__main__":
   server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))


# bot.polling()
