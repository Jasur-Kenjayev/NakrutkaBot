from aiogram import types
from loader import dp, bot
from keyboards.default.tarmoq import Tarmoq, Torqaga
from aiogram.types import Message, CallbackQuery
from states.instas import Instas
from aiogram.dispatcher import FSMContext
from keyboards.inline.TKey4 import confirmation_keyboardTK4, post_callbackTK4
import requests
import json
from data.config import ADMINS
from keyboards.default.menu import Menu
from keyboards.inline.tiktokcat import categoryTKLike

@dp.callback_query_handler(text_contains="TKeLik")
async def TKlik(call: CallbackQuery):
	await call.message.answer("<b>📇Marhamat keraklisini tanlang👇</b>",reply_markup=categoryTKLike)
	await call.message.delete()
	await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains="TKLikep")
async def TKlike(call: CallbackQuery):
	tiktok4 = open("insta/tiktok4.txt","r")
	tiktok4i = int(tiktok4.read())
	tiktok4.close()
	await call.message.answer(f"<b>❤️ 1000 ta like narxi: {tiktok4i}₽\n\n🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 100000 ta\n🔴 Nakrutka Tezligi - Sekin\n🚀 Joriy tezlik - Mavjud emas\n\n👇 Marhamat kerakli miqdorni kiriting.</b>",reply_markup=Torqaga)
	await call.message.delete()
	await call.answer(cache_time=60)
	await Instas.tkint4.set()

@dp.message_handler(state=Instas.tkint4)
async def tkinput4(message: Message,state: FSMContext):
	id = message.from_user.id
	tkint4 = message.text
	await state.update_data(
		{"tkint4": tkint4}
	)
	try:
		kiriti = int(tkint4)
		if kiriti >= 50:
			balansg = open(f"balans/balans{id}.txt", "r")
			tiktok4 = open("insta/tiktok4.txt","r")
			sumasi = int(tiktok4.read())
			hisobi = float(balansg.read())
			
			donasi = sumasi / 1000
			hisobk = kiriti * donasi
			balansg.close()
			tiktok4.close()
		if hisobi >= hisobk:
			await message.answer(f"<b>⚫ TikTok Post Linkini Kiriting👇</b>",reply_markup=Torqaga)
			await Instas.tklink4.set()
		else:
			await message.answer(f"<b>💰Hisobingizda yetarli mablag' mavjud emas!</b>")
	except:
		await message.answer("<b>🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 100000 ta\n\n👇 Marhamat kerakli miqdorni kiriting.</b>")

@dp.message_handler(state=Instas.tklink4)
async def tklink4i(message: types.Message, state: FSMContext):
	tklink4 = message.text
	await state.update_data(
        {"tklink4": tklink4}
	)
	data = await state.get_data()
	tkint4 = data.get("tkint4")
	tklink4 = data.get("tklink4")
	tiktok4 = open("insta/tiktok4.txt","r")
	natija = int(tiktok4.read())
	instai = int(tkint4)
	snatija = natija / 1000
	onatija = snatija * instai
	natijalar = "%.2f" % onatija
	msg = f"<b>📇 Malumotlar to'g'riligini tekshring👇\n\n🗞 Buyurtma soni - {tkint4} ta\n🖇 Link - {tklink4}\n💰 Buyurtma narxi - {natijalar}₽</b>"
	tiktok4.close()
	await Instas.next()
	await message.answer(msg,reply_markup=confirmation_keyboardTK4)

@dp.callback_query_handler(post_callbackTK4.filter(actionTK4="postTK4"), state=Instas.tkcon4)
async def confirm_TK4(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        tkint4 = data.get("tkint4")
        tklink4 = data.get("tklink4")
        id = call.message.chat.id
        aslbalans = open(f"balans/balans{id}.txt", "r")
        tiktok4 = open("insta/tiktok4.txt","r")
        innarxi = int(tiktok4.read())
        sonib = int(tkint4)
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
        tiktok4.close()
        mykey = "badcfb3366718f41450ead89cf954878"
        url = f'https://wiq.ru/api/?key={mykey}&action=create&service=306&quantity={sonib}&link={tklink4}'
        respons = requests.get(url).json()
        resnatija = (respons["order"])
        msg = f"<b>📇Yangi buyurtma ID - {resnatija}\n📌Soni - {sonib} ta\n🖇Link - {tklink4}\n💰Narxi - {natijalar1}₽\n\n✅@NakrutkaiBot</b>"
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>📇Buyurtmangiz qabul qilindi✅\n\n🕐Tez orada buyurtmangiz to'liq bajariladi✅</b>",reply_markup=Menu)
    await bot.send_message(ADMINS[0],msg, parse_mode="HTML")
		
@dp.callback_query_handler(post_callbackTK4.filter(actionTK4="cancelTK4"), state=Instas.tkcon4)
async def cancel_TK4(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>Buyurtmalar bekor qilindi 🛑</b>",reply_markup=Menu)
    
@dp.message_handler(state=Instas.tkcon4)
async def enter_TK4(message: Message, state: FSMContext):
   await message.answer("<b>👆👆👆Quyidagi buyurtmangizni\n✅Tasdiqlang Yoki ❌Rad eting Bo'lmasa Botagi boshqa tugmalar ishlamaydi🔐</b>")
	