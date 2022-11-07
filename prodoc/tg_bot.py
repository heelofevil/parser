from prodoc.tg_token import token
import telebot
from telebot import types
from prodoctorov import url_prodoc

bot = telebot.TeleBot(token)
# Список переменных для парсинга
attr_prodoc = []

# Старт бота + кнопки
def telegramm_bot(token):
    @bot.message_handler(commands=['start'])
    def start_bot(message):
        bot.send_message(message.chat.id,
                         "Добро пожаловать! Я бот администратор, я могу найти вам самые хорошие цены на УЗИ! 🏥")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🏦 Москва")
        btn2 = types.KeyboardButton("🏢 Санкт-Петербург")
        btn3 = types.KeyboardButton("🏫 Екатеринбург")
        btn4 = types.KeyboardButton("🏭 Пермь")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, 'Выберите город (Москва, Санкт-Петербург, Екатеринбург, Пермь)',
                         reply_markup=markup)

    # Логика кнопок
    @bot.message_handler(content_types='text')
    def fed(message):
        if message.text in "🏦 Москва 🏢 Санкт-Петербург 🏫 Екатеринбург 🏭 Пермь":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1, item2 = types.KeyboardButton("🔴 УЗИ шеи"), types.KeyboardButton("🟠 УЗИ брюшной полости")
            item3, item4 = types.KeyboardButton("🟡 УЗИ малого таза"), types.KeyboardButton("🟢 УЗИ половой системы")
            item5 = types.KeyboardButton("Назад")
            markup.add(item1, item2, item3, item4, item5)
            bot.send_message(message.chat.id, 'Выбери область узи', reply_markup=markup)

                
        if message.text in "🔴 УЗИ шеи":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1, item2 = types.KeyboardButton("паращитовидных желез"), types.KeyboardButton("щитовидной железы")
            item3 = types.KeyboardButton("Назад")
            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id, 'Выберите вид узи', reply_markup=markup)


        if message.text in "🟠 УЗИ брюшной полости":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1, item2, item3 = types.KeyboardButton("желудка"), types.KeyboardButton("желчного пузыря"), types.KeyboardButton("печени")
            item4, item5 = types.KeyboardButton("почек"), types.KeyboardButton("обзорное всех органов")
            item6 = types.KeyboardButton("Назад")
            markup.add(item1, item2, item3, item4, item5, item6)
            bot.send_message(message.chat.id, 'Выберите вид узи', reply_markup=markup)

        if message.text in "🟡 УЗИ малого таза":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1, item2 = types.KeyboardButton("мочевого пузыря"), types.KeyboardButton("УЗИ определением остаточной мочи")
            item3 = types.KeyboardButton("Назад")
            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id, 'Выберите вид узи', reply_markup=markup)

        if message.text in "🟢 УЗИ половой системы":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1, item2 = types.KeyboardButton("матки и придатков"), types.KeyboardButton("молочных желез")
            item3, item4 = types.KeyboardButton("мошонки"), types.KeyboardButton("предстательной железы")
            item5 = types.KeyboardButton("Назад")
            markup.add(item1, item2, item3, item4, item5)
            bot.send_message(message.chat.id, 'Выберите вид узи', reply_markup=markup)

        # Условия сбора переменных для дальнейшего парсинга
        if message.text in '🏦 Москва паращитовидных желез желудка мочевого пузыря матки и придатков 🔴 УЗИ шеи':
            attr_prodoc.append(1)
        elif message.text in '🏢 Санкт-Петербург щитовидной железы желчного пузыря УЗИ определением остаточной мочи молочных желез 🟠 УЗИ брюшной полости':
            attr_prodoc.append(2)
        elif message.text in '🏫 Екатеринбург печени мошонки 🟡 УЗИ малого таза':
            attr_prodoc.append(3)
        elif message.text in '🏭 Пермь почек предстательной железы 🟢 УЗИ половой системы':
            attr_prodoc.append(4)
        elif message.text in 'обзорное всех органов':
            attr_prodoc.append(5)

        # Условие для отката переменных парсинга
        elif message.text in "Назад":
            start_bot(message)
            attr_prodoc.clear()

        # Условия для вывода информации в тг бот
        if len(attr_prodoc) == 3:
            status = url_prodoc(*attr_prodoc)
            for i, k in status.items():
                bot.send_message(message.chat.id, f'{k[0]} {k[1]} цена {k[2]} \n\n[Cсылка для записи]({k[3]})', parse_mode='Markdown')


    bot.infinity_polling()


if __name__ == '__main__':
    telegramm_bot(token)
