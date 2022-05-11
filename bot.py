import telebot
# import os
# import sys
# import django
import pandas as pd
from telebot import types



# project_path = os.path.dirname(os.path.abspath('/home/oleja/PycharmProjects/bg/bot.py'))
#
# sys.path.append(project_path)
#
# os.environ['DJANGO_SETTINGS_MODULE'] = 'baikal.settings'
#
# django.setup()

# from excelbaikal.models import Profile

TOKEN= '5312581817:AAHtd08tUol_oxYzCiyct82K0FMh-cwqih8'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item5 = types.KeyboardButton('ПАРНАС ПРИЕМКА')
    item6 = types.KeyboardButton('ПАРНАС ВЫДАЧА ')
    item2 = types.KeyboardButton('СОФИЙСКАЯ')
    item7 = types.KeyboardButton('ОТВЕТ.ХРАН.')
    item4 = types.KeyboardButton('МИНЕРАЛ')
    item3 = types.KeyboardButton('КИЕВСКАЯ')
    item1 = types.KeyboardButton('ОФИС')
    markup.add(item1, item2, item3, item4, item5, item6, item7)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}, выбери место работы'.format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'КИЕВСКАЯ':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item3 = types.KeyboardButton('Ивантей С.')
            item2 = types.KeyboardButton('Рябов Д.')
            item1 = types.KeyboardButton('Костин С.')
            back = types.KeyboardButton('<Назад')
            markup.add(item1, item2, item3, back)
            bot.send_message(message.chat.id, 'КИЕВСКАЯ', reply_markup=markup)
            send = bot.send_message(message.chat.id, 'Выберите Вашу фамилию и имя, или нажмите <Назад ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, kiev)


        elif message.text == 'МИНЕРАЛ':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item5 = types.KeyboardButton('Трофимов А.')
            item4 = types.KeyboardButton('Истомин А.В.')
            item3 = types.KeyboardButton('Хивренко А.')
            item2 = types.KeyboardButton('Крылов А')
            item1 = types.KeyboardButton('Чеботарёв Г.')
            back = types.KeyboardButton('<Назад')
            markup.add(item1, item2, item3, item4, item5, back)

            bot.send_message(message.chat.id, 'МИНЕРАЛЬНАЯ', reply_markup=markup)
            send = bot.send_message(message.chat.id, 'Выберите Вашу фамилию и имя, или нажмите <Назад ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, mineral)


        elif message.text == 'ОФИС':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item5 = types.KeyboardButton('Орлов Р.В.')
            item4 = types.KeyboardButton('Зарев А.В.')
            item3 = types.KeyboardButton('Жущиковский М.С.')
            item2 = types.KeyboardButton('Антонов А.А.')
            item1 = types.KeyboardButton('Строганов В.И.')
            back = types.KeyboardButton('<Назад')
            markup.add(item1, item2, item3, item4, item5, back)

            bot.send_message(message.chat.id, 'ОФИС', reply_markup=markup)
            send = bot.send_message(message.chat.id, 'Выберите Вашу фамилию и имя, или нажмите <Назад ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, office)


        elif message.text == 'ОТВЕТ.ХРАН.':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item4 = types.KeyboardButton('Тищенко Р.С.')
            item3 = types.KeyboardButton('Стольцев А.Ю.')
            item2 = types.KeyboardButton('Плотников В.В.')
            item1 = types.KeyboardButton('Гуцулюк О.')
            back = types.KeyboardButton('<Назад')
            markup.add(item1, item2, item3, item4, back)

            bot.send_message(message.chat.id, 'ОТВЕТ.ХРАН.', reply_markup=markup)
            send = bot.send_message(message.chat.id, 'Выберите Вашу фамилию и имя, или нажмите <Назад ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, otvet)


        elif message.text == 'СОФИЙСКАЯ':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item7 = types.KeyboardButton('Сычёв С.')
            item6 = types.KeyboardButton('Мавлетов А.')
            item5 = types.KeyboardButton('Кудин В.В.')
            item4 = types.KeyboardButton('Власов Н.')
            item3 = types.KeyboardButton('Власов И.')
            item2 = types.KeyboardButton('Богомолов В.')
            item1 = types.KeyboardButton('Захаров И.Ю.')
            back = types.KeyboardButton('<Назад')
            markup.add(item1, item2, item3, item4, item5, item6, item7, back)

            bot.send_message(message.chat.id, 'СОФИЙСКАЯ', reply_markup=markup)
            send = bot.send_message(message.chat.id, 'Выберите Вашу фамилию и имя, или нажмите <Назад ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, sofi)


        elif message.text == 'ПАРНАС ВЫДАЧА':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item18 = types.KeyboardButton('Полубояринов М.М.')
            item17 = types.KeyboardButton('Блинов Андрей')
            item16 = types.KeyboardButton('Варнаков Р.А.')
            item15 = types.KeyboardButton('Якман Т.')
            item14 = types.KeyboardButton('Якман А.')
            item13 = types.KeyboardButton('Синицын Александр')
            item12 = types.KeyboardButton('Старков Виктор')
            item11 = types.KeyboardButton('Трохолев Влад')
            item10 = types.KeyboardButton('Рожок Олег')
            item9 = types.KeyboardButton('Петров А.')
            item8 = types.KeyboardButton('Насир Ф.З.')
            item7 = types.KeyboardButton('Михайлов Алекс.')
            item6 = types.KeyboardButton('Корнилов Павел')
            item5 = types.KeyboardButton('Дроздов Д.С.')
            item4 = types.KeyboardButton('Цуриков М.Г.')
            item3 = types.KeyboardButton('Абашин А.Ю.')
            item2 = types.KeyboardButton('Карпов А.С.')
            item1 = types.KeyboardButton('Акимов Д.В.')

            back = types.KeyboardButton('<Назад')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, item15, item16, item17, item18, back)

            bot.send_message(message.chat.id, 'ПАРНАС ВЫДАЧА', reply_markup=markup)
            send = bot.send_message(message.chat.id, 'Выберите Вашу фамилию и имя, или нажмите <Назад ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, vydach)


        elif message.text == 'ПАРНАС ПРИЕМКА':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item19 = types.KeyboardButton('Хусаинов Х.М.')
            item18 = types.KeyboardButton('Волков Д.В.')
            item17 = types.KeyboardButton('Лукин О.В.')
            item16 = types.KeyboardButton('Дмитриев Иван')
            item15 = types.KeyboardButton('Яббаров Л.')
            item14 = types.KeyboardButton('Алберт Вечяслав')
            item13 = types.KeyboardButton('Шнитов Евгений')
            item12 = types.KeyboardButton('Церцеил Сергей')
            item11 = types.KeyboardButton('Строганов А.И.')
            item10 = types.KeyboardButton('Маринов Д.А.')
            item9 = types.KeyboardButton('Кузнецов Д.')
            item8 = types.KeyboardButton('Крат В.А.')
            item7 = types.KeyboardButton('Кассин Александр')
            item6 = types.KeyboardButton('Елфимов И.А.')
            item5 = types.KeyboardButton('Басов Михаил')
            item4 = types.KeyboardButton('Абдиев Тимур')
            item3 = types.KeyboardButton('Солодовников А.')
            item2 = types.KeyboardButton('Смирнов С.И.')
            item1 = types.KeyboardButton('Ванцевич В.Э.')

            back = types.KeyboardButton('<Назад')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, item15, item16, item17, item18, item19, back)

            bot.send_message(message.chat.id, 'ПАРНАС ПРИЕМКА', reply_markup=markup)
            send = bot.send_message(message.chat.id, 'Выберите Вашу фамилию и имя, или нажмите <Назад ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, priem)



        elif message.text == '<Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item5 = types.KeyboardButton('ПАРНАС ПРИЕМКА')
            item6 = types.KeyboardButton('ПАРНАС ВЫДАЧА')
            item2 = types.KeyboardButton('СОФИЙСКАЯ')
            item7 = types.KeyboardButton('ОТВЕТ.ХРАН.')
            item4 = types.KeyboardButton('МИНЕРАЛ')
            item3 = types.KeyboardButton('КИЕВСКАЯ')
            item1 = types.KeyboardButton('ОФИС')
            back = types.KeyboardButton('<Назад')
            markup.add(item1, item2, item3, item4, item5, item6, item7, back)

            bot.send_message(message.chat.id, '<Назад', reply_markup=markup)

        # elif message.chat == 'Рожок Олег':
        #     item1 = types.Message('day1     day2	day3	day4	day5	day6	day7	day8	day9	day10	day11	day12	day13	day14	day15	day16	day17	day18	day19	day20	day21	day22	day23	day24	day25	day26	day27	day28	day29	day30	day31')
        #     back = types.KeyboardButton('<Назад')
        #     bot.send_message(message.chat.id, '{0.first_name}!'.format(message.from_user), item1, back)
def office(message):
    data = pd.read_excel("shedule2.xlsx", sheet_name='Sheet1', index_col='id')
    if message.text == 'Орлов Р.В.':
        person60 = data.iloc[60]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person60)):
            bot.send_message(message.chat.id, result[i] + '  ' + person60[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, office)

    elif message.text == 'Зарев А.В.':
        person59 = data.iloc[59]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person59)):
            bot.send_message(message.chat.id, result[i] + '  ' + person59[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, office)
    elif message.text == 'Жущиковский М.С.':
        person58 = data.iloc[58]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person58)):
            bot.send_message(message.chat.id, result[i] + '  ' + person58[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, office)
    elif message.text == 'Антонов А.А.':
        person57 = data.iloc[57]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person57)):
            bot.send_message(message.chat.id, result[i] + '  ' + person57[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, office)
    elif message.text == 'Строганов В.И.':
        person56 = data.iloc[56]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person56)):
            bot.send_message(message.chat.id, result[i] + '  ' + person56[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, office)
def kiev(message):
    data = pd.read_excel("shedule2.xlsx", sheet_name='Sheet1', index_col='id')
    if message.text == 'Ивантей С.':
        person55 = data.iloc[55]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person55)):
            bot.send_message(message.chat.id, result[i] + '  ' + person55[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, kiev)
    elif message.text == 'Рябов Д.':
        person54 = data.iloc[54]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person54)):
            bot.send_message(message.chat.id, result[i] + '  ' + person54[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, kiev)
    elif message.text == 'Костин С.':
        person53 = data.iloc[53]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person53)):
            bot.send_message(message.chat.id, result[i] + '  ' + person53[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, kiev)

def mineral(message):
    data = pd.read_excel("shedule2.xlsx", sheet_name='Sheet1', index_col='id')
    if message.text == 'Трофимов А.':
        person52 = data.iloc[52]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person52)):
            bot.send_message(message.chat.id, result[i] + '  ' + person52[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, mineral)
    elif message.text == 'Истомин А.В.':
        person51 = data.iloc[51]
        result = data.iloc[61]
        for i in range(len(person51)):
            bot.send_message(message.chat.id, result[i] + '  ' + person51[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, mineral)
    elif message.text == 'Хивренко А.':
        person50 = data.iloc[50]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person50)):
            bot.send_message(message.chat.id, result[i] + '  ' + person50[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, mineral)
    elif message.text == 'Крылов А':
        person49 = data.iloc[49]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person49)):
            bot.send_message(message.chat.id, result[i] + '  ' + person49[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, mineral)
    elif message.text == 'Чеботарёв Г.':
        person48 = data.iloc[48]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person48)):
            bot.send_message(message.chat.id, result[i] + '  ' + person48[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, mineral)

def otvet(message):
    data = pd.read_excel("shedule2.xlsx", sheet_name='Sheet1', index_col='id')
    if message.text == 'Тищенко Р.С.':
        person47 = data.iloc[47]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person47)):
            bot.send_message(message.chat.id, result[i] + '  ' + person47[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, otvet)
    elif message.text == 'Стольцев А.Ю.':
        person46 = data.iloc[46]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person46)):
            bot.send_message(message.chat.id, result[i] + '  ' + person46[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, otvet)
    elif message.text == 'Плотников В.В.':
        person45 = data.iloc[45]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person45)):
            bot.send_message(message.chat.id, result[i] + '  ' + person45[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, otvet)
    elif message.text == 'Гуцулюк О.':
        person44 = data.iloc[44]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person44)):
            bot.send_message(message.chat.id, result[i] + '  ' + person44[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, otvet)

def sofi(message):
    data = pd.read_excel("shedule2.xlsx", sheet_name='Sheet1', index_col='id')
    if message.text == 'Сычёв С.':
        person43 = data.iloc[43]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person43)):
            bot.send_message(message.chat.id, result[i] + '  ' + person43[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, sofi)
    elif message.text == 'Мавлетов А.':
        person42 = data.iloc[42]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person42)):
            bot.send_message(message.chat.id, result[i] + '  ' + person42[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, sofi)
    elif message.text == 'Кудин В.В.':
        person41 = data.iloc[41]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person41)):
            bot.send_message(message.chat.id, result[i] + '  ' + person41[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, sofi)
    elif message.text == 'Власов Н.':
        person40 = data.iloc[40]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person40)):
            bot.send_message(message.chat.id, result[i] + '  ' + person40[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, sofi)
    elif message.text == 'Власов И.':
        person39 = data.iloc[39]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person39)):
            bot.send_message(message.chat.id, result[i] + '  ' + person39[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, sofi)
    elif message.text == 'Богомолов В.':
        person38 = data.iloc[38]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person38)):
            bot.send_message(message.chat.id, result[i] + '  ' + person38[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, sofi)
    elif message.text == 'Захаров И.Ю.':
        person37 = data.iloc[37]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person37)):
            bot.send_message(message.chat.id, result[i] + '  ' + person37[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, sofi)

def vydach(message):
    data = pd.read_excel("shedule2.xlsx", sheet_name='Sheet1', index_col='id')
    if message.text == 'Полубояринов М.М.':
        person36 = data.iloc[36]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person36)):
            bot.send_message(message.chat.id, result[i] + '  ' + person36[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, vydach)
    elif message.text == 'Блинов Андрей':
        person35 = data.iloc[35]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person35)):
            bot.send_message(message.chat.id, result[i] + '  ' + person35[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, vydach)
    elif message.text == 'Варнаков Р.А.':
        person34 = data.iloc[34]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person34)):
            bot.send_message(message.chat.id, result[i] + '  ' + person34[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, vydach)
    elif message.text == 'Якман Т.':
        person33 = data.iloc[33]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person33)):
            bot.send_message(message.chat.id, result[i] + '  ' + person33[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, vydach)
    elif message.text == 'Якман А.':
        person32 = data.iloc[32]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person32)):
            bot.send_message(message.chat.id, result[i] + '  ' + person32[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, vydach)
    elif message.text == 'Синицын Александр':
        person31 = data.iloc[31]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person31)):
            bot.send_message(message.chat.id, result[i] + '  ' + person31[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, vydach)
    elif message.text == 'Старков Виктор':
        person30 = data.iloc[30]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person30)):
            bot.send_message(message.chat.id, result[i] + '  ' + person30[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, vydach)
    elif message.text == 'Трохолев Влад':
        person29 = data.iloc[29]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person29)):
            bot.send_message(message.chat.id, result[i] + '  ' + person29[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, vydach)
    elif message.text == 'Рожок Олег':
        person28 = data.iloc[28]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person28)):
            bot.send_message(message.chat.id, result[i] + '  ' + person28[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, vydach)
    elif message.text == 'Петров А.':
        person27 = data.iloc[27]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person27)):
            bot.send_message(message.chat.id, result[i] + '  ' + person27[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, vydach)
    elif message.text == 'Насир Ф.З.':
        person26 = data.iloc[26]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person26)):
            bot.send_message(message.chat.id, result[i] + '  ' + person26[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, vydach)
    elif message.text == 'Михайлов Алекс.':
        person25 = data.iloc[25]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person25)):
            bot.send_message(message.chat.id, result[i] + '  ' + person25[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, vydach)
    elif message.text == 'Корнилов Павел':
        person24 = data.iloc[24]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person24)):
            bot.send_message(message.chat.id, result[i] + '  ' + person24[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, vydach)
    elif message.text == 'Дроздов Д.С.':
        person23 = data.iloc[23]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person23)):
            bot.send_message(message.chat.id, result[i] + '  ' + person23[i])

    elif message.text == 'Цуриков М.Г.':
        person22 = data.iloc[22]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person22)):
            bot.send_message(message.chat.id, result[i] + '  ' + person22[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, vydach)
    elif message.text == 'Абашин А.Ю.':
        person21 = data.iloc[21]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person21)):
            bot.send_message(message.chat.id, result[i] + '  ' + person21[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, vydach)
    elif message.text == 'Карпов А.С.':
        person20 = data.iloc[20]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person20)):
            bot.send_message(message.chat.id, result[i] + '  ' + person20[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, vydach)
    elif message.text == 'Акимов Д.В.':
        person19 = data.iloc[19]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person19)):
            bot.send_message(message.chat.id, result[i] + '  ' + person19[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите ФИО или нажмите кнопку <Назад  ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, vydach)

def priem(message):
    data = pd.read_excel("shedule2.xlsx", sheet_name='Sheet1', index_col='id')

    if message.text == 'Хусаинов Х.М.':
        person18 = data.iloc[18]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person18)):
            bot.send_message(message.chat.id, result[i] + '  ' + person18[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите Вашу фамилию и имя, или нажмите <Назад ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, priem)
    elif message.text == 'Волков Д.В.':
        person17 = data.iloc[17]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person17)):
            bot.send_message(message.chat.id, result[i] + '  ' + person17[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите Вашу фамилию и имя, или нажмите <Назад ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, priem)
    elif message.text == 'Лукин О.В.':
        person16 = data.iloc[16]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person16)):
            bot.send_message(message.chat.id, result[i] + '  ' + person16[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите Вашу фамилию и имя, или нажмите <Назад ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, priem)
    elif message.text == 'Дмитриев Иван':
        person15 = data.iloc[15]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person15)):
            bot.send_message(message.chat.id, result[i] + '  ' + person15[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите Вашу фамилию и имя, или нажмите <Назад ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, priem)
    elif message.text == 'Яббаров Л.':
        person14 = data.iloc[14]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person14)):
            bot.send_message(message.chat.id, result[i] + '  ' + person14[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите Вашу фамилию и имя, или нажмите <Назад ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, priem)
    elif message.text == 'Алберт Вечяслав':
        person13 = data.iloc[13]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person13)):
            bot.send_message(message.chat.id, result[i] + '  ' + person13[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите Вашу фамилию и имя, или нажмите <Назад ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, priem)
    elif message.text == 'Шнитов Евгений':
        person12 = data.iloc[12]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person12)):
            bot.send_message(message.chat.id, result[i] + '  ' + person12[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите Вашу фамилию и имя, или нажмите <Назад ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, priem)
    elif message.text == 'Церцеил Сергей':
        person11 = data.iloc[11]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person11)):
            bot.send_message(message.chat.id, result[i] + '  ' + person11[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите Вашу фамилию и имя, или нажмите <Назад ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, priem)
    elif message.text == 'Строганов А.И.':
        person10 = data.iloc[10]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person10)):
            bot.send_message(message.chat.id, result[i] + '  ' + person10[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите Вашу фамилию и имя, или нажмите <Назад ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, priem)
    elif message.text == 'Маринов Д.А.':
        person9 = data.iloc[9]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person9)):
            bot.send_message(message.chat.id, result[i] + '  ' + person9[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите Вашу фамилию и имя, или нажмите <Назад ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, priem)
    elif message.text == 'Кузнецов Д.':
        person8 = data.iloc[8]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person8)):
            bot.send_message(message.chat.id, result[i] + '  ' + person8[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите Вашу фамилию и имя, или нажмите <Назад ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, priem)
    elif message.text == 'Крат В.А.':
        person7 = data.iloc[7]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person7)):
            bot.send_message(message.chat.id, result[i] + '  ' + person7[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите Вашу фамилию и имя, или нажмите <Назад ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, priem)
    elif message.text == 'Кассин Александр':
        person6 = data.iloc[6]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person6)):
            bot.send_message(message.chat.id, result[i] + '  ' + person6[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите Вашу фамилию и имя, или нажмите <Назад ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, priem)
    elif message.text == 'Елфимов И.А.':
        person5 = data.iloc[5]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person5)):
            bot.send_message(message.chat.id, result[i] + '  ' + person5[i])

    elif message.text == 'Басов Михаил':
        person4 = data.iloc[4]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person4)):
            bot.send_message(message.chat.id, result[i] + '  ' + person4[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите Вашу фамилию и имя, или нажмите <Назад ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, priem)
    elif message.text == 'Абдиев Тимур':
        person3 = data.iloc[3]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person3)):
            bot.send_message(message.chat.id, result[i] + '  ' + person3[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите Вашу фамилию и имя, или нажмите <Назад ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, priem)
    elif message.text == 'Солодовников А.':
        person2 = data.iloc[2]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person2)):
            bot.send_message(message.chat.id, result[i] + '  ' + person2[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите Вашу фамилию и имя, или нажмите <Назад ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, priem)
    elif message.text == 'Смирнов С.И.':
        person1 = data.iloc[1]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person1)):
            bot.send_message(message.chat.id, result[i] + '  ' + person1[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите Вашу фамилию и имя, или нажмите <Назад ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, priem)
    elif message.text == 'Ванцевич В.Э.':
        person0 = data.iloc[0]
        # data1 = data.T
        result = data.iloc[61]
        for i in range(len(person0)):
            bot.send_message(message.chat.id, result[i] + '  ' + person0[i])
        else:
            send = bot.send_message(message.chat.id, 'Выберите Вашу фамилию и имя, или нажмите <Назад ДВАЖДЫ для перехода в главное меню')
            bot.register_next_step_handler(send, priem)


    # second.info(verbose=True)
    # second.dtypes
    # data.values
        # second = data.loc['ПАРНАС ВЫДАЧА ']
        # third = data.loc['Софийская']
        # fourth = data.loc['От.Хран.']
        # fifth = data.loc['Минеральная']
        # sixs = data.loc['Киевская']
        # seventh = data.loc['Офис']
        # print(first)
          # ,second,third,fourth,fifth,sixs,seventh)
bot.polling(none_stop=True)
