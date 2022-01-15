import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.TOKEN)


# Приветсвенное письмо и отображение кнопок 

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

#кнопки

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Показать развлечения")

    markup.add(item1)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный, чтобы показывать развлечения города - Симферополь.'.format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

# Проверка результатов кнопок
@bot.message_handler(content_types=['text'])
def relax_all(message):
    if message.text == '🎲 Показать развлечения':
        delete = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Прекрасно, сейчас все расскажу... 😃')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Рестораны")
        item2 = types.KeyboardButton("Парки")
        item3 = types.KeyboardButton("Игровые комнаты")
        item4 = types.KeyboardButton("Музеи")            
        item5 = types.KeyboardButton("Кинотеатры")            
        item6 = types.KeyboardButton("ТРК")
        # сделать инлайновую клаву с этими кнопками 

        markup.add(item1, item2, item3, item4, item5, item6)            
        bot.send_message(message.chat.id, 'О чем рассказать подробнее? 😊', reply_markup=markup)

# ----------------------------------------------
    elif message.text == "Рестораны":
        telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Выберите ресторан... ')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Тут вам не там")
        item2 = types.KeyboardButton("23 Cafe boulangerie")            
        item3 = types.KeyboardButton("Simfero")            
        item4 = types.KeyboardButton("Айвазовский")            
        item5 = types.KeyboardButton("Grill Pizza Station")            
        item6 = types.KeyboardButton("Павлин Мавлин")
        item7 = types.KeyboardButton("Мияги")
        item8 = types.KeyboardButton("Оранжерея")
        item9 = types.KeyboardButton("New York Street Pizza")
        item10 = types.KeyboardButton("Назад")

        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)            
        bot.send_message(message.chat.id, 'Приятного аппетита', reply_markup=markup);  
    elif message.text == "Парки":
        telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Выберите парк... ')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Детский парк")
        item2 = types.KeyboardButton("Гагаринский парк")            
        item3 = types.KeyboardButton("Парк Тренёва")        
        item3 = types.KeyboardButton("Екатерининский сад")        
        item3 = types.KeyboardButton("Парк Шевченко")        
        item4 = types.KeyboardButton("Назад")

        markup.add(item1, item2, item3, item4)            
        bot.send_message(message.chat.id, 'Хорошего отдыха', reply_markup=markup);
    elif message.text == "Игровые комнаты":
        telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'выберите игровую комнату...')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Wow! Парк")
        item2 = types.KeyboardButton("Рыжий кот") 
        item3 = types.KeyboardButton("Action Park Пандориум")            
        item4 = types.KeyboardButton("Парк чудес")            
        item5 = types.KeyboardButton("Знаниум")                   
        item6 = types.KeyboardButton("Неопарк")            
        item7 = types.KeyboardButton("Чудо остров")            
        item8 = types.KeyboardButton("Лаборатория Пингвинов")            
        item9 = types.KeyboardButton("Лазертаг-клуб Tager")   
        item10 = types.KeyboardButton("7 Сот")               
        item11 = types.KeyboardButton("Скалодром ParkRock Симферополь")            
        item12 = types.KeyboardButton("Лазертаг Объект № 22")

        item13 = types.KeyboardButton("Назад")

        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9 ,item10, item11, item12, item13)            
        bot.send_message(message.chat.id, 'Хорошего проведение времени', reply_markup=markup);
    elif message.text == "Музеи":
        telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'выберите "место культуры" ... ')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Симферопольский художественный музей") 
        item2 = types.KeyboardButton("МБУК Музей истории города Симферополя")            
        item3 = types.KeyboardButton("Центральный музей Тавриды")            
        item4 = types.KeyboardButton("ГБУ РК Крымский этнографический музей")            
        item5 = types.KeyboardButton("Музей городского транспорта")            
        item6 = types.KeyboardButton("Крымскотатарский музей культурно-исторического наследия")
        item7 = types.KeyboardButton("Дом-музей имени И.Л. Сельвинского при КРУ ЦМТ")
        item8 = types.KeyboardButton("Назад")

        markup.add(item1, item2, item3, item4, item5, item6, item7, item8)            
        bot.send_message(message.chat.id, 'Хорошего время провождения', reply_markup=markup);
    elif message.text == "Кинотеатры":
        telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'выберите кинотеатр... ')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Люмен")
        item2 = types.KeyboardButton("Мультиплекс")            
        item3 = types.KeyboardButton("Мир кино")            
        item4 = types.KeyboardButton("Кинотеатр Шевченко")            
        item5 = types.KeyboardButton("Спартак")            
        item6 = types.KeyboardButton("Кино Берг")
        item7 = types.KeyboardButton("Назад")

        markup.add(item1, item2, item3, item4, item5, item6, item7)            
        bot.send_message(message.chat.id, 'Приятного аппетита', reply_markup=markup);
    elif message.text == "ТРК":
        telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'выберите ТРК... ')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Меганом")
        item2 = types.KeyboardButton("Снеха сити")            
        item3 = types.KeyboardButton("Берг")            
        item4 = types.KeyboardButton("Ашан/Южная галерея")            
        item5 = types.KeyboardButton("FM")            
        item6 = types.KeyboardButton("Центрум")
        item7 = types.KeyboardButton("Назад")

        markup.add(item1, item2, item3, item4, item5, item6, item7)            
        bot.send_message(message.chat.id, 'ГОРЯЧЁ-ЖАРКИХ скидок', reply_markup=markup);
    elif message.text == "Назад":
        delete = telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Рестораны")
        item2 = types.KeyboardButton("Парки")
        item3 = types.KeyboardButton("Игровые комнаты")
        item4 = types.KeyboardButton("Музеи")            
        item5 = types.KeyboardButton("Кинотеатры")            
        item6 = types.KeyboardButton("ТРК")
        # сделать инлайновую клаву с этими кнопками 

        markup.add(item1, item2, item3, item4, item5, item6,)            
        bot.send_message(message.chat.id, 'О чем рассказать подробнее? 😊', reply_markup=markup)

