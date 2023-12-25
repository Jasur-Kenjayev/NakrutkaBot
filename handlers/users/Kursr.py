from aiogram.dispatcher import FSMContext
from aiogram import types
from data.config import ADMINS
from loader import dp
from states.instaaddmoney import instaaddMoney
from keyboards.default.adminKeyboard import asosiymenu, Kursorqaga


@dp.message_handler(text="⬅️ Orqaga", state=instaaddMoney,user_id=ADMINS)
async def tarmoqio(message: types.Message, state: FSMContext):
	await state.finish()
	await message.answer("<b>🤖Asosi Paneldasiz✅</b>",reply_markup=asosiymenu)
	
	
@dp.message_handler(text="📉 RUBL KURSI",user_id=ADMINS)
async def kurs_rubl(message: types.Message):
    await message.answer("<b>📉Marhamat Rubl Kursini Kiriting👇</b>",reply_markup=Kursorqaga)
    await instaaddMoney.kurstet.set()
    
@dp.message_handler(state=instaaddMoney.kurstet)
async def insta_kurs1(message: types.Message, state: FSMContext):
    Kursr = message.text
    KursRubl = open("insta/Kurs.txt","w")
    KursRubl.write(Kursr)
    KursRubl.close()
    await message.answer("<b>📊Narxi O'zgartirildi✅</b>",reply_markup=asosiymenu)
    await state.finish()