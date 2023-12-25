from aiogram import types
from loader import dp, bot
from keyboards.default.tarmoq import Tarmoq, Torqaga
from keyboards.inline.likeecat import categoryLeP
from aiogram.types import Message, CallbackQuery
from states.instas import Instas
from aiogram.dispatcher import FSMContext
from keyboards.inline.LEkey1 import confirmation_keyboardLE1, post_callbackLE1
import requests
import json
from data.config import ADMINS
from keyboards.default.menu import Menu

@dp.callback_query_handler(text_contains="LeeProsmo")
async def LEprosmotr(call: CallbackQuery):
	await call.message.answer("<b>📇Marhamat keraklisini tanlang👇</b>",reply_markup=categoryLeP)
	await call.message.delete()
	await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains="LEprosmotri")
async def leporosmotr(call: CallbackQuery):
	likee1 = open("insta/likee1.txt","r")
	like1 = int(likee1.read())
	likee1.close()
	await call.message.answer(f"<b>👁 1000 ta prosmotr narxi: {like1}₽\n\n🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 10000 ta\n🔴 Nakrutka Tezligi - Sekin\n🚀 Joriy tezlik - Mavjud emas.\n✅ Haqiqi Obunachilar Ko'radi\n\n👇 Marhamat kerakli miqdorni kiriting.</b>",reply_markup=Torqaga)
	await call.message.delete()
	await call.answer(cache_time=60)
	await Instas.leint1.set()

@dp.message_handler(state=Instas.leint1)
async def leinput1(message: Message,state: FSMContext):
	id = message.from_user.id
	leint1 = message.text
	await state.update_data(
		{"leint1": leint1}
	)
	try:
		kiriti = int(leint1)
		if kiriti >= 50:
			balansg = open(f"balans/balans{id}.txt", "r")
			likee1 = open("insta/likee1.txt","r")
			sumasi = int(likee1.read())
			hisobi = float(balansg.read())
			
			donasi = sumasi / 1000
			hisobk = kiriti * donasi
			balansg.close()
			likee1.close()
		if hisobi >= hisobk:
			await message.answer(f"<b>🟠 Likee post linkini kiriting👇</b>",reply_markup=Torqaga)
			await Instas.LElikn1.set()
		else:
			await message.answer(f"<b>💰Hisobingizda yetarli mablag' mavjud emas!</b>")
	except:
		await message.answer("<b>🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 10000 ta\n\n👇 Marhamat kerakli miqdorni kiriting.</b>")

@dp.message_handler(state=Instas.LElikn1)
async def LElikn1ui(message: types.Message, state: FSMContext):
	LElikn1 = message.text
	await state.update_data(
        {"LElikn1": LElikn1}
	)
	data = await state.get_data()
	leint1 = data.get("leint1")
	LElikn1 = data.get("LElikn1")
	likee1 = open("insta/likee1.txt","r")
	natija = int(likee1.read())
	instai = int(leint1)
	snatija = natija / 1000
	onatija = snatija * instai
	natijalar = "%.2f" % onatija
	msg = f"<b>📇 Malumotlar to'g'riligini tekshring👇\n\n🗞 Buyurtma soni - {leint1} ta\n🖇 Link - {LElikn1}\n💰 Buyurtma narxi - {natijalar}₽</b>"
	likee1.close()
	await Instas.next()
	await message.answer(msg,reply_markup=confirmation_keyboardLE1)


@dp.callback_query_handler(post_callbackLE1.filter(actionLE1="postLE1"), state=Instas.lecon1)
async def confirm_LE1(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        leint1 = data.get("leint1")
        LElikn1 = data.get("LElikn1")
        id = call.message.chat.id
        aslbalans = open(f"balans/balans{id}.txt", "r")
        likee1 = open("insta/likee1.txt","r")
        innarxi = int(likee1.read())
        sonib = int(leint1)
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
        likee1.close()
        mykey = "badcfb3366718f41450ead89cf954878"
        url = f'https://wiq.ru/api/?key={mykey}&action=create&service=703&quantity={sonib}&link={LElikn1}'
        respons = requests.get(url).json()
        resnatija = (respons["order"])
        msg = f"<b>📇Yangi buyurtma ID - {resnatija}\n📌Soni - {sonib} ta\n🖇Link - {LElikn1}\n💰Narxi - {natijalar1}₽\n\n✅@NakrutkaiBot</b>"
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>📇Buyurtmangiz qabul qilindi✅\n\n🕐Tez orada buyurtmangiz to'liq bajariladi✅</b>",reply_markup=Menu)
    await bot.send_message(ADMINS[0],msg, parse_mode="HTML")
		
@dp.callback_query_handler(post_callbackLE1.filter(actionLE1="cancelLE1"), state=Instas.lecon1)
async def cancel_LE1(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>Buyurtmalar bekor qilindi 🛑</b>",reply_markup=Menu)
    
@dp.message_handler(state=Instas.lecon1)
async def enter_LE1(message: Message, state: FSMContext):
   await message.answer("<b>👆👆👆Quyidagi buyurtmangizni\n✅Tasdiqlang Yoki ❌Rad eting Bo'lmasa Botagi boshqa tugmalar ishlamaydi🔐</b>")
	