import requests
import datetime
import telebot
from telebot import types
from bs4 import BeautifulSoup as BS

bot = telebot.TeleBot('5900928383:AAGpmKuaeOdgWLQwuWXVgRclwDjZNAIRthg')

@bot.message_handler(commands=['start'])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button1 = types.KeyboardButton("Расписание на предыдущий учебный день")
    button2 = types.KeyboardButton("Расписание на текущий учебный день")
    button3 = types.KeyboardButton("Расписание на следующий учебный день")
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, 'Жду 50 рублей на тинькофф 89772951844', reply_markup=markup)

@bot.message_handler(content_types='text')
def timetableTomorrow(message):
    if message.text=="Расписание на следующий учебный день":
        now = datetime.datetime.now()

        for i in range(1, 6):
            if now.isoweekday() == i:
                s = i + 1
                if i == 5:
                    s = 1
                r = requests.get("https://www.tspk-mo.ru/student/timetable/1/" + str(s))
                html = BS(r.content, "html.parser")

        item = html.select(".slider-item__image > img")
        urlArr = []
        for i in range(3):
            url = "https://www.tspk-mo.ru/" + item[i].attrs["src"]
            urlArr.append(url) 
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(urlArr[0]), telebot.types.InputMediaPhoto(urlArr[1]), telebot.types.InputMediaPhoto(urlArr[2])])
    
    if message.text=="Расписание на текущий учебный день":

        now = datetime.datetime.now()

        for i in range(1, 6):
            if now.isoweekday() == i:
                r = requests.get("https://www.tspk-mo.ru/student/timetable/1/" + str(i))
                html = BS(r.content, "html.parser")

        item = html.select(".slider-item__image > img")
        urlArr = []
        for i in range(3):
            url = "https://www.tspk-mo.ru/" + item[i].attrs["src"]
            urlArr.append(url) 
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(urlArr[0]), telebot.types.InputMediaPhoto(urlArr[1]), telebot.types.InputMediaPhoto(urlArr[2])])
    if message.text=="Расписание на предыдущий учебный день":
        now = datetime.datetime.now()

        for i in range(1, 6):
            if now.isoweekday() == i:
                s = i - 1
                if i == 1:
                    s = 5
                r = requests.get("https://www.tspk-mo.ru/student/timetable/1/" + str(s))
                html = BS(r.content, "html.parser")

        item = html.select(".slider-item__image > img")
        urlArr = []
        for i in range(3):
            url = "https://www.tspk-mo.ru/" + item[i].attrs["src"]
            urlArr.append(url) 
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(urlArr[0]), telebot.types.InputMediaPhoto(urlArr[1]), telebot.types.InputMediaPhoto(urlArr[2])])


bot.infinity_polling()