from prodoc.tg_token import token
import requests
import telebot
from telebot import types
bot = telebot.TeleBot(token)
city = {1: 'moskva/', 2: 'spb/', 3: 'ekaterinburg/', 4: 'perm/'}

def telegramm_bot(token):

    @bot.message_handler(commands=['start'])
    def start_bot(message):
        bot.send_message(message.chat.id, "Добро пожаловать! Я бот администратор, я могу найти вам самые хорошие цены на УЗИ! =)")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Москва")
        btn2 = types.KeyboardButton("Санкт-Петербург")
        btn3 = types.KeyboardButton("Екатеринбург")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, 'Выберите город (Москва, Санкт-Петербург, Екатеринбург, Пермь)',
                         reply_markup=markup)

    @bot.message_handler(commands=['button'])
    def button_message(message):
        pass
        #markup.add(types.KeyboardButton("Пермь"))
        # bot.send_message(message.chat.id, 'Выберите город (1-Москва, 2-Санкт-Петербург, 3-Екатеринбург, 4-Пермь): ', reply_markup=markup)

    @bot.message_handler(content_types='text')
    def fed(message):
        if message.text in "Москва":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Gorod")
            markup.add(item1)
            bot.send_message(message.chat.id, 'asdada: ',reply_markup=markup)

    #
    # @bot.message_handler(content_types='text')
    # def select_city(message):
    #     if message.text == "Москва":
    #         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #         item1 = types.KeyboardButton("Gorod")
    #         markup.add(item1)
    #         bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)
    #     elif message.text == "Gorod":
    #         bot.send_message(message.chat.id, 'Спасибо за прочтение статьи!')


    bot.polling()

if __name__ == '__main__':
    telegramm_bot(token)
