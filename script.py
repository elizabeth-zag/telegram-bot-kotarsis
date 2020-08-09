import requests
import telebot
import os
import random
from flask import Flask, request

token = '1165655525:AAEQVHu34L1tqYfSSySSSNgBDQ5833hi7Ck'
bot = telebot.TeleBot(token=token)
server = Flask(__name__)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(
        resize_keyboard=True, row_width=5, one_time_keyboard=True)

    itembtn1 = telebot.types.KeyboardButton('😺 Радостный')
    itembtn2 = telebot.types.KeyboardButton('😿 Грустный')
    itembtn3 = telebot.types.KeyboardButton('😼 Шальной')
    itembtn4 = telebot.types.KeyboardButton('🍞 Хлебушек')
    itembtn5 = telebot.types.KeyboardButton('🐕‍🦺 Не котик')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5)
    bot.send_message(message.chat.id, "Привет! Какой ты сегодня котик?",
                     reply_markup=markup)


@bot.message_handler(regexp='Радостный')
def happy(message):
    markup = telebot.types.ReplyKeyboardMarkup(
        resize_keyboard=True, row_width=5, one_time_keyboard=True)

    itembtn1 = telebot.types.KeyboardButton('🥳 Счастливый')
    itembtn2 = telebot.types.KeyboardButton('😴 Спящий')
    itembtn3 = telebot.types.KeyboardButton('🍩 Наевшийся')
    itembtn4 = telebot.types.KeyboardButton('🌺 Вознагражденный')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    bot.send_message(message.chat.id, "?",
                     reply_markup=markup)


@ bot.message_handler(regexp='Грустный')
def sad(message):
    markup = telebot.types.ReplyKeyboardMarkup(
        resize_keyboard=True, row_width=5, one_time_keyboard=True)

    itembtn1 = telebot.types.KeyboardButton('😾 Обиженный')
    itembtn2 = telebot.types.KeyboardButton('🙀 Подавленный')
    itembtn3 = telebot.types.KeyboardButton('😿 Расстроенный')
    itembtn4 = telebot.types.KeyboardButton('👎 Тоскливый')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    bot.send_message(message.chat.id, "?",
                     reply_markup=markup)


@ bot.message_handler(regexp='Шальной')
def crazy(message):
    markup = telebot.types.ReplyKeyboardMarkup(
        resize_keyboard=True, row_width=5, one_time_keyboard=True)

    itembtn1 = telebot.types.KeyboardButton('☝ Боец')
    itembtn2 = telebot.types.KeyboardButton('🐒 Игривый')
    itembtn3 = telebot.types.KeyboardButton('💊 Готовый к новым открытиям')
    itembtn4 = telebot.types.KeyboardButton('🏹 Охотник')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    bot.send_message(message.chat.id, "?",
                     reply_markup=markup)


@bot.message_handler(regexp='Счастливый')
def happy_cat(message):
    photo = open('img/счастливый кот.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(regexp='Спящий')
def sleepy_cat(message):
    photo = open('img/спящий кот.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(regexp='Боец')
def fighter_cat(message):
    photo = open('img/воинственный кот.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(regexp='Игривый')
def playful_cat(message):
    photo = open('img/игривый кот.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(regexp='Наевшийся')
def full_cat(message):
    photo = open('img/наевшийся кот.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(regexp='Вознагражденный')
def gifted_cat(message):
    photo = open('img/вознагражденный кот.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(regexp='Готовый к новым открытиям')
def foxy_cat(message):
    photo = open('img/кот готовый к новым открытиям.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(regexp='Охотник')
def hunter_cat(message):
    photo = open('img/кот охотник.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(regexp='Обиженный')
def offended_cat(message):
    photo = open('img/обиженный кот.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(regexp='Подавленный')
def depressed_cat(message):
    photo = open('img/подавленный кот.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(regexp='Расстроенный')
def upset_cat(message):
    photo = open('img/кот с паршивым настроеним.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(regexp='Тоскливый')
def gloomy_cat(message):
    photo = open('img/тоскливый кот.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(regexp='Хлебушек')
def bread_cat(message):
    photo = open('img/хлебушек.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(regexp='Не котик')
def not_cat(message):
    photo = [open('img/ты вовсе не кот.jpg', 'rb'),
             open('img/ты вовсе не кот 2.jpg', 'rb')]
    bot.send_photo(message.chat.id, random.choice(photo))


# SERVER SIDE

@server.route('/' + token, methods=['POST'])
def getMessage():
    bot.process_new_updates(
        [telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(
        url='https://fathomless-citadel-10711.herokuapp.com/' + token)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
