import telebot
from telebot import types
import sqlite3

bot = telebot.TeleBot('7952799563:AAGgfeSLaW3WEhYC3BLH-eYfKA0w4inp0Zo')

@bot.callback_query_handler(func=lambda call: True)
def get_stats(call):
    stats_counter = 0
    stats_message = "Список планет:\n\n"
    
    #bot.send_message(call.message.chat.id, call.data)
    #bot.send_message(call.message.chat.id, "Processing...")
    conn = sqlite3.connect('astronomy_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id_tg = ?", (call.data,))
    users = cursor.fetchone()
    if users[3] == 1:
        stats_counter = stats_counter + 1
        stats_message += "Меркурий: ✅\n"
    else:
        stats_message += "Меркурий: ❌\n"
    if users[4] == 1:
        stats_counter = stats_counter + 1
        stats_message += "Венера: ✅\n"
    else:
        stats_message += "Венера: ❌\n"
    if users[5] == 1:
        stats_counter = stats_counter + 1
        stats_message += "Земля: ✅\n"
    else:
        stats_message += "Земля: ❌\n"
    if users[6] == 1:
        stats_counter = stats_counter + 1
        stats_message += "Марс: ✅\n"
    else:
        stats_message += "Марс: ❌\n"
    if users[7] == 1:
        stats_counter = stats_counter + 1
        stats_message += "Юпитер: ✅\n"
    else:
        stats_message += "Юпитер: ❌\n"
    if users[8] == 1:
        stats_counter = stats_counter + 1
        stats_message += "Сатурн: ✅\n"
    else:
        stats_message += "Сатурн: ❌\n"
    if users[9] == 1:
        stats_counter = stats_counter + 1
        stats_message += "Уран: ✅\n"
    else:
        stats_message += "Уран: ❌\n"
    if users[10] == 1:
        stats_counter = stats_counter + 1
        stats_message += "Нептун: ✅\n"
    else:
        stats_message += "Нептун: ❌\n"
        
    stats_message += f"\nПройдено {str(stats_counter)}/8 планет.\n\n"
    
    if stats_counter == 8:
        stats_message += "🎉🎉🎉Поздравляю! Все станции пройдены. Для получения приза обратись к организаторам (44 кабинет).🎉🎉🎉"
    bot.send_message(call.message.chat.id, stats_message)
    cursor.close()
    conn.close()
    
    
    


@bot.message_handler(commands=['start'])
def to_say_hello(message):
    chat_id = str(message.chat.id)
    #bot.send_message(message.chat.id, 'Твой ID участника: ' + str(message.chat.id))
    #bot.send_message(message.chat.id, chat_id)
    conn = sqlite3.connect('astronomy_database.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (game_id integer primary key autoincrement, reg_attempt integer, id_tg text unique, mercury integer, venus integer, earth integer, mars integer, jupiter integer, saturn integer, uranus integer, neptun integer)')
    conn.commit()
    mrkp = telebot.types.InlineKeyboardMarkup()
    mrkp.add(telebot.types.InlineKeyboardButton('Отследить статистику📈:', callback_data = chat_id))
    cursor.execute("SELECT reg_attempt FROM users WHERE id_tg = ?", (chat_id,))
    users = cursor.fetchone()
    try:
        if users[0] == 1:
            cursor.execute("SELECT game_id FROM users WHERE id_tg = ?", (chat_id,))
            users = cursor.fetchone()
            info = users
            bot.send_message(chat_id, "Ты уже зарегистрирован! Твой номер участника: #" + str(info[0]), reply_markup = mrkp)
    except:
        bot.send_message(message.chat.id, 'Приветствую тебя, землянин! \n Да начнется отсюда твой путь среди звёзд!\n\n Посещай различные планеты и выполняй космические задания')
        #conn.execute("BEGIN IMMEDIATE")
    
        cursor.execute('INSERT OR IGNORE INTO users (id_tg) VALUES (?)', (chat_id,))
        #cursor.execute('UPDATE users SET mercury = COALESCE(mercury, 10)')
        conn.commit()
        cursor.execute("SELECT game_id FROM users WHERE id_tg = ?", (chat_id,))
        users = cursor.fetchone()
        info = users
        bot.send_message(message.chat.id, "Твой номер участника: #" + str(info[0]), reply_markup = mrkp)
        cursor.execute("UPDATE users SET reg_attempt = 1 WHERE id_tg = ?", (chat_id,))
        conn.commit()
    conn.commit()
    cursor.close()
    conn.close()
    
    
        
@bot.message_handler(commands=['admin'])
def check_as_admin_id(message):
    if(str(message.chat.id) == "-1026151711"):
        bot.send_message(message.chat.id, 'Вы вошли в режим администратора Меркурия')
        admin_mercury(message)
    elif(str(message.chat.id) == "1026151711"):
        bot.send_message(message.chat.id, 'Вы вошли в режим администратора Венеры')
        admin_venus(message)
    elif(str(message.chat.id) == "1451957284"):
        bot.send_message(message.chat.id, 'Вы вошли в режим администратора Земли')
        admin_earth(message)
    elif(str(message.chat.id) == "-1026151711"):
        bot.send_message(message.chat.id, 'Вы вошли в режим администратора Марса')
        admin_mars(message)
    elif(str(message.chat.id) == "-1026151711"):
        bot.send_message(message.chat.id, 'Вы вошли в режим администратора Юпитера')
        admin_jupiter(message)
    elif(str(message.chat.id) == "-1026151711"):
        bot.send_message(message.chat.id, 'Вы вошли в режим администратора Сатурна')
        admin_saturn(message)
    elif(str(message.chat.id) == "-1026151711"):
        bot.send_message(message.chat.id, 'Вы вошли в режим администратора Урана')
        admin_uranus(message)
    elif(str(message.chat.id) == "-1026151711"):
        bot.send_message(message.chat.id, 'Вы вошли в режим администратора Нептуна')
        admin_neptun(message)
    else:
        bot.send_message(message.chat.id, "Вы не являетесь администартором!")
    


def admin_mercury(message):
    
    planet_rus = "Меркурий"
    planet_eng = "mercury"
    bot.send_message(message.chat.id, 'Введите номер участника, завершившего ваше задание (без #)')
    bot.register_next_step_handler(message, game_id_input_function, planet_rus, planet_eng)
    
def admin_venus(message):
    
    planet_rus = "Венера"
    planet_eng = "venus"
    bot.send_message(message.chat.id, 'Введите номер участника, завершившего ваше задание (без #)')
    bot.register_next_step_handler(message, game_id_input_function, planet_rus, planet_eng)
    
def admin_earth(message):
    
    planet_rus = "Земля"
    planet_eng = "earth"
    bot.send_message(message.chat.id, 'Введите номер участника, завершившего ваше задание (без #)')
    bot.register_next_step_handler(message, game_id_input_function, planet_rus, planet_eng)
    
def admin_mars(message):
    
    planet_rus = "Марс"
    planet_eng = "mars"
    bot.send_message(message.chat.id, 'Введите номер участника, завершившего ваше задание (без #)')
    bot.register_next_step_handler(message, game_id_input_function, planet_rus, planet_eng)

def admin_jupiter(message):
    
    planet_rus = "Юпитер"
    planet_eng = "jupiter"
    bot.send_message(message.chat.id, 'Введите номер участника, завершившего ваше задание (без #)')
    bot.register_next_step_handler(message, game_id_input_function, planet_rus, planet_eng)

def admin_saturn(message):
    
    planet_rus = "Сатурн"
    planet_eng = "saturn"
    bot.send_message(message.chat.id, 'Введите номер участника, завершившего ваше задание (без #)')
    bot.register_next_step_handler(message, game_id_input_function, planet_rus, planet_eng)
    
def admin_uranus(message):
    
    planet_rus = "Уран"
    planet_eng = "uranus"
    bot.send_message(message.chat.id, 'Введите номер участника, завершившего ваше задание (без #)')
    bot.register_next_step_handler(message, game_id_input_function, planet_rus, planet_eng)
    
def admin_neptun(message):
    
    planet_rus = "Нептун"
    planet_eng = "neptun"
    bot.send_message(message.chat.id, 'Введите номер участника, завершившего ваше задание (без #)')
    bot.register_next_step_handler(message, game_id_input_function, planet_rus, planet_eng)
  

def game_id_input_function(message, planet_rus, planet_eng):
    try:
        game_id_of_user_who_writes = int(message.text)
        
        conn = sqlite3.connect('astronomy_database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id_tg FROM users WHERE game_id = ?", (int(game_id_of_user_who_writes),))
        users = cursor.fetchone()
        mrkp = telebot.types.InlineKeyboardMarkup()
        mrkp.add(telebot.types.InlineKeyboardButton('Отследить статистику📈:', callback_data = str(users[0])))
        cursor.execute(f"UPDATE users SET {planet_eng} = 1 WHERE game_id = ?", (game_id_of_user_who_writes,))
        conn.commit()
        
        cursor.execute("SELECT id_tg FROM users WHERE game_id = ?", (int(game_id_of_user_who_writes),))
        users = cursor.fetchone()
        info = users
        #bot.send_message(message.chat.id, "Твой номер участника: #" + str(info[0]), reply_markup = mrkp)
        conn.commit()
        cursor.close()
        conn.close()
        bot.send_message(int(info[0]), 'Успешное выполнение этапа ' + planet_rus + '!', reply_markup = mrkp)
        
        
        bot.send_message(message.chat.id, "Уведомление отправлено игроку успешно! :)")
    except:
        bot.send_message(message.chat.id, 'Нет такого участника, повторите попытку! :(')
    if (planet_rus == "Меркурий"):
         admin_mercury(message)
    elif (planet_rus == "Венера"):
        admin_venus(message)
    elif (planet_rus == "Земля"):
        admin_earth(message)
    elif (planet_rus == "Марс"):
        admin_mars(message)
    elif (planet_rus == "Юпитер"):
        admin_jupiter(message)
    elif (planet_rus == "Сатурн"):
        admin_saturn(message)
    elif (planet_rus == "Уран"):
        admin_uranus(message)
    elif (planet_rus == "Нептун"):
        admin_neptun(message)

    

bot.polling(none_stop=True, timeout = 2000000)