from telegram.ext import Updater
import os.path as pt
from telegram import Update
from telegram import InputMediaPhoto
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
import random
import time
import json

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


saveUser(1,2)