from aiogram import types
from loader import dp, bot
from keyboards.default.tarmoq import Tarmoq, Torqaga
from keyboards.inline.TRcat import categoryTrW
from aiogram.types import Message, CallbackQuery
from states.instas import Instas
from aiogram.dispatcher import FSMContext
from keyboards.inline.TRkey import confirmation_keyboardTR, post_callbackTR
import requests
import json
from data.config import ADMINS
from keyboards.default.menu import Menu
from keyboards.inline.instatanlash import TrTan

@dp.message_handler(text="🟢 Twitter")
async def TR(message:
	types.Message):
	await message.answer("<b>📲 Kerakli xizmat turini tanlang</b>",reply_markup=TrTan)
	
@dp.callback_query_handler(text_contains="TreProsmo")
async def Trprosm(call: CallbackQuery):
	await call.message.answer("<b>📇Marhamat keraklisini tanlang👇</b>",reply_markup=categoryTrW)
	await call.message.delete()
	await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains="TRprosmotri")
async def trpr(call: CallbackQuery):
	twitter = open("insta/twitter.txt","r")
	twitt = int(twitter.read())
	twitter.close()
	await call.message.answer(f"<b>👁 1000 ta prosmotr narxi: {twitt}₽\n\n🔥 Minimal buyurtma: 1000 ta\n⚡️ Maksimal buyurtma: 1000000 ta\n🔴 Nakrutka Tezligi - Sekin\n🚀 Joriy tezlik - Mavjud emas.\n✅ Haqiqi Prosmotr\n\n👇 Marhamat kerakli miqdorni kiriting.</b>",reply_markup=Torqaga)
	await call.message.delete()
	await call.answer(cache_time=60)
	await Instas.trint.set()

@dp.message_handler(state=Instas.trint)
async def trput(message: Message,state: FSMContext):
	id = message.from_user.id
	trint = message.text
	await state.update_data(
		{"trint": trint}
	)
	try:
		kiriti = int(trint)
		if kiriti >= 1000:
			balansg = open(f"balans/balans{id}.txt", "r")
			twitter = open("insta/twitter.txt","r")
			sumasi = int(twitter.read())
			hisobi = float(balansg.read())
			
			donasi = sumasi / 1000
			hisobk = kiriti * donasi
			balansg.close()
			twitter.close()
		if hisobi >= hisobk:
			await message.answer(f"<b>🟢 Twitter post linkini kiriting👇</b>",reply_markup=Torqaga)
			await Instas.trlink.set()
		else:
			await message.answer(f"<b>💰Hisobingizda yetarli mablag' mavjud emas!</b>")
	except:
		await message.answer("<b>🔥 Minimal buyurtma: 1000 ta\n⚡️ Maksimal buyurtma: 1000000 ta\n\n👇 Marhamat kerakli miqdorni kiriting.</b>")

@dp.message_handler(state=Instas.trlink)
async def trlio(message: types.Message, state: FSMContext):
	trlink = message.text
	await state.update_data(
        {"trlink": trlink}
	)
	data = await state.get_data()
	trint = data.get("trint")
	trlink = data.get("trlink")
	twitter = open("insta/twitter.txt","r")
	natija = int(twitter.read())
	instai = int(trint)
	snatija = natija / 1000
	onatija = snatija * instai
	natijalar = "%.2f" % onatija
	msg = f"<b>📇 Malumotlar to'g'riligini tekshring👇\n\n🗞 Buyurtma soni - {trint} ta\n🖇 Link - {trlink}\n💰 Buyurtma narxi - {natijalar}₽</b>"
	twitter.close()
	await Instas.next()
	await message.answer(msg,reply_markup=confirmation_keyboardTR)


@dp.callback_query_handler(post_callbackTR.filter(actionTR="postTR"), state=Instas.trcon)
async def confirm_TR(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        trint = data.get("trint")
        trlink = data.get("trlink")
        id = call.message.chat.id
        aslbalans = open(f"balans/balans{id}.txt", "r")
        twitter = open("insta/twitter.txt","r")
        innarxi = int(twitter.read())
        sonib = int(trint)
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
        twitter.close()
        mykey = "badcfb3366718f41450ead89cf954878"
        url = f'https://wiq.ru/api/?key={mykey}&action=create&service=550&quantity={sonib}&link={trlink}'
        respons = requests.get(url).json()
        resnatija = (respons["order"])
        msg = f"<b>📇Yangi buyurtma ID - {resnatija}\n📌Soni - {sonib} ta\n🖇Link - {trlink}\n💰Narxi - {natijalar1}₽\n\n✅@NakrutkaiBot</b>"
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>📇Buyurtmangiz qabul qilindi✅\n\n🕐Tez orada buyurtmangiz to'liq bajariladi✅</b>",reply_markup=Menu)
    await bot.send_message(ADMINS[0],msg, parse_mode="HTML")
		
@dp.callback_query_handler(post_callbackTR.filter(actionTR="cancelTR"), state=Instas.trcon)
async def cancel_TR(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>Buyurtmalar bekor qilindi 🛑</b>",reply_markup=Menu)
    
@dp.message_handler(state=Instas.trcon)
async def enterTr(message: Message, state: FSMContext):
   await message.answer("<b>👆👆👆Quyidagi buyurtmangizni\n✅Tasdiqlang Yoki ❌Rad eting Bo'lmasa Botagi boshqa tugmalar ishlamaydi🔐</b>")
	