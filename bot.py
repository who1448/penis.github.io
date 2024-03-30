import telebot
from telebot import types
bot = telebot.TeleBot('6858482368:AAFDjQ5eCYbrlnietdvAD4xXawi6SmrXlwU')
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_photo(message.chat.id, r'https://disk.yandex.ru/i/oCqS79cIYtLaZg')
#    photo_id = message.photo.file_id
#    print(f"ID фотографии: {photo_id}")
#@bot.message_handler(commands=['start'])
#def start(message):
#    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#    btn1 = types.KeyboardButton('Фото')
#    btn2 = types.KeyboardButton('Текст')
#    markup.add(btn1,btn2)
#    bot.send_message(message.chat.id,'Привет, я бот который может показать тебе расписание уроков на все дни недели.\n\nВыбирай, в каком формате тебе нужно расписание?',reply_markup=markup)
@bot.message_handler()
def format(message):
    if message.text == 'Фото':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Понедельник.png')
        btn2 = types.KeyboardButton('Вторник.png')
        btn3 = types.KeyboardButton('Среда.png')
        btn4 = types.KeyboardButton('Четверг.png')
        btn5 = types.KeyboardButton('Пятница.png')
        markup.add(btn1,btn2,btn3,btn4,btn5)
        bot.send_message(message.chat.id, 'Твой формат - "Фото"\nТеперь определимся на какой день недели тебе нужно расписание?', reply_markup=markup)
    elif message.text == 'Текст':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Понедельник.txt')
        btn2 = types.KeyboardButton('Вторник.txt')
        btn3 = types.KeyboardButton('Среда.txt')
        btn4 = types.KeyboardButton('Четверг.txt')
        btn5 = types.KeyboardButton('Пятница.txt')
        markup.add(btn1,btn2,btn3,btn4,btn5)
        bot.send_message(message.chat.id, 'Твой формат - "Текст"\nТеперь определимся на какой день недели тебе нужно расписание?', reply_markup=markup)
    elif message.text == 'Понедельник.txt':
        bot.send_message(message.chat.id, 'Вот твое расписание:\nРусский язык 8\nБиология 6\nИнформатика 2 \nИстория 9\nФизическая культура\nЛитература 8 \nНемецкий язык 1 ')
    elif message.text == 'Вторник.txt':
        bot.send_message(message.chat.id, 'Вот твое расписание:\nФизика 8\nФизика 8\nАлгебра 2\nГеометрия 2\nИстория 9 \nФизизическая культура\nНемецкий язык 1')
    elif message.text == 'Среда.txt':
        bot.send_message(message.chat.id, 'Вот твое расписание:\nРусский язык 8\nХимия 6\nАлгебра 2\nГеометрия 2\nОБЖ 6\nЛитература 8\nОбществознание 9')
    elif message.text == 'Четверг.txt':
        bot.send_message(message.chat.id, 'Вот твое расписание:\nГеография 4 \nЛитература 8 \nАлгебра 2 \nТВИС 2\nБиология 6\nРусский язык 8 \nРРЯ/РЛ 8')
    elif message.text == 'Пятница.txt':
        bot.send_message(message.chat.id, 'Вот твое расписание:\nНемецкий язык 1 \nГеография 4 \nФизическая культура \nХимия 6\nФизика 8\nМоя Россия - Мои горизонты\nПодросток и закон 9')
    elif message.text == 'Понедельник.png':
        photo = open('https://disk.yandex.ru/i/oCqS79cIYtLaZg')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,'Вот твое расписание:')
    elif message.text == 'Вторник.png':
        bot.send_message(message.chat.id, 'Вот твое расписание:')
    elif message.text == 'Среда.png':
        bot.send_message(message.chat.id, 'Вот твое расписание:')
    elif message.text == 'Четверг.png':
        bot.send_message(message.chat.id, 'Вот твое расписание:')
    elif message.text == 'Пятница.png':
        bot.send_message(message.chat.id, 'Вот твое расписание:\n')
bot.polling(none_stop=True)
