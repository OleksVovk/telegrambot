import telebot
from telebot.types import Message

token = 'TOKEN'
bot = telebot.TeleBot(token)


@bot.message_handler(func=lambda message: True)
def bold(message: Message):
    bot.reply_to(message, message.text.upper())


bot.polling()

# url = "https://api.telegram.org/botTOKEN/"
#
# a = requests.get(f'{url}getMe')  # getMe - keyword
# print(a.json())
# b = requests.get(f'{url}getUpdates')
# pprint.pprint(b.json())
#
# load = {}
# load['chat_id'] = 3414751
# load['latitude'] = 50.7472
# load['longitude'] = 25.3254
# c = requests.post(f'{url}sendLocation', data=load)




