from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = "<b>🤖 Ushbu bot orqali barcha ijtimoiy tarmoqlarga tez va arzon narxlarda nakrutka qilishingiz mumkun\n\n🛠 Botdagi barcha nakrutkalar aftamatlashtirilgan aftamatig bot tomonidan nakrutka qilinadi\n\n✅ @OsonNakrutkaBot</b>"
    await message.answer(text)