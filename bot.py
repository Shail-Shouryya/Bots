from config import token
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
                    
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters
import requests
import re
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url
# def bop(bot, update):
def talk (update, context):
    url = get_url()
    # chat_id = update.message.chat_id
    # bot.send_photo(chat_id=chat_id, photo=url)
    context.bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")
def bop (update, context):
    url = get_url()
    # chat_id = update.message.chat_id
    # bot.send_photo(chat_id=chat_id, photo=url)
    context.bot.send_photo(chat_id=update.message.chat_id, photo=url)
def echo(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text=update.message.text)
def main():
    updater = Updater(token=token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('talk', talk))
    dp.add_handler(CommandHandler('bop', bop))
    echo_handler = MessageHandler(Filters.text, echo)
    dp.add_handler(echo_handler)
    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()