import telebot
import sqlite3
from telebot import types # Импорт библиотек

bot = telebot.TeleBot('*********************************************') # Подлючение токена бота

conn = sqlite3.connect('school.db', check_same_thread=False) # Подлючение базы данных "school.db"
cursor = conn.cursor() # Создание курсора для взаимодействия с базой данных
 

@bot.message_handler(commands=["start"]) # Функция, обрабатывающая команду /start
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(row_width=1) # Создание "Reply" кнопок
    itembtn1 = types.KeyboardButton('Посмотреть оценки')
    itembtn4 = types.KeyboardButton('/help')
    markup.add(itembtn1, itembtn4)
    bot.send_message(m.chat.id, 'Привет! \nЯ - Бот, помогающий системе контроля знаний школьников работать удобнее и быстрее! \nНапиши - /help чтобы узнать что я умею!', reply_markup=markup)

@bot.message_handler(commands=["help"]) # Функция, обрабатывающая команду /help
def help(m, res=False):
    bot.send_message(m.chat.id,'/start - начало работы\n/help - получение списка команд\nЧтобы посмотреть оценки школьников, выберите пункт "Посмотреть оценки", затем выберите нужный класс и я пришлю вам оценки!' )


@bot.message_handler(content_types=["text"]) # Функция, обрабатывающая текстовые сообщения
def handle_marks(message):
    if(message.text == 'Посмотреть оценки'):
        markup = types.ReplyKeyboardRemove(selective=True) # Удаление предыдущих "Reply" кнопок
        markup = types.ReplyKeyboardMarkup(row_width=1) # Создание новых "Reply" кнопок
        btn1 = types.KeyboardButton('1 класс')
        btn2 = types.KeyboardButton('2 класс')
        btn3 = types.KeyboardButton('3 класс')
        btn4 = types.KeyboardButton('4 класс')
        btn5 = types.KeyboardButton('5 класс')
        btn6 = types.KeyboardButton('6 класс')
        btn7 = types.KeyboardButton('7 класс')
        btn8 = types.KeyboardButton('8 класс')
        btn9 = types.KeyboardButton('9 класс')
        btn10 = types.KeyboardButton('10 класс')
        btn11 = types.KeyboardButton('11 класс')
        btn12 = types.KeyboardButton('назад')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12)
        bot.send_message(message.chat.id, 'Выберите класс!', reply_markup=markup)
    elif(message.text== '1 класс'): # Вывод всех оценок 1 класса
        sqlite_select_query = """SELECT *from `1Klass` """ # Метод, вытаскивающий данные из таблицы "1klass"
        cursor.execute(sqlite_select_query) # Вызов метода "sqlite_select_query" с помощью курсора
        records = cursor.fetchall() # Запись количества записей в таблице в переменную "records", для создания цикла
        bot.send_message(message.chat.id, 'Оценки 1 класса:') # Отправка сообщения пользователю
        for row in records: # Цикл, перебирающий данные из таблицы "1klass" и отправляющий их пользователю в разных сообщениях
            bot.send_message(message.chat.id, f'ID- {row[0]}\nФамилия - {row[1]}\nИмя - {row[2]}\nОтчество - {row[3]}\nМатематика - {row[4]}\nРусский Язык - {row[5]}\nЛитература - {row[6]}\nЧтение - {row[7]}\nОкружающий мир - {row[8]}\nФиз-ра - {row[9]}\nТехнология - {row[10]}\nМузыка - {row[11]}')
    elif(message.text == '2 класс'):
        sqlite_select_query = """SELECT *from `2Klass` """
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        bot.send_message(message.chat.id, 'Оценки 2 класса:')
        for row in records:
            bot.send_message(message.chat.id, f'ID - {row[0]}\nФамилия - {row[1]}\nИмя - {row[2]}\nОтчество - {row[3]}\nМатематика - {row[4]}\nРусский язык - {row[5]}\nЧтение - {row[6]}\nОкружающий мир - {row[7]}\nИскусство - {row[8]}\nФиз-ра - {row[9]}\nМузыка - {row[10]}\nТехнология - {row[11]}\nАнглийский язык - {row[12]}')
    elif(message.text == '3 класс'):
        sqlite_select_query = """SELECT *from `3Klass`"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        bot.send_message(message.chat.id, 'Оценки 3 класса:')
        for row in records:
            bot.send_message(message.chat.id, f'ID - {row[0]}\nФамилия - {row[1]}\nИмя - {row[2]}\nОтчество - {row[3]}\nМатематика - {row[4]}\nРусский язык - {row[5]}\nОкружающий мир - {row[6]}\nЧтение - {row[7]}\nИЗО - {row[8]}\nФиз-ра - {row[9]}\nМузыка - {row[10]}\nТехнология - {row[11]}\nАнглийский язык - {row[12]}')
    elif(message.text == '4 класс'):
        sqlite_select_query = """SELECT *from `4Klass`"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        bot.send_message(message.chat.id, 'Оценки 4 класса:')
        for row in records:
            bot.send_message(message.chat.id, f'ID - {row[0]}\nФамилия - {row[1]}\nИмя - {row[2]}\nОтчество - {row[3]}\nМатематика - {row[4]}\nРусский язык - {row[5]}\nОкружающий мир - {row[6]}\nИЗО - {row[7]}\nФиз-ра - {row[8]}\nМузыка - {row[9]}\nТехнология - {row[10]}\nАнглийский язык - {row[11]}')
    elif(message.text == '5 класс'):
        sqlite_select_query = """SELECT *from `5Klass`"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        bot.send_message(message.chat.id, 'Оценки 5 класса:')
        for row in records:
            bot.send_message(message.chat.id, f"ID - {row[0]}\nФамилия - {row[1]}\nИмя - {row[2]}\nОтчество - {row[3]}\nМатематика - {row[4]}\nРусский язык - {row[5]}\nБиология - {row[6]}\nГеография - {row[7]}\nЛитература - {row[8]}\nИстория - {row[9]}\nТехнология - {row[10]}\nМузыка - {row[11]}\nИЗО - {row[12]}\nФиз-ра - {row[13]}\nАнглийский язык - {row[14]}\nОБЖ - {row[15]}\nИнформатика - {row[16]}")
    elif(message.text == '6 класс'):
        sqlite_select_query = """SELECT *from `6Klass`"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        bot.send_message(message.chat.id, 'Оценки 6 класса:')
        for row in records:
            bot.send_message(message.chat.id, f'ID - {row[0]}\nФамилия - {row[1]}\nИмя - {row[2]}\nОтчество - {row[3]}\nМатематика - {row[4]}\nРусский язык - {row[5]}\nЛитература - {row[6]}\nИстория - {row[7]}\nОбществознание - {row[8]}\nГеография - {row[9]}\nБиология - {row[10]}\nФиз-ра - {row[11]}\nТехнология - {row[12]}\nАнглийский язык - {row[13]}\nМузыка - {row[14]}')
    elif(message.text == '7 класс'):
        sqlite_select_query = """SELECT *from `7Klass`"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        bot.send_message(message.chat.id, 'Оценки 7 класса:')
        for row in records:
            bot.send_message(message.chat.id, f'ID - {row[0]}\nФамилия - {row[1]}\nИмя - {row[2]}\nОтчество - {row[3]}\nМатематика - {row[4]}\nРусский язык - {row[5]}\nЛитература - {row[6]}\nФизика - {row[7]}\nФиз-ра - {row[8]}\nБиология - {row[9]}\nОбществознание - {row[10]}\nИстория - {row[11]}\nТехнология - {row[12]}\nМузыка - {row[13]}\nИЗО - {row[14]}\nГеография - {row[15]}\nИнформатика - {row[16]}\nАнглийский язык - {row[17]}')
    elif(message.text == '8 класс'):
        sqlite_select_query = """SELECT *from `8Klass`"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        bot.send_message(message.chat.id, 'Оценки 8 класса:')
        for row in records:
            bot.send_message(message.chat.id, f'ID - {row[0]}\nФамилия - {row[1]}\nИмя - {row[2]}\nОтчество - {row[3]}\nМатематика - {row[4]}\nРусский язык - {row[5]}\nЛитература - {row[6]}\nФизика - {row[7]}\nБиология - {row[8]}\nХимия - {row[9]}\nОбществознание - {row[10]}\nИстория - {row[11]}\nТехнология - {row[12]}\nМузыка - {row[13]}\nГеография - {row[14]}\nОБЖ - {row[15]}\nИнформатика - {row[16]}\nАнглийский язык - {row[17]}\nФиз-ра - {row[18]}')
    elif(message.text == '9 класс'):
        sqlite_select_query = """SELECT *from `9Klass`"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        bot.send_message(message.chat.id, 'Оценки 9 класса:')
        for row in records:
            bot.send_message(message.chat.id, f'ID - {row[0]}\nФамилия - {row[1]}\nИмя - {row[2]}\nОтчество - {row[3]}\nМатематика - {row[4]}\nРусский язык - {row[5]}\nФизика - {row[6]}\nЛитература - {row[7]}\nГеография - {row[8]}\nИстория - {row[9]}\nОбществознание - {row[10]}\nХимия - {row[11]}\nБиология - {row[12]}\nФиз-ра - {row[13]}\nАнглийский язык - {row[14]}\nИнформатика - {row[15]}\nОБЖ - {row[16]}\nТехнология - {row[17]}')
    elif(message.text == '10 класс'):
        sqlite_select_query = """SELECT *from `10Klass`"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        bot.send_message(message.chat.id, 'Оценки 10 класса')
        for row in records:
            bot.send_message(message.chat.id, f'ID - {row[0]}\nФамилия - {row[1]}\nИмя - {row[2]}\nОтчество - {row[3]}\nМатематика - {row[4]}\nРусский язык - {row[5]}\nФизика - {row[6]}\nБиология - {row[7]}\nИстория - {row[8]}\nОбществознание - {row[9]}\nЛитература - {row[10]}\nГеография - {row[11]}\nХимия - {row[12]}\nИнформатика - {row[13]}\nАнглийский язык - {row[14]}\nФиз-ра - {row[15]}\nОБЖ - {row[16]}\nТехнология - {row[17]}\nЭкология - {row[18]}')
    elif(message.text == '11 класс'):
        sqlite_select_query = """SELECT *from `11Klass`"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        bot.send_message(message.chat.id, 'Оценки 11 класса')
        for row in records:
            bot.send_message(message.chat.id, f'ID - {row[0]}\nФамилия - {row[1]}\nИмя - {row[2]}\nОтчество - {row[3]}\nМатематика - {row[4]}\nРусский язык - {row[5]}\nБиология - {row[6]}\nХимия - {row[7]}\nФизика - {row[8]}\nОбществознание - {row[9]}\nГеография - {row[10]}\nИстория - {row[11]}\nЛитература - {row[12]}\nИнформатика - {row[13]}\nАнглийский язык - {row[14]}\nФиз-ра - {row[15]}\nТехнология - {row[16]}\nАстрономия - {row[17]}\nЭкология - {row[18]}')
    elif(message.text == 'назад'): # Обработка кнопки "назад"
        start(message) # Возвращение к методу "start"
    else: # Обработка любого другого текстового сообщения
        bot.send_message(message.chat.id, 'я вас не понимаю, для того чтобы узнать список команд - напишите /help')
   


# Запуск бота
bot.polling(none_stop=True, interval=0)