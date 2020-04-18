import telebot
import config
import weather
from telebot import types
import pyketiki


bot = telebot.TeleBot('964615920:AAEwHybjIse8w7tBe76kuMNBZpo6ckO23vg')
markup = types.ReplyKeyboardMarkup()
markup.row('коронавирус', 'погода')
markup.row('пикеты')


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'выберите команду', reply_markup=markup)

@bot.message_handler(regexp="коронавирус")
def handle_message(message):
    bot.send_message(message.chat.id, config.Count, reply_markup=markup)
    bot.send_message(message.chat.id, config.CountNF, reply_markup=markup)

@bot.message_handler(regexp="погода")
def handle_message(message):
    bot.send_message(message.chat.id, weather.WeatherToday, reply_markup=markup)    
    bot.send_message(message.chat.id, weather.Weather, reply_markup=markup)    
    
@bot.message_handler(regexp="пикеты")
def handle_message(message):
    bot.send_message(message.chat.id, pyketiki.piket, reply_markup=markup)

if __name__ == '__main__':
    bot.polling(none_stop=True)
