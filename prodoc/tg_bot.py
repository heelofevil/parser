from prodoc.tg_token import token
import telebot
from telebot import types
from prodoctorov import parsing_prodoc

bot = telebot.TeleBot(token)
cult = []


def telegramm_bot(token):
    @bot.message_handler(commands=['start'])
    def start_bot(message):
        bot.send_message(message.chat.id,
                         "Добро пожаловать! Я бот администратор, я могу найти вам самые хорошие цены на УЗИ! =)")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Москва")
        btn2 = types.KeyboardButton("Санкт-Петербург")
        btn3 = types.KeyboardButton("Екатеринбург")
        btn4 = types.KeyboardButton("Пермь")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, 'Выберите город (Москва, Санкт-Петербург, Екатеринбург, Пермь)',
                         reply_markup=markup)


    @bot.message_handler(content_types='text')
    def fed(message):
        if message.text in "МоскваСанкт-ПетербургЕкатеринбург":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1, item2 = types.KeyboardButton("УЗИ шеи"),types.KeyboardButton("УЗИ брюшной полости")
            item3, item4 = types.KeyboardButton("УЗИ малого таза"),types.KeyboardButton("УЗИ половой системы")
            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, 'Выбери область узи', reply_markup=markup)

                
        if message.text in "УЗИ шеи":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1, item2 = types.KeyboardButton("паращитовидных желез"), types.KeyboardButton("щитовидной железы")
            markup.add(item1, item2)
            bot.send_message(message.chat.id, 'Выберите вид узи', reply_markup=markup)


        if message.text in "УЗИ брюшной полости":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1, item2, item3 = types.KeyboardButton("желудка"), types.KeyboardButton("желчного пузыря"), types.KeyboardButton("печени")
            item4, item5 = types.KeyboardButton("почек"), types.KeyboardButton("обзорное всех органов")
            markup.add(item1, item2, item3, item4, item5)
            bot.send_message(message.chat.id, 'Выберите вид узи', reply_markup=markup)

        if message.text in "УЗИ малого таза":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1, item2 = types.KeyboardButton("мочевого пузыря"), types.KeyboardButton("УЗИ м.п. с определением остаточной мочи")
            markup.add(item1, item2)
            bot.send_message(message.chat.id, 'Выберите вид узи', reply_markup=markup)

        if message.text in "УЗИ половой системы":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1, item2 = types.KeyboardButton("матки и придатков"), types.KeyboardButton("молочных желез")
            item3, item4 = types.KeyboardButton("мошонки"), types.KeyboardButton("предстательной железы")
            markup.add(item1, item2,item3, item4)
            bot.send_message(message.chat.id, 'Выберите вид узи', reply_markup=markup)


        if message.text in 'Москва паращитовидных желез желудка мочевого пузыря матки и придатков УЗИ шеи':
            cult.append(1)
        elif message.text in 'Санкт-Петербург щитовидной железы желчного пузыря УЗИ м.п. с определением остаточной мочи молочных желез УЗИ брюшной полости':
            cult.append(2)
        elif message.text in 'Екатеринбург печени мошонки УЗИ малого таза':
            cult.append(3)
        elif message.text in 'Пермь почек предстательной железы УЗИ половой системы':
            cult.append(4)
        elif message.text in 'обзорное всех органов':
            cult.append(5)
        if len(cult) == 3:
            status = parsing_prodoc(*cult)
            for i, k in status.items():
                bot.send_message(message.chat.id, f'Учреждение: {k[0]} {k[1]} цена {k[2]} \n[Cсылка для записи]({k[3]})', parse_mode='Markdown')






    bot.infinity_polling()


if __name__ == '__main__':
    telegramm_bot(token)
