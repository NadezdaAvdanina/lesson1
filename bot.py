from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def hi_user(bot, update):
    print('Вызван /start')
    bot.sendMessage(update.message.chat_id, text='Давай общаться!')


def talk_to_me(bot, update):
    print(update.message.text)
    bot.sendMessage(update.message.chat_id, update.message.text)


def show_error(bot, update, error):
    print(error)

def main():
    updater = Updater("331326206:AAFjdj7gdynL-CHP1GGEu4IzLzyjgQFiDf8")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", hi_user))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    dp.add_error_handler(show_error)
    updater.start_polling()
    updater.idle()

main()    