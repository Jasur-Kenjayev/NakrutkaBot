from aiogram import types
from loader import dp, bot
from keyboards.default.tarmoq import Tarmoq, Torqaga
from keyboards.inline.likeecat import categoryLEP
from aiogram.types import Message, CallbackQuery
from states.instas import Instas
from aiogram.dispatcher import FSMContext
from keyboards.inline.LEkey2 import confirmation_keyboardLE2, post_callbackLE2
import requests
import json
from data.config import ADMINS
from keyboards.default.menu import Menu

@dp.callback_query_handler(text_contains="LEeLik")
async def LElike(call: CallbackQuery):
	await call.message.answer("<b>📇Marhamat keraklisini tanlang👇</b>",reply_markup=categoryLEP)
	await call.message.delete()
	await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains="LEliklar")
async def lelikr(call: CallbackQuery):
	likee2 = open("insta/likee2.txt","r")
	like2 = int(likee2.read())
	likee2.close()
	await call.message.answer(f"<b>❤️ 1000 ta like narxi: {like2}₽\n\n🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 10000 ta\n🔴 Nakrutka Tezligi - Sekin\n🚀 Joriy tezlik - Mavjud emas.\n✅ Haqiqi lik bosiladi\n\n👇 Marhamat kerakli miqdorni kiriting.</b>",reply_markup=Torqaga)
	await call.message.delete()
	await call.answer(cache_time=60)
	await Instas.leint2.set()

@dp.message_handler(state=Instas.leint2)
async def leinput2(message: Message,state: FSMContext):
	id = message.from_user.id
	leint2 = message.text
	await state.update_data(
		{"leint2": leint2}
	)
	try:
		kiriti = int(leint2)
		if kiriti >= 50:
			balansg = open(f"balans/balans{id}.txt", "r")
			likee2 = open("insta/likee2.txt","r")
			sumasi = int(likee2.read())
			hisobi = float(balansg.read())
			
			donasi = sumasi / 1000
			hisobk = kiriti * donasi
			balansg.close()
			likee2.close()
		if hisobi >= hisobk:
			await message.answer(f"<b>🟠 Likee post linkini kiriting👇</b>",reply_markup=Torqaga)
			await Instas.LElikn2.set()
		else:
			await message.answer(f"<b>💰Hisobingizda yetarli mablag' mavjud emas!</b>")
	except:
		await message.answer("<b>🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 10000 ta\n\n👇 Marhamat kerakli miqdorni kiriting.</b>")

@dp.message_handler(state=Instas.LElikn2)
async def LElikn2ui(message: types.Message, state: FSMContext):
	LElikn2 = message.text
	await state.update_data(
        {"LElikn2": LElikn2}
	)
	data = await state.get_data()
	leint2 = data.get("leint2")
	LElikn2 = data.get("LElikn2")
	likee2 = open("insta/likee2.txt","r")
	natija = int(likee2.read())
	instai = int(leint2)
	snatija = natija / 1000
	onatija = snatija * instai
	natijalar = "%.2f" % onatija
	msg = f"<b>📇 Malumotlar to'g'riligini tekshring👇\n\n🗞 Buyurtma soni - {leint2} ta\n🖇 Link - {LElikn2}\n💰 Buyurtma narxi - {natijalar}₽</b>"
	likee2.close()
	await Instas.next()
	await message.answer(msg,reply_markup=confirmation_keyboardLE2)


@dp.callback_query_handler(post_callbackLE2.filter(actionLE2="postLE2"), state=Instas.lecon2)
async def confirm_LE2(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        leint2 = data.get("leint2")
        LElikn2 = data.get("LElikn2")
        id = call.message.chat.id
        aslbalans = open(f"balans/balans{id}.txt", "r")
        likee2 = open("insta/likee2.txt","r")
        innarxi = int(likee2.read())
        sonib = int(leint2)
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
        likee2.close()
        mykey = "badcfb3366718f41450ead89cf954878"
        url = f'https://wiq.ru/api/?key={mykey}&action=create&service=701&quantity={sonib}&link={LElikn2}'
        respons = requests.get(url).json()
        resnatija = (respons["order"])
        msg = f"<b>📇Yangi buyurtma ID - {resnatija}\n📌Soni - {sonib} ta\n🖇Link - {LElikn2}\n💰Narxi - {natijalar1}₽\n\n✅@NakrutkaiBot</b>"
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>📇Buyurtmangiz qabul qilindi✅\n\n🕐Tez orada buyurtmangiz to'liq bajariladi✅</b>",reply_markup=Menu)
    await bot.send_message(ADMINS[0],msg, parse_mode="HTML")
		
@dp.callback_query_handler(post_callbackLE2.filter(actionLE2="cancelLE2"), state=Instas.lecon2)
async def cancel_LE2(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>Buyurtmalar bekor qilindi 🛑</b>",reply_markup=Menu)
    
@dp.message_handler(state=Instas.lecon2)
async def enter_LE2(message: Message, state: FSMContext):
   await message.answer("<b>👆👆👆Quyidagi buyurtmangizni\n✅Tasdiqlang Yoki ❌Rad eting Bo'lmasa Botagi boshqa tugmalar ishlamaydi🔐</b>")
	