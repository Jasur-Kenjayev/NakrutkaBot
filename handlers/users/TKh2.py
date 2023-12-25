from aiogram import types
from loader import dp, bot
from keyboards.default.tarmoq import Tarmoq, Torqaga
from aiogram.types import Message, CallbackQuery
from states.instas import Instas
from aiogram.dispatcher import FSMContext
from keyboards.inline.TKey2 import confirmation_keyboardTK2, post_callbackTK2
import requests
import json
from data.config import ADMINS
from keyboards.default.menu import Menu
from keyboards.inline.tiktokcat import categoryTKPros 

@dp.callback_query_handler(text_contains="TKpProsmo")
async def TKprosv(call: CallbackQuery):
	await call.message.answer("<b>📇Marhamat keraklisini tanlang👇</b>",reply_markup=categoryTKPros)
	await call.message.delete()
	await call.answer(cache_time=60)
	
@dp.callback_query_handler(text_contains="TKProsmotri")
async def TKprsm(call: CallbackQuery):
	tiktok2 = open("insta/tiktok2.txt","r")
	tiktok2i = int(tiktok2.read())
	tiktok2.close()
	await call.message.answer(f"<b>👁 1000 ta prosmotr narxi: {tiktok2i}₽\n\n🔥 Minimal buyurtma: 500 ta\n⚡️ Maksimal buyurtma: 100000000 ta\n🔴 Nakrutka Tezligi - Sekin\n🚀 Joriy tezlik - Mavjud emas.\n\n👇 Marhamat kerakli miqdorni kiriting.</b>",reply_markup=Torqaga)
	await call.message.delete()
	await call.answer(cache_time=60)
	await Instas.tkint2.set()

@dp.message_handler(state=Instas.tkint2)
async def tkinput2(message: Message,state: FSMContext):
	id = message.from_user.id
	tkint2 = message.text
	await state.update_data(
		{"tkint2": tkint2}
	)
	try:
		kiriti = int(tkint2)
		if kiriti >= 500:
			balansg = open(f"balans/balans{id}.txt", "r")
			tiktok2 = open("insta/tiktok2.txt","r")
			sumasi = int(tiktok2.read())
			hisobi = float(balansg.read())
			
			donasi = sumasi / 1000
			hisobk = kiriti * donasi
			balansg.close()
			tiktok2.close()
		if hisobi >= hisobk:
			await message.answer(f"<b>⚫ TikTok Post Linkini Kiriting👇</b>",reply_markup=Torqaga)
			await Instas.tklink2.set()
		else:
			await message.answer(f"<b>💰Hisobingizda yetarli mablag' mavjud emas!</b>")
	except:
		await message.answer("<b>🔥 Minimal buyurtma: 500 ta\n⚡️ Maksimal buyurtma: 100000000 ta\n\n👇 Marhamat kerakli miqdorni kiriting.</b>")

@dp.message_handler(state=Instas.tklink2)
async def tklink2i(message: types.Message, state: FSMContext):
	tklink2 = message.text
	await state.update_data(
        {"tklink2": tklink2}
	)
	data = await state.get_data()
	tkint2 = data.get("tkint2")
	tklink2 = data.get("tklink2")
	tiktok2 = open("insta/tiktok2.txt","r")
	natija = int(tiktok2.read())
	instai = int(tkint2)
	snatija = natija / 1000
	onatija = snatija * instai
	natijalar = "%.2f" % onatija
	msg = f"<b>📇 Malumotlar to'g'riligini tekshring👇\n\n🗞 Buyurtma soni - {tkint2} ta\n🖇 Link - {tklink2}\n💰 Buyurtma narxi - {natijalar}₽</b>"
	tiktok2.close()
	await Instas.next()
	await message.answer(msg,reply_markup=confirmation_keyboardTK2)

@dp.callback_query_handler(post_callbackTK2.filter(actionTK2="postTK2"), state=Instas.tkcon2)
async def confirm_TK2(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        tkint2 = data.get("tkint2")
        tklink2 = data.get("tklink2")
        id = call.message.chat.id
        aslbalans = open(f"balans/balans{id}.txt", "r")
        tiktok2 = open("insta/tiktok2.txt","r")
        innarxi = int(tiktok2.read())
        sonib = int(tkint2)
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
        tiktok2.close()
        mykey = "badcfb3366718f41450ead89cf954878"
        url = f'https://wiq.ru/api/?key={mykey}&action=create&service=310&quantity={sonib}&link={tklink2}'
        respons = requests.get(url).json()
        resnatija = (respons["order"])
        msg = f"<b>📇Yangi buyurtma ID - {resnatija}\n📌Soni - {sonib} ta\n🖇Link - {tklink2}\n💰Narxi - {natijalar1}₽\n\n✅@NakrutkaiBot</b>"
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>📇Buyurtmangiz qabul qilindi✅\n\n🕐Tez orada buyurtmangiz to'liq bajariladi✅</b>",reply_markup=Menu)
    await bot.send_message(ADMINS[0],msg, parse_mode="HTML")
		
@dp.callback_query_handler(post_callbackTK2.filter(actionTK2="cancelTK2"), state=Instas.tkcon2)
async def cancel_TK2(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>Buyurtmalar bekor qilindi 🛑</b>",reply_markup=Menu)
    
@dp.message_handler(state=Instas.tkcon2)
async def enter_TK2(message: Message, state: FSMContext):
   await message.answer("<b>👆👆👆Quyidagi buyurtmangizni\n✅Tasdiqlang Yoki ❌Rad eting Bo'lmasa Botagi boshqa tugmalar ishlamaydi🔐</b>")
	