# ---------------------------------------------- Рестораны
    elif message.text == "Тут вам не там":
        telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("23 Cafe boulangerie")            
        item3 = types.KeyboardButton("Simfero")            
        item4 = types.KeyboardButton("Айвазовский")            
        item5 = types.KeyboardButton("Grill Pizza Station")            
        item6 = types.KeyboardButton("Павлин Мавлин")
        item7 = types.KeyboardButton("Мияги")
        item8 = types.KeyboardButton("Оранжерея")
        item9 = types.KeyboardButton("New York Street Pizza")
        item10 = types.KeyboardButton("Назад")

        markup.add(item2, item3, item4, item5, item6, item7, item8, item9, item10)            
        bot.send_message(message.chat.id, 'Полный адрес: Кавказская ул., 16 этаж 1 \nВремя открытия: 10:00 \nВремя закрытия 00:00 \nРейтинг: 4,4 \nТелефон: +7 (978) 554-46-66 \n ', reply_markup=markup);
    elif message.text == "23 Cafe boulangerie":
        telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("Тут вам не там")            
        item3 = types.KeyboardButton("Simfero")            
        item4 = types.KeyboardButton("Айвазовский")            
        item5 = types.KeyboardButton("Grill Pizza Station")            
        item6 = types.KeyboardButton("Павлин Мавлин")
        item7 = types.KeyboardButton("Мияги")
        item8 = types.KeyboardButton("Оранжерея")
        item9 = types.KeyboardButton("New York Street Pizza")
        item10 = types.KeyboardButton("Назад")

        markup.add(item2, item3, item4, item5, item6, item7, item8, item9, item10)            
        bot.send_message(message.chat.id, 'Полный адрес: ул. Карла Маркса, 14 14/9 \nВремя открытия: 8:00 \nВремя закрытия 00:00 \nРейтинг: 4,9\nТелефон: +7 (978) 900-53-23 \n ', reply_markup=markup);
    elif message.text == "Simfero":
        telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("23 Cafe boulangerie")            
        item3 = types.KeyboardButton("Тут вам не там")            
        item4 = types.KeyboardButton("Айвазовский")            
        item5 = types.KeyboardButton("Grill Pizza Station")            
        item6 = types.KeyboardButton("Павлин Мавлин")
        item7 = types.KeyboardButton("Мияги")
        item8 = types.KeyboardButton("Оранжерея")
        item9 = types.KeyboardButton("New York Street Pizza")
        item10 = types.KeyboardButton("Назад")

        markup.add(item2, item3, item4, item5, item6, item7, item8, item9, item10)            
        bot.send_message(message.chat.id, 'Полный адрес: ул. Карла Маркса, 28 • этаж 5 \nВремя открытия: 12:00 \nВремя закрытия 00:00 \nРейтинг: 4,7\nТелефон: +7 (978) 701-28-28 \n ', reply_markup=markup);
    elif message.text == "Айвазовский":
        telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("23 Cafe boulangerie")            
        item3 = types.KeyboardButton("Simfero")            
        item4 = types.KeyboardButton("Тут вам не там")            
        item5 = types.KeyboardButton("Grill Pizza Station")            
        item6 = types.KeyboardButton("Павлин Мавлин")
        item7 = types.KeyboardButton("Мияги")
        item8 = types.KeyboardButton("Оранжерея")
        item9 = types.KeyboardButton("New York Street Pizza")
        item10 = types.KeyboardButton("Назад")

        markup.add(item2, item3, item4, item5, item6, item7, item8, item9, item10)            
        bot.send_message(message.chat.id, 'Полный адрес: Турецкая ул., 30 \nВремя открытия: 12:00 \nВремя закрытия 02:00 \nРейтинг: 4,6 \nТелефон: +7 (978) 864-88-89 \n ', reply_markup=markup);
    elif message.text == "Grill Pizza Station":
        telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("23 Cafe boulangerie")            
        item3 = types.KeyboardButton("Simfero")            
        item4 = types.KeyboardButton("Айвазовский")            
        item5 = types.KeyboardButton("Тут вам не там")            
        item6 = types.KeyboardButton("Павлин Мавлин")
        item7 = types.KeyboardButton("Мияги")
        item8 = types.KeyboardButton("Оранжерея")
        item9 = types.KeyboardButton("New York Street Pizza")
        item10 = types.KeyboardButton("Назад")

        markup.add(item2, item3, item4, item5, item6, item7, item8, item9, item10)            
        bot.send_message(message.chat.id, 'Полный адрес: просп. Академика Вернадского, 141 \nВремя открытия: 11:00 \nВремя закрытия 23:00 \nРейтинг: 5,0\nТелефон: +7 (978) 121-08-88 \n ', reply_markup=markup);
    elif message.text == "Павлин Мавлин":
        telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("23 Cafe boulangerie")            
        item3 = types.KeyboardButton("Simfero")            
        item4 = types.KeyboardButton("Айвазовский")            
        item5 = types.KeyboardButton("Grill Pizza Station")            
        item6 = types.KeyboardButton("Тут вам не там")
        item7 = types.KeyboardButton("Мияги")
        item8 = types.KeyboardButton("Оранжерея")
        item9 = types.KeyboardButton("New York Street Pizza")
        item10 = types.KeyboardButton("Назад")

        markup.add(item2, item3, item4, item5, item6, item7, item8, item9, item10)            
        bot.send_message(message.chat.id, 'Полный адрес: ул. Воровского, 2 \nВремя открытия: 11:00 \nВремя закрытия 00:00 \nРейтинг: 4,6\nТелефон: +7 (978) 227-02-27 \n ', reply_markup=markup);
    elif message.text == "Мияги":
        telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("23 Cafe boulangerie")            
        item3 = types.KeyboardButton("Simfero")            
        item4 = types.KeyboardButton("Айвазовский")            
        item5 = types.KeyboardButton("Grill Pizza Station")            
        item6 = types.KeyboardButton("Павлин Мавлин")
        item7 = types.KeyboardButton("Тут вам не там")
        item8 = types.KeyboardButton("Оранжерея")
        item9 = types.KeyboardButton("New York Street Pizza")
        item10 = types.KeyboardButton("Назад")

        markup.add(item2, item3, item4, item5, item6, item7, item8, item9, item10)            
        bot.send_message(message.chat.id, 'Полный адрес: просп. Кирова, 29  \nВремя открытия: 11:00 \nВремя закрытия 00:00 \nРейтинг: 4,5\nТелефон: +7 (978) 740-72-24 \n ', reply_markup=markup);
    elif message.text == "Оранжерея":
        telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("23 Cafe boulangerie")            
        item3 = types.KeyboardButton("Simfero")            
        item4 = types.KeyboardButton("Айвазовский")            
        item5 = types.KeyboardButton("Grill Pizza Station")            
        item6 = types.KeyboardButton("Павлин Мавлин")
        item7 = types.KeyboardButton("Тут вам не там")
        item8 = types.KeyboardButton("Мияги")
        item9 = types.KeyboardButton("New York Street Pizza")
        item10 = types.KeyboardButton("Назад")

        markup.add(item2, item3, item4, item5, item6, item7, item8, item9, item10)            
        bot.send_message(message.chat.id, 'Полный адрес: Севастопольская ул., 62 • этаж 4 \nВремя открытия: 9:00 \nВремя закрытия 00:00 \nРейтинг: 4,3\nТелефон: +7 (978) 901-11-20 \n ', reply_markup=markup);
    elif message.text == "New York Street Pizza":
        telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("23 Cafe boulangerie")            
        item3 = types.KeyboardButton("Simfero")            
        item4 = types.KeyboardButton("Айвазовский")            
        item5 = types.KeyboardButton("Grill Pizza Station")            
        item6 = types.KeyboardButton("Павлин Мавлин")
        item7 = types.KeyboardButton("Тут вам не там")
        item8 = types.KeyboardButton("Оранжерея")
        item9 = types.KeyboardButton("Мияги")
        item10 = types.KeyboardButton("Назад")

        markup.add(item2, item3, item4, item5, item6, item7, item8, item9, item10)            
        bot.send_message(message.chat.id, 'Полный адрес: ул. Горького, 2 \nВремя открытия: 11:00 \nВремя закрытия 23:00 \nРейтинг: 4,8\nТелефон: +7 (978) 871-00-03 \n ', reply_markup=markup);
