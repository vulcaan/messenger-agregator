"""
This is an echo bot.
It echoes any incoming text messages to the console.
"""

import logging

from aiogram import Bot, Dispatcher, executor, types

# TODO: find a more convenient way
f = open("D:\\KhAI\\diplom\\code\\tg-bot\\resources\\tg_bot_token.txt", "r")
API_TOKEN = f.read()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Dummy method to print a user's message to the console.
@dp.message_handler()
async def receive(message: types.Message):
    print('Message "' + message.text + '" from: ' + str(message.from_user.id))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)