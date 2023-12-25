from aiogram import types
from loader import dp, bot
from keyboards.default.tarmoq import Tarmoq, Torqaga
from aiogram.types import Message, CallbackQuery
from states.instas import Instas
from aiogram.dispatcher import FSMContext
from keyboards.inline.TGkey4 import confirmation_keyboardTG4, post_callbackTG4
import requests
import json
from data.config import ADMINS
from keyboards.default.menu import Menu

@dp.callback_query_handler(text_contains="tgobunach5")
async def tgobunachii5(call: CallbackQuery):
	TGobunachif4 = open("insta/TGobunachi4.txt","r")
	TGobunachisi4 = int(TGobunachif4.read())
	TGobunachif4.close()
	await call.message.answer(f"<b>👤 1000 ta obunachi narxi: {TGobunachisi4}₽\n\n🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 300000 ta\n🔴 Nakrutka Tezligi - Tez\n🚀 Joriy tezlik - (~3390-4282) soatiga\n\n👇 Marhamat kerakli miqdorni kiriting.</b>",reply_markup=Torqaga)
	await call.message.delete()
	await call.answer(cache_time=60)
	await Instas.tgint4.set()

@dp.message_handler(state=Instas.tgint4)
async def tginput(message: Message,state: FSMContext):
	id = message.from_user.id
	tgint4 = message.text
	await state.update_data(
		{"tgint4": tgint4}
	)
	try:
		kiriti = int(tgint4)
		if kiriti >= 50:
			balansg = open(f"balans/balans{id}.txt", "r")
			TGobunachif4 = open("insta/TGobunachi4.txt","r")
			sumasi = int(TGobunachif4.read())
			hisobi = float(balansg.read())
		
			donasi = sumasi / 1000
			hisobk = kiriti * donasi
			balansg.close()
			TGobunachif4.close()
		if hisobi >= hisobk:
			await message.answer(f"<b>🔵 Telegram kanal yoki grupa linkni kiriting👇\n\n✅ Masalan: https://t.me/Python_Koderuz</b>",reply_markup=Torqaga)
			await Instas.tglink4.set()
		else:
			await message.answer(f"<b>💰Hisobingizda yetarli mablag' mavjud emas!</b>")
	except:
		await message.answer("<b>🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 300000 ta\n\n👇 Marhamat kerakli miqdorni kiriting.</b>")

@dp.message_handler(state=Instas.tglink4)
async def tglinki4(message: types.Message, state: FSMContext):
	tglink4 = message.text
	await state.update_data(
        {"tglink4": tglink4}
	)
	data = await state.get_data()
	tgint4 = data.get("tgint4")
	tglink4 = data.get("tglink4")
	TGobunachif4 = open("insta/TGobunachi4.txt","r")
	natija = int(TGobunachif4.read())
	instai = int(tgint4)
	snatija = natija / 1000
	onatija = snatija * instai
	natijalar = "%.2f" % onatija
	msg = f"<b>📇 Malumotlar to'g'riligini tekshring👇\n\n🗞 Buyurtma soni - {tgint4} ta\n🖇 Link - {tglink4}\n💰 Buyurtma narxi - {natijalar}₽</b>"
	TGobunachif4.close()
	await Instas.next()
	await message.answer(msg,reply_markup=confirmation_keyboardTG4)


@dp.callback_query_handler(post_callbackTG4.filter(actionTG4="postTG4"), state=Instas.tgcon4)
async def confirm_TG4(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        tgint4 = data.get("tgint4")
        tglink4 = data.get("tglink4")
        id = call.message.chat.id
        aslbalans = open(f"balans/balans{id}.txt", "r")
        TGobunachif4 = open("insta/TGobunachi4.txt","r")
        innarxi = int(TGobunachif4.read())
        sonib = int(tgint4)
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
        TGobunachif4.close()
        mykey = "badcfb3366718f41450ead89cf954878"
        url = f'https://wiq.ru/api/?key={mykey}&action=create&service=414&quantity={sonib}&link={tglink4}'
        respons = requests.get(url).json()
        resnatija = (respons["order"])
        msg = f"<b>📇Yangi buyurtma ID - {resnatija}\n📌Soni - {sonib} ta\n🖇Link - {tglink4}\n💰Narxi - {natijalar1}₽\n\n✅@NakrutkaiBot</b>"
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>📇Buyurtmangiz qabul qilindi✅\n\n🕐Tez orada buyurtmangiz to'liq bajariladi✅</b>",reply_markup=Menu)
    await bot.send_message(ADMINS[0],msg, parse_mode="HTML")
		
@dp.callback_query_handler(post_callbackTG4.filter(actionTG4="cancelTG4"), state=Instas.tgcon4)
async def cancel_TG4(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>Buyurtmalar bekor qilindi 🛑</b>",reply_markup=Menu)
    
@dp.message_handler(state=Instas.tgcon4)
async def enter_TG4(message: Message, state: FSMContext):
   await message.answer("<b>👆👆👆Quyidagi buyurtmangizni\n✅Tasdiqlang Yoki ❌Rad eting Bo'lmasa Botagi boshqa tugmalar ishlamaydi🔐</b>")
	