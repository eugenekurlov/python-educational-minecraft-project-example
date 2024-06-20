import telebot
from telebot import types
from tabulate import tabulate
from config import TOKEN
import database as db


def telegram_bot(TOKEN):

    bot = telebot.TeleBot(TOKEN)

    @bot.message_handler(commands=['start'])
    def start(message): # the parameter keep all info about user and chat
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        start_button = types.KeyboardButton('Let\'s go')
        result_button = types.KeyboardButton('Results')
        markup.add(start_button)
        mess = f'Hello, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
        bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(message, on_click_result)

    def on_click_result(message):
        if message.text == "Let\'s go":
            bot.send_message(message.chat.id, 'Ok, let\'s get it!')

    # delete all previous messages in bot
    @bot.message_handler(commands=['clear_chat'])
    def clear_chat(message):
        a = message.message_id
        for i in range(a):
            bot.delete_message(message.chat.id, message.message_id-i-1)

    @bot.message_handler(commands=['results'])
    def results(message):
        # create buttons
        markup = types.InlineKeyboardMarkup()
        button_show = types.InlineKeyboardButton('Show results', callback_data='show_result')
        button_clear = types.InlineKeyboardButton('Clear results', callback_data='clear_result')
        markup.add(button_show, button_clear)
        bot.reply_to(message, 'What do you want?', reply_markup=markup)

    @bot.message_handler(commands=['website'])
    def website(message):
        # create button
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Minecraft documentation', url='https://www.stuffaboutcode.com/p/minecraft-api-reference.html'))
        bot.send_message(message.chat.id, "You're welcome!", reply_markup=markup)

    @bot.callback_query_handler(func=lambda callback: callback.data)
    def callback_message(callback):  # name of parameter should be the same as in lambda function above
        file_name = "records_table.csv"

        try:
            result_table = db.load_table(file_name)
            if callback.data == 'show_result':
                result_table['Total_time'] = (result_table['Total_time']
                                              .dt.total_seconds()
                                              .to_string(float_format=lambda x: '%.2f' % x, index=False)
                                              .split('\n')
                                              )
                result_table.rename(columns={'Total_time': 'Total_time'+'\n'+'in_sec'}, inplace=True)
                result_table = tabulate(result_table, headers='keys', tablefmt='psql')
                bot.send_message(callback.message.chat.id, f"<pre>{result_table}</pre>", parse_mode='html')
            if callback.data == 'clear_result':
                result_table = result_table.iloc[0:0]
                db.write_to_table(file_name, result_table)
                bot.send_message(callback.message.chat.id, "<b>All records were deleted</b>", parse_mode='html')

        except FileNotFoundError:
            bot.send_message(callback.message.chat.id, "There's no results yet")

    # keep the bot running all the time
    bot.polling(none_stop=True)


if __name__ == '__main__':
    telegram_bot(TOKEN)
