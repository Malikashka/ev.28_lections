import json
import telebot
from telebot import types
from pars import main

token = '6171389263:AAEkHmKDrH0E_9k4jjZPPr5wNPaSixlvY74'

bot = telebot.TeleBot(token)


keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Photo")
item2 = types.KeyboardButton("Description")
keyboard.add(item1, item2)

def read_news():
    with open('data.json') as file:
        data = json.load(file)
        
    return data

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEIqJJkQY_Zc8MwgiLyeGHeGWMlgpV-0gAC2A8AAkjyYEsV-8TaeHRrmC8E')
    bot.send_message(message.chat.id, f'Приветствую тебя {message.from_user.first_name}')
    print('Загружаю информацию....')
    main()
    print('Данные готовы!')
    
    data = read_news()
    
    for x in data:
        print(x)
        bot.send_message(message.chat.id, f'{x} --> *{data[x]["title"]}*', parse_mode='Markdown')
        
    bot_message = bot.send_message(message.chat.id, '🔎 Выберите номер статьи для просмотра:')
    bot.register_next_step_handler(bot_message, check_number)

def check_number(message):
    nums = [str(x) for x in range(1, 21)]
    
    if message.text not in nums:
        print(message.text)
        bot_message = bot.send_message(message.chat.id, 'Вы ввели не корректное значение! Необходимо выбрать от 1 до 20:')
        bot.register_next_step_handler(bot_message, check_number)
    else:
        data = read_news()
        bot_message = bot.send_message(message.chat.id, f'{data[message.text]["title"]} Some title news you can see Description of this news and Photo', reply_markup=keyboard)
        bot.register_next_step_handler(bot_message, show_info, message.text, data)
        
def show_info(message, number, data):
    if message.text.lower() == 'photo':
        bot.send_message(message.chat.id, data[number]['img'])
        bot_message = bot.send_message(message.chat.id, '🔎 Выберите номер статьи для просмотра:')
        bot.register_next_step_handler(bot_message, check_number)
        
    else:
        bot.send_message(message.chat.id, data[number]['desc'])
        bot_message = bot.send_message(message.chat.id, '🔎 Выберите номер статьи для просмотра:')
        bot.register_next_step_handler(bot_message, check_number)
bot.polling()