from aiogram import types
from loader import dp, bot
from keyboards.default.tarmoq import Tarmoq, Torqaga
from aiogram.types import Message, CallbackQuery
from states.instas import Instas
from aiogram.dispatcher import FSMContext
from keyboards.inline.TKey3 import confirmation_keyboardTK3, post_callbackTK3
import requests
import json
from data.config import ADMINS
from keyboards.default.menu import Menu
	
@dp.callback_query_handler(text_contains="TKprosmotriu")
async def TKprsm1(call: CallbackQuery):
	tiktok3 = open("insta/tiktok3.txt","r")
	tiktok3i = int(tiktok3.read())
	tiktok3.close()
	await call.message.answer(f"<b>👁 1000 ta prosmotr narxi: {tiktok3i}₽\n\n🔥 Minimal buyurtma: 100 ta\n⚡️ Maksimal buyurtma: 10000000 ta\n🔴 Nakrutka Tezligi - Tez\n🚀 Joriy tezlik - (~2392-6307) soatiga\n\n👇 Marhamat kerakli miqdorni kiriting.</b>",reply_markup=Torqaga)
	await call.message.delete()
	await call.answer(cache_time=60)
	await Instas.tkint3.set()

@dp.message_handler(state=Instas.tkint3)
async def tkinput3(message: Message,state: FSMContext):
	id = message.from_user.id
	tkint3 = message.text
	await state.update_data(
		{"tkint3": tkint3}
	)
	try:
		kiriti = int(tkint3)
		if kiriti >= 100:
			balansg = open(f"balans/balans{id}.txt", "r")
			tiktok3 = open("insta/tiktok3.txt","r")
			sumasi = int(tiktok3.read())
			hisobi = float(balansg.read())
			
			donasi = sumasi / 1000
			hisobk = kiriti * donasi
			balansg.close()
			tiktok3.close()
		if hisobi >= hisobk:
			await message.answer(f"<b>⚫ TikTok Post Linkini Kiriting👇</b>",reply_markup=Torqaga)
			await Instas.tklink3.set()
		else:
			await message.answer(f"<b>💰Hisobingizda yetarli mablag' mavjud emas!</b>")
	except:
		await message.answer("<b>🔥 Minimal buyurtma: 100 ta\n⚡️ Maksimal buyurtma: 10000000 ta\n\n👇 Marhamat kerakli miqdorni kiriting.</b>")

@dp.message_handler(state=Instas.tklink3)
async def tklink3i(message: types.Message, state: FSMContext):
	tklink3 = message.text
	await state.update_data(
        {"tklink3": tklink3}
	)
	data = await state.get_data()
	tkint3 = data.get("tkint3")
	tklink3 = data.get("tklink3")
	tiktok3 = open("insta/tiktok3.txt","r")
	natija = int(tiktok3.read())
	instai = int(tkint3)
	snatija = natija / 1000
	onatija = snatija * instai
	natijalar = "%.2f" % onatija
	msg = f"<b>📇 Malumotlar to'g'riligini tekshring👇\n\n🗞 Buyurtma soni - {tkint3} ta\n🖇 Link - {tklink3}\n💰 Buyurtma narxi - {natijalar}₽</b>"
	tiktok3.close()
	await Instas.next()
	await message.answer(msg,reply_markup=confirmation_keyboardTK3)

@dp.callback_query_handler(post_callbackTK3.filter(actionTK3="postTK3"), state=Instas.tkcon3)
async def confirm_TK3(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        tkint3 = data.get("tkint3")
        tklink3 = data.get("tklink3")
        id = call.message.chat.id
        aslbalans = open(f"balans/balans{id}.txt", "r")
        tiktok3 = open("insta/tiktok3.txt","r")
        innarxi = int(tiktok3.read())
        sonib = int(tkint3)
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
        tiktok3.close()
        mykey = "badcfb3366718f41450ead89cf954878"
        url = f'https://wiq.ru/api/?key={mykey}&action=create&service=210&quantity={sonib}&link={tklink3}'
        respons = requests.get(url).json()
        resnatija = (respons["order"])
        msg = f"<b>📇Yangi buyurtma ID - {resnatija}\n📌Soni - {sonib} ta\n🖇Link - {tklink3}\n💰Narxi - {natijalar1}₽\n\n✅@NakrutkaiBot</b>"
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>📇Buyurtmangiz qabul qilindi✅\n\n🕐Tez orada buyurtmangiz to'liq bajariladi✅</b>",reply_markup=Menu)
    await bot.send_message(ADMINS[0],msg, parse_mode="HTML")
		
@dp.callback_query_handler(post_callbackTK3.filter(actionTK3="cancelTK3"), state=Instas.tkcon3)
async def cancel_TK3(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>Buyurtmalar bekor qilindi 🛑</b>",reply_markup=Menu)
    
@dp.message_handler(state=Instas.tkcon3)
async def enter_TK3(message: Message, state: FSMContext):
   await message.answer("<b>👆👆👆Quyidagi buyurtmangizni\n✅Tasdiqlang Yoki ❌Rad eting Bo'lmasa Botagi boshqa tugmalar ishlamaydi🔐</b>")
	