# ---------------------------------------------- Парки
    elif message.text == "Детский парк":
        telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Выберите парк... ')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("Гагаринский парк")            
        item3 = types.KeyboardButton("Парк Тренёва")        
        item4 = types.KeyboardButton("Екатерининский сад")        
        item5 = types.KeyboardButton("Парк Шевченко")        
        item6 = types.KeyboardButton("Назад")

        markup.add(item2, item3, item4, item5, item6)            
        bot.send_message(message.chat.id, 'Полный адрес: 44.956045, 34.109849  \nВремя открытия: 00:00 \nВремя закрытия 00:00 \nРейтинг: 4,5', reply_markup=markup);
    elif message.text == "Гагаринский парк":
        telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Выберите парк... ')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("Детский парк")            
        item3 = types.KeyboardButton("Парк Тренёва")        
        item4 = types.KeyboardButton("Екатерининский сад")        
        item5 = types.KeyboardButton("Парк Шевченко")        
        item6 = types.KeyboardButton("Назад")

        markup.add(item2, item3, item4, item5, item6)            
        bot.send_message(message.chat.id, 'Полный адрес: 44.964278, 34.097881  \nВремя открытия: 00:00 \nВремя закрытия 00:00 \nРейтинг: 4,5', reply_markup=markup);
    elif message.text == "Парк Тренёва":
        telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Выберите парк... ')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("Гагаринский парк")            
        item3 = types.KeyboardButton("Детский парк")        
        item4 = types.KeyboardButton("Екатерининский сад")        
        item5 = types.KeyboardButton("Парк Шевченко")        
        item6 = types.KeyboardButton("Назад")

        markup.add(item2, item3, item4, item5, item6)            
        bot.send_message(message.chat.id, 'Полный адрес: 44.946132, 34.098287  \nВремя открытия: 00:00 \nВремя закрытия 00:00 \nРейтинг: 4,5', reply_markup=markup);
    elif message.text == "Екатерининский сад":
        telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Выберите парк... ')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("Гагаринский парк")            
        item3 = types.KeyboardButton("Парк Тренёва")        
        item4 = types.KeyboardButton("Детский парк")        
        item5 = types.KeyboardButton("Парк Шевченко")        
        item6 = types.KeyboardButton("Назад")

        markup.add(item2, item3, item4, item5, item6)            
        bot.send_message(message.chat.id, 'Полный адрес: 44.952199, 34.105733  \nВремя открытия: 00:00 \nВремя закрытия 00:00 \nРейтинг: 4,5', reply_markup=markup);
    elif message.text == "Парк Шевченко":
        telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Выберите парк... ')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("Гагаринский парк")            
        item3 = types.KeyboardButton("Парк Тренёва")        
        item4 = types.KeyboardButton("Екатерининский сад")        
        item5 = types.KeyboardButton("Детский парк")        
        item6 = types.KeyboardButton("Назад")

        markup.add(item2, item3, item4, item5, item6)            
        bot.send_message(message.chat.id, 'Полный адрес: 44.934825, 34.090520  \nВремя открытия: 00:00 \nВремя закрытия 00:00 \nРейтинг: 4,5', reply_markup=markup);
