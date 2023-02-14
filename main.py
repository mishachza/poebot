import logging
import ast

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ChatType

from filters.filters import ReplyFilterBot
from config import APITELEGRAM
from chatgpt import gpt_dialog, COMMANDS2, shop_list, reminder_list




bot = Bot(token=APITELEGRAM)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_process(msg: types.Message):
    await bot.send_message(msg.chat.id, "Бип-Боп, Поебот Ак-ти-ви-ро-ван")



@dp.message_handler(chat_type=ChatType.PRIVATE)
async def private_dialog(msg: types.Message):
    answer = gpt_dialog(prompt=msg.text)
    await msg.answer_chat_action('typing')
    await bot.send_message(msg.chat.id, answer)

# @dp.message_handler(chat_type=ChatType.PRIVATE)
# async def private_dialog(msg: types.Message):
#     prompt = f'{COMMANDS2} \n  "{msg.text}" \n Return the keys from the dictionary that the text corresponds to'
#     answer = gpt_dialog(prompt=prompt)
#     print(answer)
#     if 1 in list(answer):
#         prompt = f'"{msg.text}" \n fill in the list: "{shop_list}" separated by commas'
#         answer = gpt_dialog(prompt=prompt)
#         add = shop_list|ast.literal_eval(answer)
#         await bot.send_message(msg.chat.id, add)
#     else:
#         await bot.send_message(msg.chat.id, answer)
    # add = COMMANDS|ast.literal_eval(answer)
    # if add == COMMANDS:
    #     answer = gpt_dialog(prompt=msg.text)
    #     await msg.answer_chat_action("typing")
    #     await bot.send_message(msg.chat.id, answer)
    # else:
    #     shop_list = add['add to shopping list']
    #     remind_list = add['set a reminder']
    #     await msg.answer_chat_action("typing")
    #     await bot.send_sticker(msg.chat.id, 'CAACAgIAAxkBAAEHhXhj2CKWt1SFFdhYrq4Wg4hfRGT8IQACJgMAArVx2gY-GQuL5xwZQC0E')


@dp.message_handler(ReplyFilterBot())
async def reply_dialog(msg: types.Message):
    prompt = msg.text
    answer = gpt_dialog(prompt=prompt)
    await msg.answer_chat_action("typing")
    await bot.send_message(msg.chat.id, answer)





if __name__ == '__main__':
    executor.start_polling(dp)