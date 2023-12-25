import requests
import json
from data.config import ADMINS
from aiogram import types
from loader import dp

@dp.message_handler(text="💰API BALANS",user_id=ADMINS)
async def api_balans(message:
	types.Message):
	url = f'https://wiq.ru/api/?key=badcfb3366748f41452ead89cf954878&action=balance'
	respons = requests.get(url).json()
	resnatija = (respons["balance"])
	await message.answer(f"<b>💰Hisobingiz - {resnatija}$</b>")