# ---------------------------------------------- Игровые комнаты

    elif message.text == "Wow! Парк":
        telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("Рыжий кот") 
        item3 = types.KeyboardButton("Action Park Пандориум")            
        item4 = types.KeyboardButton("Парк чудес")            
        item5 = types.KeyboardButton("Знаниум")                   
        item6 = types.KeyboardButton("Неопарк")            
        item7 = types.KeyboardButton("Чудо остров")            
        item8 = types.KeyboardButton("Лаборатория Пингвинов")            
        item9 = types.KeyboardButton("Лазертаг-клуб Tager")   
        item10 = types.KeyboardButton("7 Сот")               
        item11 = types.KeyboardButton("Скалодром ParkRock Симферополь")            
        item12 = types.KeyboardButton("Лазертаг Объект № 22")

        item13 = types.KeyboardButton("Назад")

        markup.add(item2, item3, item4, item5, item6, item7, item8, item9 ,item10, item11, item12, item13)                       
        bot.send_message(message.chat.id, 'Полный адрес: ул. Механизаторов, 51 \nВремя открытия: 20:00 \nВремя закрытия 21:00 \n ', reply_markup=markup);
    elif message.text == "Рыжий кот":
        telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("Wow! Парк")
        item3 = types.KeyboardButton("Action Park Пандориум")            
        item4 = types.KeyboardButton("Парк чудес")            
        item5 = types.KeyboardButton("Знаниум")                   
        item6 = types.KeyboardButton("Неопарк")            
        item7 = types.KeyboardButton("Чудо остров")            
        item8 = types.KeyboardButton("Лаборатория Пингвинов")            
        item9 = types.KeyboardButton("Лазертаг-клуб Tager")   
        item10 = types.KeyboardButton("7 Сот")               
        item11 = types.KeyboardButton("Скалодром ParkRock Симферополь")            
        item12 = types.KeyboardButton("Лазертаг Объект № 22")

        item13 = types.KeyboardButton("Назад")

        markup.add(item2, item3, item4, item5, item6, item7, item8, item9 ,item10, item11, item12, item13)                       
        bot.send_message(message.chat.id, 'Полный адрес: просп. Победы, 44Б • этаж 2 \nВремя открытия: 9:00 \nВремя закрытия 21:00 \n ', reply_markup=markup);
    elif message.text == "Action Park Пандориум":
        telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("Рыжий кот") 
        item3 = types.KeyboardButton("Wow! Парк")            
        item4 = types.KeyboardButton("Парк чудес")            
        item5 = types.KeyboardButton("Знаниум")                   
        item6 = types.KeyboardButton("Неопарк")            
        item7 = types.KeyboardButton("Чудо остров")            
        item8 = types.KeyboardButton("Лаборатория Пингвинов")            
        item9 = types.KeyboardButton("Лазертаг-клуб Tager")   
        item10 = types.KeyboardButton("7 Сот")               
        item11 = types.KeyboardButton("Скалодром ParkRock Симферополь")            
        item12 = types.KeyboardButton("Лазертаг Объект № 22")

        item13 = types.KeyboardButton("Назад")

        markup.add(item2, item3, item4, item5, item6, item7, item8, item9 ,item10, item11, item12, item13)                       
        bot.send_message(message.chat.id, 'Полный адрес: Евпаторийское ш., ТРК Meganom, этаж 2-й \nВремя открытия: 11:00 \nВремя закрытия 22:00 \n ', reply_markup=markup);
    elif message.text == "Парк чудес":
        telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("Рыжий кот") 
        item3 = types.KeyboardButton("Action Park Пандориум")            
        item4 = types.KeyboardButton("Wow! Парк")            
        item5 = types.KeyboardButton("Знаниум")                   
        item6 = types.KeyboardButton("Неопарк")            
        item7 = types.KeyboardButton("Чудо остров")            
        item8 = types.KeyboardButton("Лаборатория Пингвинов")            
        item9 = types.KeyboardButton("Лазертаг-клуб Tager")   
        item10 = types.KeyboardButton("7 Сот")               
        item11 = types.KeyboardButton("Скалодром ParkRock Симферополь")            
        item12 = types.KeyboardButton("Лазертаг Объект № 22")

        item13 = types.KeyboardButton("Назад")

        markup.add(item2, item3, item4, item5, item6, item7, item8, item9 ,item10, item11, item12, item13)                       
        bot.send_message(message.chat.id, 'Полный адрес: Киевская ул., 80 • Чистые пруды, этаж 2 \nВремя открытия: 10:00 \nВремя закрытия 20:00 \n ', reply_markup=markup);
    elif message.text == "Знаниум":
        telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("Рыжий кот") 
        item3 = types.KeyboardButton("Action Park Пандориум")            
        item4 = types.KeyboardButton("Парк чудес")            
        item5 = types.KeyboardButton("Wow! Парк")                   
        item6 = types.KeyboardButton("Неопарк")            
        item7 = types.KeyboardButton("Чудо остров")            
        item8 = types.KeyboardButton("Лаборатория Пингвинов")            
        item9 = types.KeyboardButton("Лазертаг-клуб Tager")   
        item10 = types.KeyboardButton("7 Сот")               
        item11 = types.KeyboardButton("Скалодром ParkRock Симферополь")            
        item12 = types.KeyboardButton("Лазертаг Объект № 22")

        item13 = types.KeyboardButton("Назад")

        markup.add(item2, item3, item4, item5, item6, item7, item8, item9 ,item10, item11, item12, item13)                       
        bot.send_message(message.chat.id, 'Полный адрес: Киевская ул., 115 • ДК Профсоюзов \nВремя открытия: 10:00 \nВремя закрытия 18:00 \n ', reply_markup=markup);
    elif message.text == "Неопарк":
        telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("Рыжий кот") 
        item3 = types.KeyboardButton("Action Park Пандориум")            
        item4 = types.KeyboardButton("Парк чудес")            
        item5 = types.KeyboardButton("Знаниум")                   
        item6 = types.KeyboardButton("Wow! Парк")            
        item7 = types.KeyboardButton("Чудо остров")            
        item8 = types.KeyboardButton("Лаборатория Пингвинов")            
        item9 = types.KeyboardButton("Лазертаг-клуб Tager")   
        item10 = types.KeyboardButton("7 Сот")               
        item11 = types.KeyboardButton("Скалодром ParkRock Симферополь")            
        item12 = types.KeyboardButton("Лазертаг Объект № 22")

        item13 = types.KeyboardButton("Назад")

        markup.add(item2, item3, item4, item5, item6, item7, item8, item9 ,item10, item11, item12, item13)                       
        bot.send_message(message.chat.id, 'Полный адрес: Севастопольская ул., 31Е ТРЦ Лоцман, этаж 2 \nВремя открытия: 10:00 \nВремя закрытия 20:00 \n ', reply_markup=markup);
    elif message.text == "Чудо остров":
        telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("Рыжий кот") 
        item3 = types.KeyboardButton("Action Park Пандориум")            
        item4 = types.KeyboardButton("Парк чудес")            
        item5 = types.KeyboardButton("Знаниум")                   
        item6 = types.KeyboardButton("Неопарк")            
        item7 = types.KeyboardButton("Wow! Парк")            
        item8 = types.KeyboardButton("Лаборатория Пингвинов")            
        item9 = types.KeyboardButton("Лазертаг-клуб Tager")   
        item10 = types.KeyboardButton("7 Сот")               
        item11 = types.KeyboardButton("Скалодром ParkRock Симферополь")            
        item12 = types.KeyboardButton("Лазертаг Объект № 22")

        item13 = types.KeyboardButton("Назад")
        markup.add(item2, item3, item4, item5, item6, item7, item8, item9 ,item10, item11, item12, item13)                       
        bot.send_message(message.chat.id, 'Полный адрес: просп. Победы, 5А \nВремя открытия: 10:00 \nВремя закрытия 20:00 \n ', reply_markup=markup);
    elif message.text == "Лаборатория Пингвинов":
        telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("Рыжий кот") 
        item3 = types.KeyboardButton("Action Park Пандориум")            
        item4 = types.KeyboardButton("Парк чудес")            
        item5 = types.KeyboardButton("Знаниум")                   
        item6 = types.KeyboardButton("Неопарк")            
        item7 = types.KeyboardButton("Чудо остров")            
        item8 = types.KeyboardButton("Wow! Парк")            
        item9 = types.KeyboardButton("Лазертаг-клуб Tager")   
        item10 = types.KeyboardButton("7 Сот")               
        item11 = types.KeyboardButton("Скалодром ParkRock Симферополь")            
        item12 = types.KeyboardButton("Лазертаг Объект № 22")

        item13 = types.KeyboardButton("Назад")

        markup.add(item2, item3, item4, item5, item6, item7, item8, item9 ,item10, item11, item12, item13)                       
        bot.send_message(message.chat.id, 'Полный адрес: Кечкеметская ул., 29 Мебельный парк Арнем, этаж 4 \nВремя открытия: 9:00 \nВремя закрытия 20:00', reply_markup=markup); 
    elif message.text == "Лазертаг-клуб Tager":
        telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("Рыжий кот") 
        item3 = types.KeyboardButton("Action Park Пандориум")            
        item4 = types.KeyboardButton("Парк чудес")            
        item5 = types.KeyboardButton("Знаниум")                   
        item6 = types.KeyboardButton("Неопарк")            
        item7 = types.KeyboardButton("Чудо остров")            
        item8 = types.KeyboardButton("Лаборатория Пингвинов")            
        item9 = types.KeyboardButton("Wow! Парк")   
        item10 = types.KeyboardButton("7 Сот")               
        item11 = types.KeyboardButton("Скалодром ParkRock Симферополь")            
        item12 = types.KeyboardButton("Лазертаг Объект № 22")

        item13 = types.KeyboardButton("Назад")

        markup.add(item2, item3, item4, item5, item6, item7, item8, item9 ,item10, item11, item12, item13)                       
        bot.send_message(message.chat.id, 'Полный адрес: ул. Крылова, 155А \nВремя открытия: 9:00 \nВремя закрытия 23:00 \n ', reply_markup=markup);
    elif message.text == "7 Сот":
        telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("Рыжий кот") 
        item3 = types.KeyboardButton("Action Park Пандориум")            
        item4 = types.KeyboardButton("Парк чудес")            
        item5 = types.KeyboardButton("Знаниум")                   
        item6 = types.KeyboardButton("Неопарк")            
        item7 = types.KeyboardButton("Чудо остров")            
        item8 = types.KeyboardButton("Лаборатория Пингвинов")            
        item9 = types.KeyboardButton("Лазертаг-клуб Tager")   
        item10 = types.KeyboardButton("Wow! Парк")               
        item11 = types.KeyboardButton("Скалодром ParkRock Симферополь")            
        item12 = types.KeyboardButton("Лазертаг Объект № 22")

        item13 = types.KeyboardButton("Назад")

        markup.add(item2, item3, item4, item5, item6, item7, item8, item9 ,item10, item11, item12, item13)                       
        bot.send_message(message.chat.id, 'Полный адрес: ул. Героев Сталинграда, 8 • ТЦ Фуршет \nВремя открытия: 11:00 \nВремя закрытия 22:00 \n ', reply_markup=markup);
    elif message.text == "Скалодром ParkRock Симферополь":
        telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("Рыжий кот") 
        item3 = types.KeyboardButton("Action Park Пандориум")            
        item4 = types.KeyboardButton("Парк чудес")            
        item5 = types.KeyboardButton("Знаниум")                   
        item6 = types.KeyboardButton("Неопарк")            
        item7 = types.KeyboardButton("Чудо остров")            
        item8 = types.KeyboardButton("Лаборатория Пингвинов")            
        item9 = types.KeyboardButton("Лазертаг-клуб Tager")   
        item10 = types.KeyboardButton("7 Сот")               
        item11 = types.KeyboardButton("Wow! Парк")            
        item12 = types.KeyboardButton("Лазертаг Объект № 22")

        item13 = types.KeyboardButton("Назад")

        markup.add(item2, item3, item4, item5, item6, item7, item8, item9 ,item10, item11, item12, item13)                       
        bot.send_message(message.chat.id, 'Полный адрес: Линейная ул., 2М • эт. 2 \nВремя открытия: 12:00 \nВремя закрытия 19:00 \n ', reply_markup=markup);
    elif message.text == "Лазертаг Объект № 22":
        telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("Рыжий кот") 
        item3 = types.KeyboardButton("Action Park Пандориум")            
        item4 = types.KeyboardButton("Парк чудес")            
        item5 = types.KeyboardButton("Знаниум")                   
        item6 = types.KeyboardButton("Неопарк")            
        item7 = types.KeyboardButton("Чудо остров")            
        item8 = types.KeyboardButton("Лаборатория Пингвинов")            
        item9 = types.KeyboardButton("Лазертаг-клуб Tager")   
        item10 = types.KeyboardButton("7 Сот")               
        item11 = types.KeyboardButton("Скалодром ParkRock Симферополь")            
        item12 = types.KeyboardButton("Wow! Парк")

        item13 = types.KeyboardButton("Назад")

        markup.add(item2, item3, item4, item5, item6, item7, item8, item9 ,item10, item11, item12, item13)                       
        bot.send_message(message.chat.id, 'Полный адрес: Киевская ул., 190Б, Симферополь \nВремя открытия: 00:00 \nВремя закрытия 00:00 \n ', reply_markup=markup);   
