import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menu import Menu
from data.config import ADMINS
from loader import dp, db, bot
from aiogram.types import ParseMode


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    id = message.from_user.id
    try:
    	balansi = open(f"balans/balans{id}.txt", "r")
    	balansi.close()
    	await message.answer(f"*👋 Assalomu alaykum hurmatli {message.from_user.full_name}\n\n🤖 Ushbu bot orqali barcha ijtimoiy tarmoqlarga Obunachi Prosmotr Like Nakrutka qilish mumkun asosisi tez va arzon narxda va sifatli nakrutka qilishingiz mumkun!\n\n✅ Botdagi barcha nakrutka xizmatlari aftamatlashtirilgan aftamatig bot tomonidan nakrutka qilinadi tez va qulay mijozlar uchun👇*",parse_mode=ParseMode.MARKDOWN,reply_markup=Menu)
    except:
    	balans = open(f"balans/balans{id}.txt", "w")
    	baci = ('0')
    	balans.write(baci)
    	balans.close()
    	await message.answer(f"*👋 Assalomu alaykum hurmatli {message.from_user.full_name}\n\n🤖 Ushbu bot orqali barcha ijtimoiy tarmoqlarga Obunachi Prosmotr Like Nakrutka qilish mumkun asosisi tez va arzon narxda va sifatli nakrutka qilishingiz mumkun!\n\n✅ Botdagi barcha nakrutka xizmatlari aftamatlashtirilgan aftamatig bot tomonidan nakrutka qilinadi tez va qulay mijozlar uchun👇*",parse_mode=ParseMode.MARKDOWN,reply_markup=Menu)
	   
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)
    # Adminga xabar beramiz
    count = db.count_users()[0]
    msg = f"*{message.from_user.full_name} 💡Bazaga Yangi 👤Foydalanuvchi ➕Qo'shildi. Bazada {count} ta Foydalanuvchi Bor✅*"
    await bot.send_message(chat_id=ADMINS[0], text=msg,parse_mode=ParseMode.MARKDOWN)
    await bot.send_message(chat_id=ADMINS[1], text=msg,parse_mode=ParseMode.MARKDOWN)