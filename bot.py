import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):

	#keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Новые")
	item2 = types.KeyboardButton("Актуальные")

	markup.add(item1, item2)

	bot.reply_to(message, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, чем могу помочь?".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == 'Новые':

			markup = types.InlineKeyboardMarkup(row_width=2)
			item4 = types.InlineKeyboardButton("Срочные новости", url = 'https://vgtimes.ru/free/84605-celyy-mesyac-pochti-chto-halyavy-v-the-dark-pictures-dostupno-besplatnoe-priglashenie-dlya-druga.html', callback_data='Read')
			item5 = types.InlineKeyboardButton("Больше новостей", url = 'https://vgtimes.ru/news/84608-v-svezhih-rolikah-v-geympleem-elden-ring-pokazali-novuyu-lokaciyu-i-bossa.html', callback_data='Pereity')

			markup.add(item4, item5)

			bot.send_message(message.chat.id, "Новые новости из мира игр - https://vgtimes.ru/news/84608-v-svezhih-rolikah-v-geympleem-elden-ring-pokazali-novuyu-lokaciyu-i-bossa.html", reply_markup=markup)
		elif message.text == 'Актуальные':


			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton("Читать", url = 'https://vgtimes.ru/free/84605-celyy-mesyac-pochti-chto-halyavy-v-the-dark-pictures-dostupno-besplatnoe-priglashenie-dlya-druga.html', callback_data='Read')
			item2 = types.InlineKeyboardButton("Больше новостей", url = 'https://vgtimes.ru/news/84608-v-svezhih-rolikah-v-geympleem-elden-ring-pokazali-novuyu-lokaciyu-i-bossa.html', callback_data='Pereity')

			markup.add(item1, item2)


			bot.send_message(message.chat.id, 'Актуальные новости из мира игр - https://vgtimes.ru/news/84609-razrabotchik-vyyasnil-mozhno-li-proyti-tetris-do-konca-s-pomoschyu-ii.html', reply_markup=markup)
		else:
			bot.send_message(message.chat.id, 'Я не знаю что ответить:(')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'Read':
                bot.send_message(call.message.chat.id, 'Переходи по ссылке и чатай новости из мира игр! - https://vgtimes.ru/news/84603-na-video-pokazali-kak-vyglyadit-dying-light-2-na-ps4-i-xbox-one.html')
            elif call.data == 'Pereity':
                bot.send_message(call.message.chat.id, 'Спасибо за использоание нашего бота! - https://vgtimes.ru/news/84604-v-fevrale-windows-11-poluchit-ryad-novyh-funkciy.html')
 
            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Актуальные",
                reply_markup=None)
 
            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="Спасибо за использование нашего бота!")
 
    except Exception as e:
        print(repr(e))

bot.polling(none_stop=True)