# ---------------------------------------------- Музеи

    elif message.text == "Симферопольский художественный музей":
        telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("МБУК Музей истории города Симферополя")            
        item3 = types.KeyboardButton("Центральный музей Тавриды")            
        item4 = types.KeyboardButton("ГБУ РК Крымский этнографический музей")            
        item5 = types.KeyboardButton("Музей городского транспорта")            
        item6 = types.KeyboardButton("Крымскотатарский музей культурно-исторического наследия")
        item7 = types.KeyboardButton("Дом-музей имени И.Л. Сельвинского при КРУ ЦМТ")
        item8 = types.KeyboardButton("Назад")

        markup.add(item2, item3, item4, item5, item6, item7, item8)            
        bot.send_message(message.chat.id, 'Полный адрес: Долгоруковская ул., 35А \nВремя открытия: 10:00 \nВремя закрытия 17:00 \n ', reply_markup=markup);
    elif message.text == "МБУК Музей истории города Симферополя":
        telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("Симферопольский художественный музей")            
        item3 = types.KeyboardButton("Центральный музей Тавриды")            
        item4 = types.KeyboardButton("ГБУ РК Крымский этнографический музей")            
        item5 = types.KeyboardButton("Музей городского транспорта")            
        item6 = types.KeyboardButton("Крымскотатарский музей культурно-исторического наследия")
        item7 = types.KeyboardButton("Дом-музей имени И.Л. Сельвинского при КРУ ЦМТ")
        item8 = types.KeyboardButton("Назад")

        markup.add(item2, item3, item4, item5, item6, item7, item8)            
        bot.send_message(message.chat.id, 'Полный адрес: Гоголя ул., 14 \nВремя открытия: 10:00 \nВремя закрытия 17:00 \n ', reply_markup=markup);
    elif message.text == "Центральный музей Тавриды":
        telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("МБУК Музей истории города Симферополя")            
        item3 = types.KeyboardButton("Симферопольский художественный музей")            
        item4 = types.KeyboardButton("ГБУ РК Крымский этнографический музей")            
        item5 = types.KeyboardButton("Музей городского транспорта")            
        item6 = types.KeyboardButton("Крымскотатарский музей культурно-исторического наследия")
        item7 = types.KeyboardButton("Дом-музей имени И.Л. Сельвинского при КРУ ЦМТ")
        item8 = types.KeyboardButton("Назад")

        markup.add(item2, item3, item4, item5, item6, item7, item8)            
        bot.send_message(message.chat.id, 'Полный адрес: Гоголя ул., 14 \nВремя открытия: 9:00 \nВремя закрытия 17:30 \n ', reply_markup=markup);
    elif message.text == "ГБУ РК Крымский этнографический музей":
        telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("МБУК Музей истории города Симферополя")            
        item3 = types.KeyboardButton("Центральный музей Тавриды")            
        item4 = types.KeyboardButton("Симферопольский художественный музей")            
        item5 = types.KeyboardButton("Музей городского транспорта")            
        item6 = types.KeyboardButton("Крымскотатарский музей культурно-исторического наследия")
        item7 = types.KeyboardButton("Дом-музей имени И.Л. Сельвинского при КРУ ЦМТ")
        item8 = types.KeyboardButton("Назад")

        markup.add(item2, item3, item4, item5, item6, item7, item8)            
        bot.send_message(message.chat.id, 'Полный адрес: Пушкина ул., 18 \nВремя открытия: 9:00 \nВремя закрытия 17:15 \n ', reply_markup=markup);
    elif message.text == "Музей городского транспорта":
        telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("МБУК Музей истории города Симферополя")            
        item3 = types.KeyboardButton("Центральный музей Тавриды")            
        item4 = types.KeyboardButton("ГБУ РК Крымский этнографический музей")            
        item5 = types.KeyboardButton("Симферопольский художественный музей")            
        item6 = types.KeyboardButton("Крымскотатарский музей культурно-исторического наследия")
        item7 = types.KeyboardButton("Дом-музей имени И.Л. Сельвинского при КРУ ЦМТ")
        item8 = types.KeyboardButton("Назад")

        markup.add(item2, item3, item4, item5, item6, item7, item8)            
        bot.send_message(message.chat.id, 'Полный адрес: Киевская ул., 78 \nВремя открытия: 8:00 \nВремя закрытия 14:00 \n ', reply_markup=markup);
    elif message.text == "Крымскотатарский музей культурно-исторического наследия":
        telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("МБУК Музей истории города Симферополя")            
        item3 = types.KeyboardButton("Центральный музей Тавриды")            
        item4 = types.KeyboardButton("ГБУ РК Крымский этнографический музей")            
        item5 = types.KeyboardButton("Музей городского транспорта")            
        item6 = types.KeyboardButton("Симферопольский художественный музей")
        item7 = types.KeyboardButton("Дом-музей имени И.Л. Сельвинского при КРУ ЦМТ")
        item8 = types.KeyboardButton("Назад")

        markup.add(item2, item3, item4, item5, item6, item7, item8)            
        bot.send_message(message.chat.id, 'Полный адрес: Чехова ул., 17 \nВремя открытия: 9:30 \nВремя закрытия 17:00 \n ', reply_markup=markup);
    elif message.text == "Дом-музей имени И.Л. Сельвинского при КРУ ЦМТ":
        telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("МБУК Музей истории города Симферополя")            
        item3 = types.KeyboardButton("Центральный музей Тавриды")            
        item4 = types.KeyboardButton("ГБУ РК Крымский этнографический музей")            
        item5 = types.KeyboardButton("Музей городского транспорта")            
        item6 = types.KeyboardButton("Крымскотатарский музей культурно-исторического наследия")
        item7 = types.KeyboardButton("Симферопольский художественный музей")
        item8 = types.KeyboardButton("Назад")

        markup.add(item2, item3, item4, item5, item6, item7, item8)            
        bot.send_message(message.chat.id, 'Полный адрес: Бонданый пер., 2 \nВремя открытия: 9:00 \nВремя закрытия 17:00 \n ', reply_markup=markup);
