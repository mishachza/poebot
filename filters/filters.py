from aiogram import Bot, types
from aiogram.dispatcher.filters import BoundFilter
from config import APITELEGRAM

bot = Bot(token=APITELEGRAM)

class ReplyFilterBot(BoundFilter):
    async def check(self, msg: types.Message):
        try:
            if msg.reply_to_message.from_user.id == bot.id:
                return True
        except Exception:
            pass

