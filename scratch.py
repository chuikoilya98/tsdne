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
    with open(pt.abspath('data/users.json'), 'r') as file:
        data = json.load(file)
        users = data['users']
        
        for u in users:
            if userId == u['id'] :
                print(False)
            else:
                newUser = {
                    'name' : name,
                    'id' : userId
                }

                users.append(newUser)

                print(users)

                with open(pt.abspath('data/users.json'), 'w') as f :
                    data = {
                        'users' : users
                    }
                    result = json.dumps(data)
                    f.write(result)



saveUser(2,5)