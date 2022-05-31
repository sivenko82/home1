import telebot
from telebot import types

bot=telebot.TeleBot("TOKEN")


@bot.message_handler(commands=['start'])
def start(message):
    mess=f"привет,{message.from_user.first_name} этот бот для пацанов введи имя своего кореша и получи его фото "
    bot.send_message(message.chat.id,mess,parse_mode="html")
@bot.message_handler()
def get_user_text(message):
    if message.text=="Рома":
        photo11=open("W210.png","rb")
        bot.send_photo(message.chat.id,photo11)
    elif message.text=="Паша":
        photo=open("imagesoasha.jpg","rb")
        bot.send_photo(message.chat.id,photo)
    elif message.text=="Киря":
        photo1=open("imageskiril.jpg","rb")
        bot.send_photo(message.chat.id,photo1)
    elif message.text == "Андрей":
        photo12 = open("575-5754587_taxi-driver-png-free-download-taxi-driver-blu.png", "rb")
        bot.send_photo(message.chat.id, photo12)
    elif message.text == "Эльдар":
        photo123 = open("Subaru-Logo-PNG-HD-Quality.png", "rb")
        bot.send_photo(message.chat.id, photo123)
    elif message.text == "Паша К":
        photo1234 = open("5________________.png", "rb")
        bot.send_photo(message.chat.id, photo1234)
    else:
        bot.send_message(message.chat.id,"ТАкого  нет ",parse_mode="html")
@bot.message_handler(content_types=["photo"])
def get_user_photo(message):
    bot.send_message(message.chat.id,"такой страшный тут")

@bot.message_handler(commands=["website"])
def website(message):
    markup=types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Главный",url="https://vk.com/id28121155"))
    bot.send_message(message.chat.id,"сайт",reply_markup=markup)


@bot.message_handler(commands=["help"])
def help(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
    website =types.KeyboardButton("веб сайт")
    start= types.KeyboardButton("START")

    markup.add(website,start)
    bot.send_message(message.chat.id,"сайт",reply_markup=markup)

bot.polling(none_stop=True)