# ---------------------------------------------- Кинотеатры
    elif message.text == "Люмен":
        telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("Мультиплекс")            
        item3 = types.KeyboardButton("Мир кино")            
        item4 = types.KeyboardButton("Кинотеатр Шевченко")            
        item5 = types.KeyboardButton("Спартак")            
        item6 = types.KeyboardButton("Кино Берг")
        item7 = types.KeyboardButton("Назад")

        markup.add(item2, item3, item4, item5, item6, item7)                       
        bot.send_message(message.chat.id, 'Полный адрес: Севастопольская ул., 62 этаж 4\nВремя открытия: 8:00 \nВремя закрытия: 2:00', reply_markup=markup);
    elif message.text == "Мультиплекс":
        telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Люмен")
        item2 = types.KeyboardButton("Мультиплекс")            
        item3 = types.KeyboardButton("Мир кино")            
        item4 = types.KeyboardButton("Кинотеатр Шевченко")            
        item5 = types.KeyboardButton("Спартак")            
        item6 = types.KeyboardButton("Кино Берг")
        item7 = types.KeyboardButton("Назад")

        markup.add(item1, item3, item4, item5, item6, item7)                       
        bot.send_message(message.chat.id, 'Полный адрес: Евпаторийское ш., 8 ТЦ Меганом, этаж 2\nВремя открытия: 9:00 \nВремя закрытия: 3:00', reply_markup=markup);
    elif message.text == "Мир кино":
        telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Люмен")
        item2 = types.KeyboardButton("Мультиплекс")            
        item3 = types.KeyboardButton("Мир кино")            
        item4 = types.KeyboardButton("Кинотеатр Шевченко")            
        item5 = types.KeyboardButton("Спартак")            
        item6 = types.KeyboardButton("Кино Берг")
        item7 = types.KeyboardButton("Назад")

        markup.add(item1, item2, item4, item5, item6, item7)                       
        bot.send_message(message.chat.id, 'Полный адрес: Киевская ул., 189Б • ТЦ Южная Галерея\nВремя открытия: 10:00 \nВремя закрытия: 23:00', reply_markup=markup);
    elif message.text == "Кинотеатр Шевченко":
        telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Люмен")
        item2 = types.KeyboardButton("Мультиплекс")            
        item3 = types.KeyboardButton("Мир кино")            
        item4 = types.KeyboardButton("Кинотеатр Шевченко")            
        item5 = types.KeyboardButton("Спартак")            
        item6 = types.KeyboardButton("Кино Берг")
        item7 = types.KeyboardButton("Назад")

        markup.add(item1, item2, item3, item5, item6, item7)                       
        bot.send_message(message.chat.id, 'Полный адрес: ул. Горького, 5\nВремя открытия: 10:30 \nВремя закрытия: 20:00', reply_markup=markup);
    elif message.text == "Спартак":
        telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Люмен")
        item2 = types.KeyboardButton("Мультиплекс")            
        item3 = types.KeyboardButton("Мир кино")            
        item4 = types.KeyboardButton("Кинотеатр Шевченко")            
        item5 = types.KeyboardButton("Спартак")            
        item6 = types.KeyboardButton("Кино Берг")
        item7 = types.KeyboardButton("Назад")

        markup.add(item1, item2, item3, item4, item6, item7)                       
        bot.send_message(message.chat.id, 'Полный адрес: ул. Пушкина, 9\nВремя открытия: 9:00 \nВремя закрытия: 0:00', reply_markup=markup);
    elif message.text == "Кино Берг":
        telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Люмен")
        item2 = types.KeyboardButton("Мультиплекс")            
        item3 = types.KeyboardButton("Мир кино")            
        item4 = types.KeyboardButton("Кинотеатр Шевченко")            
        item5 = types.KeyboardButton("Спартак")            
        item6 = types.KeyboardButton("Кино Берг")
        item7 = types.KeyboardButton("Назад")

        markup.add(item1, item2, item3, item4, item5, item7)                       
        bot.send_message(message.chat.id, 'Полный адрес: просп. Кирова, 36Е ТЦ Берг, этаж 2\nВремя открытия: 9:30 \nВремя закрытия 23:00', reply_markup=markup);
