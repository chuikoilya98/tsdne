from telegram.ext import Updater
import os.path as pt
from telegram import Update
from telegram import InputMediaPhoto
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
import random
import time
import json

token = '5299421123:AAF4srew9eNzm6wcWR8a-7wxQ--t6jLJE5o'
updater = Updater(token= token, use_context=True)
dispatcher = updater.dispatcher

def getRandom(count=10) :
    with open(pt.abspath('result.txt'), 'r') as file:
        links = []
        for row in file:
            name = row.replace('\n', '')
            links.append(name)
        
        result = []
        for i in range(count) :
            sn = random.choice(links)
            if sn in result :
                sn = random.choice(links)
                media = InputMediaPhoto(media=sn)
                result.append(media)
            else :
                media = InputMediaPhoto(media=sn)
                result.append(media)

        return result

def saveUser(name, userId) :
    with open(pt.abspath('users.json'), 'r') as file:
        data = json.load(file)
        users = data['users']

        newUser = {
            'name' : name,
            'id' : userId
        }

        users.append(newUser)

        with open(pt.abspath('users.json'), 'w') as f :
            data = {
                'users' : users
            }
            result = json.dumps(data)
            f.write(result)

def start(update: Update, context: CallbackContext) :
    info = update.message.from_user
    name = info.first_name
    lname = info.last_name
    userId= info.id
    #saveUser(name, userId)
    context.bot.send_message(chat_id='331392389', text=f'User {name}  {lname} started AI bot')
    context.bot.send_message(chat_id=update.effective_chat.id, text="""Привет! Спасибо за то что проявил интерес к теме генеративных кроссовок
@myataya_mayka - канал автора проекта

Для генерации 10 пар нажми на /generate""")

def generate(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Генерирую...")
    time.sleep(2)
    media = getRandom()
    context.bot.send_media_group(chat_id=update.effective_chat.id,media = media)
    time.sleep(4)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Используй команду /generate чтобы получить еще AI-кроссовок")

if __name__ == '__main__' :
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    gen_handler = CommandHandler('generate', generate)
    dispatcher.add_handler(gen_handler)

    updater.start_polling()