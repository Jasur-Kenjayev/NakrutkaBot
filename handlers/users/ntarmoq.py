from aiogram import types
from loader import dp
from keyboards.default.tarmoq import Tarmoq
from keyboards.default.menu import Menu

@dp.message_handler(text="❤️ Nakrutka")
async def tarmoqlar(message:
	types.Message):
	await message.answer("<b>🌐 Kerakli ijtimoiy tarmoqni tanlang👇</b>",reply_markup=Tarmoq)

@dp.message_handler(text="🔚 Orqaga")
async def orqaga(message:
	types.Message):
	await message.answer("<b>🖥 Asosiy menyuga qaytdingiz✅</b>",reply_markup=Menu)
	