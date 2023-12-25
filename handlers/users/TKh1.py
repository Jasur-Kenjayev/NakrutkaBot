from aiogram import types
from loader import dp, bot
from keyboards.default.tarmoq import Tarmoq, Torqaga
from aiogram.types import Message, CallbackQuery
from states.instas import Instas
from aiogram.dispatcher import FSMContext
from keyboards.inline.TKey1 import confirmation_keyboardTK1, post_callbackTK1
import requests
import json
from data.config import ADMINS
from keyboards.default.menu import Menu

@dp.callback_query_handler(text_contains="TKobnachio")
async def TKobunach1(call: CallbackQuery):
	tiktok1 = open("insta/tiktok1.txt","r")
	tiktok1i = int(tiktok1.read())
	tiktok1.close()
	await call.message.answer(f"<b>👤 1000 ta obunachi narxi: {tiktok1i}₽\n\n🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 50000 ta\n🔴 Nakrutka Tezligi - Tez\n🚀 Joriy tezlik - (~115-206) Soatiga.\n\n👇 Marhamat kerakli miqdorni kiriting.</b>",reply_markup=Torqaga)
	await call.message.delete()
	await call.answer(cache_time=60)
	await Instas.tkint1.set()

@dp.message_handler(state=Instas.tkint1)
async def tkinput1(message: Message,state: FSMContext):
	id = message.from_user.id
	tkint1 = message.text
	await state.update_data(
		{"tkint1": tkint1}
	)
	try:
		kiriti = int(tkint1)
		if kiriti >= 50:
			balansg = open(f"balans/balans{id}.txt", "r")
			tiktok1 = open("insta/tiktok1.txt","r")
			sumasi = int(tiktok1.read())
			hisobi = float(balansg.read())
			
			donasi = sumasi / 1000
			hisobk = kiriti * donasi
			balansg.close()
			tiktok1.close()
		if hisobi >= hisobk:
			await message.answer(f"<b>⚫ TikTok profil linkini kiriting👇\n\n✅ Masalan: 1.we_wolf</b>",reply_markup=Torqaga)
			await Instas.tklink1.set()
		else:
			await message.answer(f"<b>💰Hisobingizda yetarli mablag' mavjud emas!</b>")
	except:
		await message.answer("<b>🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 50000 ta\n\n👇 Marhamat kerakli miqdorni kiriting.</b>")

@dp.message_handler(state=Instas.tklink1)
async def tklink1ui(message: types.Message, state: FSMContext):
	tklink1 = message.text
	await state.update_data(
        {"tklink1": tklink1}
	)
	data = await state.get_data()
	tkint1 = data.get("tkint1")
	tklink1 = data.get("tklink1")
	tiktok1 = open("insta/tiktok1.txt","r")
	natija = int(tiktok1.read())
	instai = int(tkint1)
	snatija = natija / 1000
	onatija = snatija * instai
	natijalar = "%.2f" % onatija
	msg = f"<b>📇 Malumotlar to'g'riligini tekshring👇\n\n🗞 Buyurtma soni - {tkint1} ta\n🖇 Link - {tklink1}\n💰 Buyurtma narxi - {natijalar}₽</b>"
	tiktok1.close()
	await Instas.next()
	await message.answer(msg,reply_markup=confirmation_keyboardTK1)

@dp.callback_query_handler(post_callbackTK1.filter(actionTK1="postTK1"), state=Instas.tkcon1)
async def confirm_TK1(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        tkint1 = data.get("tkint1")
        tklink1 = data.get("tklink1")
        id = call.message.chat.id
        aslbalans = open(f"balans/balans{id}.txt", "r")
        tiktok1 = open("insta/tiktok1.txt","r")
        innarxi = int(tiktok1.read())
        sonib = int(tkint1)
        asbalns = float(aslbalans.read())
        natijax = innarxi / 1000
        natijab = natijax * sonib
        natijalar1 = "%.2f" % natijab
        nato = float(natijalar1)
        natijabalans = asbalns - nato
        sungiN = str(natijabalans)
        adbalns = open(f"balans/balans{id}.txt", "w")
        adbalns.write(sungiN)
        adbalns.close()
        aslbalans.close()
        tiktok1.close()
        mykey = "badcfb3366718f41450ead89cf954878"
        url = f'https://wiq.ru/api/?key={mykey}&action=create&service=252&quantity={sonib}&link={tklink1}'
        respons = requests.get(url).json()
        resnatija = (respons["order"])
        msg = f"<b>📇Yangi buyurtma ID - {resnatija}\n📌Soni - {sonib} ta\n🖇Link - {tklink1}\n💰Narxi - {natijalar1}₽\n\n✅@NakrutkaiBot</b>"
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>📇Buyurtmangiz qabul qilindi✅\n\n🕐Tez orada buyurtmangiz to'liq bajariladi✅</b>",reply_markup=Menu)
    await bot.send_message(ADMINS[0],msg, parse_mode="HTML")
		
@dp.callback_query_handler(post_callbackTK1.filter(actionTK1="cancelTK1"), state=Instas.tkcon1)
async def cancel_TK1(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>Buyurtmalar bekor qilindi 🛑</b>",reply_markup=Menu)
    
@dp.message_handler(state=Instas.tkcon1)
async def enter_TK1(message: Message, state: FSMContext):
   await message.answer("<b>👆👆👆Quyidagi buyurtmangizni\n✅Tasdiqlang Yoki ❌Rad eting Bo'lmasa Botagi boshqa tugmalar ishlamaydi🔐</b>")
	