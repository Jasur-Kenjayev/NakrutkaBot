from aiogram import types
from loader import dp, bot
from keyboards.default.tarmoq import Tarmoq, Torqaga
from aiogram.types import Message, CallbackQuery
from states.instas import Instas
from aiogram.dispatcher import FSMContext
from keyboards.inline.YEkey2 import confirmation_keyboardYE2, post_callbackYE2
import requests
import json
from data.config import ADMINS
from keyboards.default.menu import Menu
from keyboards.inline.Youtubecat import categoryYElik
	
@dp.callback_query_handler(text_contains="YEeLiki")
async def YELikeh(call: CallbackQuery):
	await call.message.answer("<b>📇Marhamat keraklisini tanlang👇</b>",reply_markup=categoryYElik)
	await call.message.delete()
	await call.answer(cache_time=60)
	
@dp.callback_query_handler(text_contains="YElikinl")
async def YEliki1(call: CallbackQuery):
	YouTube2 = open("insta/YouTube2.txt","r")
	YouTube2e = int(YouTube2.read())
	YouTube2.close()
	await call.message.answer(f"<b>❤️ 1000 ta like narxi: {YouTube2e}₽\n\n🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 100000 ta\n🔴 Nakrutka Tezligi - Tez\n🚀 Joriy tezlik - (~7531-8763) Soatiga\n\n👇 Marhamat kerakli miqdorni kiriting.</b>",reply_markup=Torqaga)
	await call.message.delete()
	await call.answer(cache_time=60)
	await Instas.yeint2.set()

@dp.message_handler(state=Instas.yeint2)
async def yeinput2(message: Message,state: FSMContext):
	id = message.from_user.id
	yeint2 = message.text
	await state.update_data(
		{"yeint2": yeint2}
	)
	try:
		kiriti = int(yeint2)
		if kiriti >= 50:
			balansg = open(f"balans/balans{id}.txt", "r")
			YouTube2 = open("insta/YouTube2.txt","r")
			sumasi = int(YouTube2.read())
			hisobi = float(balansg.read())
			
			donasi = sumasi / 1000
			hisobk = kiriti * donasi
			balansg.close()
			YouTube2.close()
		if hisobi >= hisobk:
			await message.answer(f"<b>🎞 YouTube video linkini kiriting👇\n\n✅ Masalan: https://youtu.be/vqLoGp1u76w</b>",reply_markup=Torqaga)
			await Instas.yelink2.set()
		else:
			await message.answer(f"<b>💰Hisobingizda yetarli mablag' mavjud emas!</b>")
	except:
		await message.answer("<b>🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 100000 ta\n\n👇 Marhamat kerakli miqdorni kiriting.</b>")

@dp.message_handler(state=Instas.yelink2)
async def yelink2i(message: types.Message, state: FSMContext):
	yelink2 = message.text
	await state.update_data(
        {"yelink2": yelink2}
	)
	data = await state.get_data()
	yeint2 = data.get("yeint2")
	yelink2 = data.get("yelink2")
	YouTube2 = open("insta/YouTube2.txt","r")
	natija = int(YouTube2.read())
	instai = int(yeint2)
	snatija = natija / 1000
	onatija = snatija * instai
	natijalar = "%.2f" % onatija
	msg = f"<b>📇 Malumotlar to'g'riligini tekshring👇\n\n🗞 Buyurtma soni - {yeint2} ta\n🖇 Link - {yelink2}\n💰 Buyurtma narxi - {natijalar}₽</b>"
	YouTube2.close()
	await Instas.next()
	await message.answer(msg,reply_markup=confirmation_keyboardYE2)


@dp.callback_query_handler(post_callbackYE2.filter(actionYE2="postYE2"), state=Instas.yecon2)
async def confirm_YE2(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        yeint2 = data.get("yeint2")
        yelink2 = data.get("yelink2")
        id = call.message.chat.id
        aslbalans = open(f"balans/balans{id}.txt", "r")
        YouTube2 = open("insta/YouTube2.txt","r")
        innarxi = int(YouTube2.read())
        sonib = int(yeint2)
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
        YouTube2.close()
        mykey = "badcfb3366718f41450ead89cf954878"
        url = f'https://wiq.ru/api/?key={mykey}&action=create&service=508&quantity={sonib}&link={yelink2}'
        respons = requests.get(url).json()
        resnatija = (respons["order"])
        msg = f"<b>📇Yangi buyurtma ID - {resnatija}\n📌Soni - {sonib} ta\n🖇Link - {yelink2}\n💰Narxi - {natijalar1}₽\n\n✅@NakrutkaiBot</b>"
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>📇Buyurtmangiz qabul qilindi✅\n\n🕐Tez orada buyurtmangiz to'liq bajariladi✅</b>",reply_markup=Menu)
    await bot.send_message(ADMINS[0],msg, parse_mode="HTML")
		
@dp.callback_query_handler(post_callbackYE2.filter(actionYE2="cancelYE2"), state=Instas.yecon2)
async def cancel_YE2(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>Buyurtmalar bekor qilindi 🛑</b>",reply_markup=Menu)
    
@dp.message_handler(state=Instas.yecon2)
async def enter_YE2(message: Message, state: FSMContext):
   await message.answer("<b>👆👆👆Quyidagi buyurtmangizni\n✅Tasdiqlang Yoki ❌Rad eting Bo'lmasa Botagi boshqa tugmalar ishlamaydi🔐</b>")
	