from aiogram import types
from loader import dp, bot
from keyboards.default.tarmoq import Tarmoq, Torqaga
from aiogram.types import Message, CallbackQuery
from states.instas import Instas
from aiogram.dispatcher import FSMContext
from keyboards.inline.TKey5 import confirmation_keyboardTK5, post_callbackTK5
import requests
import json
from data.config import ADMINS
from keyboards.default.menu import Menu


@dp.callback_query_handler(text_contains="TKLayk")
async def TKlike1(call: CallbackQuery):
	tiktok5 = open("insta/tiktok5.txt","r")
	tiktok5i = int(tiktok5.read())
	tiktok5.close()
	await call.message.answer(f"<b>❤️ 1000 ta like narxi: {tiktok5i}₽\n\n🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 20000 ta\n🔴 Nakrutka Tezligi - Sekin\n🚀 Joriy tezlik - Mavjud emas\n\n👇 Marhamat kerakli miqdorni kiriting.</b>",reply_markup=Torqaga)
	await call.message.delete()
	await call.answer(cache_time=60)
	await Instas.tkint5.set()

@dp.message_handler(state=Instas.tkint5)
async def tkinput5(message: Message,state: FSMContext):
	id = message.from_user.id
	tkint5 = message.text
	await state.update_data(
		{"tkint5": tkint5}
	)
	try:
		kiriti = int(tkint5)
		if kiriti >= 50:
			balansg = open(f"balans/balans{id}.txt", "r")
			tiktok5 = open("insta/tiktok5.txt","r")
			sumasi = int(tiktok5.read())
			hisobi = float(balansg.read())
			
			donasi = sumasi / 1000
			hisobk = kiriti * donasi
			balansg.close()
			tiktok5.close()
		if hisobi >= hisobk:
			await message.answer(f"<b>⚫ TikTok Post Linkini Kiriting👇</b>",reply_markup=Torqaga)
			await Instas.tklink5.set()
		else:
			await message.answer(f"<b>💰Hisobingizda yetarli mablag' mavjud emas!</b>")
	except:
		await message.answer("<b>🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 20000 ta\n\n👇 Marhamat kerakli miqdorni kiriting.</b>")

@dp.message_handler(state=Instas.tklink5)
async def tklink5i(message: types.Message, state: FSMContext):
	tklink5 = message.text
	await state.update_data(
        {"tklink5": tklink5}
	)
	data = await state.get_data()
	tkint5 = data.get("tkint5")
	tklink5 = data.get("tklink5")
	tiktok5 = open("insta/tiktok5.txt","r")
	natija = int(tiktok5.read())
	instai = int(tkint5)
	snatija = natija / 1000
	onatija = snatija * instai
	natijalar = "%.2f" % onatija
	msg = f"<b>📇 Malumotlar to'g'riligini tekshring👇\n\n🗞 Buyurtma soni - {tkint5} ta\n🖇 Link - {tklink5}\n💰 Buyurtma narxi - {natijalar}₽</b>"
	tiktok5.close()
	await Instas.next()
	await message.answer(msg,reply_markup=confirmation_keyboardTK5)

@dp.callback_query_handler(post_callbackTK5.filter(actionTK5="postTK5"), state=Instas.tkcon5)
async def confirm_TK5(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        tkint5 = data.get("tkint5")
        tklink5 = data.get("tklink5")
        id = call.message.chat.id
        aslbalans = open(f"balans/balans{id}.txt", "r")
        tiktok5 = open("insta/tiktok5.txt","r")
        innarxi = int(tiktok5.read())
        sonib = int(tkint5)
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
        tiktok5.close()
        mykey = "badcfb3366718f41450ead89cf954878"
        url = f'https://wiq.ru/api/?key={mykey}&action=create&service=253&quantity={sonib}&link={tklink5}'
        respons = requests.get(url).json()
        resnatija = (respons["order"])
        msg = f"<b>📇Yangi buyurtma ID - {resnatija}\n📌Soni - {sonib} ta\n🖇Link - {tklink5}\n💰Narxi - {natijalar1}₽\n\n✅@NakrutkaiBot</b>"
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>📇Buyurtmangiz qabul qilindi✅\n\n🕐Tez orada buyurtmangiz to'liq bajariladi✅</b>",reply_markup=Menu)
    await bot.send_message(ADMINS[0],msg, parse_mode="HTML")
		
@dp.callback_query_handler(post_callbackTK5.filter(actionTK5="cancelTK5"), state=Instas.tkcon5)
async def cancel_TK5(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>Buyurtmalar bekor qilindi 🛑</b>",reply_markup=Menu)
    
@dp.message_handler(state=Instas.tkcon5)
async def enter_TK5(message: Message, state: FSMContext):
   await message.answer("<b>👆👆👆Quyidagi buyurtmangizni\n✅Tasdiqlang Yoki ❌Rad eting Bo'lmasa Botagi boshqa tugmalar ishlamaydi🔐</b>")
	