# ---------------------------------------------- ТРК
    elif message.text == "Меганом":
        telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("Снеха сити")            
        item3 = types.KeyboardButton("Берг")            
        item4 = types.KeyboardButton("Ашан/Южная галерея")            
        item5 = types.KeyboardButton("FM")            
        item6 = types.KeyboardButton("Центрум")
        item7 = types.KeyboardButton("Назад")

        markup.add(item2, item3, item4, item5, item6, item7)            
        bot.send_message(message.chat.id, 'Полный адрес: Мирное \nВремя открытия: :00 \nВремя закрытия :00 \n ', reply_markup=markup);
    elif message.text == "Снеха сити":
        telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Меганом")           
        item3 = types.KeyboardButton("Берг")            
        item4 = types.KeyboardButton("Ашан/Южная галерея")            
        item5 = types.KeyboardButton("FM")            
        item6 = types.KeyboardButton("Центрум")
        item7 = types.KeyboardButton("Назад")

        markup.add(item1, item3, item4, item5, item6, item7)            
        bot.send_message(message.chat.id, 'Полный адрес: ул. \nВремя открытия: :00 \nВремя закрытия :00 \n ', reply_markup=markup);
    elif message.text == "Берг":
        telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Меганом")
        item2 = types.KeyboardButton("Снеха сити")                       
        item4 = types.KeyboardButton("Ашан/Южная галерея")            
        item5 = types.KeyboardButton("FM")            
        item6 = types.KeyboardButton("Центрум")
        item7 = types.KeyboardButton("Назад")

        markup.add(item1, item2, item4, item5, item6, item7)            
        bot.send_message(message.chat.id, 'Полный адрес: ул. \nВремя открытия: :00 \nВремя закрытия :00 \n ', reply_markup=markup);
    elif message.text == "Ашан/Южная галерея":
        telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Меганом")
        item2 = types.KeyboardButton("Снеха сити")            
        item3 = types.KeyboardButton("Берг")                       
        item5 = types.KeyboardButton("FM")            
        item6 = types.KeyboardButton("Центрум")
        item7 = types.KeyboardButton("Назад")

        markup.add(item1, item2, item3, item5, item6, item7)            
        bot.send_message(message.chat.id, 'Полный адрес: ул. \nВремя открытия: :00 \nВремя закрытия :00 \n ', reply_markup=markup);
    elif message.text == "FM":
        telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Меганом")
        item2 = types.KeyboardButton("Снеха сити")            
        item3 = types.KeyboardButton("Берг")            
        item4 = types.KeyboardButton("Ашан/Южная галерея")                       
        item6 = types.KeyboardButton("Центрум")
        item7 = types.KeyboardButton("Назад")

        markup.add(item1, item2, item3, item4, item6, item7)            
        bot.send_message(message.chat.id, 'Полный адрес: ул. \nВремя открытия: :00 \nВремя закрытия :00 \n ', reply_markup=markup);
    elif message.text == "Центрум":
        telebot.types.ReplyKeyboardRemove()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Меганом")
        item2 = types.KeyboardButton("Снеха сити")            
        item3 = types.KeyboardButton("Берг")            
        item4 = types.KeyboardButton("Ашан/Южная галерея")            
        item5 = types.KeyboardButton("FM")            
        item7 = types.KeyboardButton("Назад")

        markup.add(item1, item2, item3, item4, item5, item7)            
        bot.send_message(message.chat.id, 'Полный адрес: ул. \nВремя открытия: :00 \nВремя закрытия :00 \n ', reply_markup=markup);




bot.polling(none_stop=True) 