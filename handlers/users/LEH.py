from aiogram import types
from loader import dp, bot
from keyboards.default.tarmoq import Tarmoq, Torqaga
from keyboards.inline.likeecat import categoryLE
from keyboards.inline.instatanlash import LETan
from aiogram.types import Message, CallbackQuery
from states.instas import Instas
from aiogram.dispatcher import FSMContext
from keyboards.inline.LEkey import confirmation_keyboardLE, post_callbackLE
import requests
import json
from data.config import ADMINS
from keyboards.default.menu import Menu

@dp.message_handler(text="🟠 Likee")
async def LE(message:
	types.Message):
	await message.answer("<b>📲 Kerakli xizmat turini tanlang</b>",reply_markup=LETan)

@dp.callback_query_handler(text_contains="LeObun")
async def LEobunach(call: CallbackQuery):
	await call.message.answer("<b>📇Marhamat keraklisini tanlang👇</b>",reply_markup=categoryLE)
	await call.message.delete()
	await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains="LEobunachi")
async def leobunachi1(call: CallbackQuery):
	likee = open("insta/likee.txt","r")
	like = int(likee.read())
	likee.close()
	await call.message.answer(f"<b>👤 1000 ta obunachi narxi: {like}₽\n\n🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 10000 ta\n🔴 Nakrutka Tezligi - Sekin\n🚀 Joriy tezlik - Mavjud emas.\n✅ Haqiqi Obunachilar\n\n👇 Marhamat kerakli miqdorni kiriting.</b>",reply_markup=Torqaga)
	await call.message.delete()
	await call.answer(cache_time=60)
	await Instas.leint.set()

@dp.message_handler(state=Instas.leint)
async def leinput(message: Message,state: FSMContext):
	id = message.from_user.id
	leint = message.text
	await state.update_data(
		{"leint": leint}
	)
	try:
		kiriti = int(leint)
		if kiriti >= 50:
			balansg = open(f"balans/balans{id}.txt", "r")
			likee = open("insta/likee.txt","r")
			sumasi = int(likee.read())
			hisobi = float(balansg.read())
		
			donasi = sumasi / 1000
			hisobk = kiriti * donasi
			balansg.close()
			likee.close()
		if hisobi >= hisobk:
			await message.answer(f"<b>🟠 Likee profil ID ni kiriting👇\n\n✅ Masalan: 1.we_wolf</b>",reply_markup=Torqaga)
			await Instas.LElikn.set()
		else:
			await message.answer(f"<b>💰Hisobingizda yetarli mablag' mavjud emas!</b>")
	except:
		await message.answer("<b>🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 10000 ta\n\n👇 Marhamat kerakli miqdorni kiriting.</b>")

@dp.message_handler(state=Instas.LElikn)
async def LEliknui(message: types.Message, state: FSMContext):
	LElikn = message.text
	await state.update_data(
        {"LElikn": LElikn}
	)
	data = await state.get_data()
	leint = data.get("leint")
	LElikn = data.get("LElikn")
	likee = open("insta/likee.txt","r")
	natija = int(likee.read())
	instai = int(leint)
	snatija = natija / 1000
	onatija = snatija * instai
	natijalar = "%.2f" % onatija
	msg = f"<b>📇 Malumotlar to'g'riligini tekshring👇\n\n🗞 Buyurtma soni - {leint} ta\n🖇 Link - {LElikn}\n💰 Buyurtma narxi - {natijalar}₽</b>"
	likee.close()
	await Instas.next()
	await message.answer(msg,reply_markup=confirmation_keyboardLE)


@dp.callback_query_handler(post_callbackLE.filter(actionLE="postLE"), state=Instas.lecon)
async def confirm_LE(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        leint = data.get("leint")
        LElikn = data.get("LElikn")
        id = call.message.chat.id
        aslbalans = open(f"balans/balans{id}.txt", "r")
        likee = open("insta/likee.txt","r")
        innarxi = int(likee.read())
        sonib = int(leint)
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
        likee.close()
        mykey = "badcfb3366718f41450ead89cf954878"
        url = f'https://wiq.ru/api/?key={mykey}&action=create&service=702&quantity={sonib}&link={LElikn}'
        respons = requests.get(url).json()
        resnatija = (respons["order"])
        msg = f"<b>📇Yangi buyurtma ID - {resnatija}\n📌Soni - {sonib} ta\n🖇Link - {LElikn}\n💰Narxi - {natijalar1}₽\n\n✅@NakrutkaiBot</b>"
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>📇Buyurtmangiz qabul qilindi✅\n\n🕐Tez orada buyurtmangiz to'liq bajariladi✅</b>",reply_markup=Menu)
    await bot.send_message(ADMINS[0],msg, parse_mode="HTML")
		
@dp.callback_query_handler(post_callbackLE.filter(actionLE="cancelLE"), state=Instas.lecon)
async def cancel_LE(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>Buyurtmalar bekor qilindi 🛑</b>",reply_markup=Menu)
    
@dp.message_handler(state=Instas.lecon)
async def enter_LE(message: Message, state: FSMContext):
   await message.answer("<b>👆👆👆Quyidagi buyurtmangizni\n✅Tasdiqlang Yoki ❌Rad eting Bo'lmasa Botagi boshqa tugmalar ishlamaydi🔐</b>")
	