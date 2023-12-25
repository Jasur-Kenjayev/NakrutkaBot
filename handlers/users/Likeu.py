from aiogram import types
from loader import dp, bot
from keyboards.default.tarmoq import Torqaga
from aiogram.types import Message, CallbackQuery
from states.instas import Instas
from aiogram.dispatcher import FSMContext
from keyboards.inline.inLike import confirmation_keyboardL, post_callbackL
import requests
import json
from data.config import ADMINS
from keyboards.default.menu import Menu
from keyboards.inline.likeun import categoryLike

@dp.callback_query_handler(text_contains="conLik")
async def instaLike(call: CallbackQuery):
	await call.message.answer("<b>📇Marhamat keraklisini tanlang👇</b>",reply_markup=categoryLike)
	await call.message.delete()
	await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains="Likbe")
async def Likbe(call: CallbackQuery):
	likt = open("insta/liket.txt","r")
	liktt = int(likt.read())
	likt.close()
	await call.message.answer(f"<b>❤️ 1000 ta like narxi: {liktt}₽\n\n🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 30000 ta\n🔴 Nakrutka Tezligi - Juda Tez\n🚀 Joriy tezlik - (~117-124) soatiga\n\n👇 Marhamat kerakli miqdorni kiriting.</b>",reply_markup=Torqaga)
	await call.message.delete()
	await call.answer(cache_time=60)
	await Instas.Likk.set()

@dp.message_handler(state=Instas.Likk)
async def insLik(message: Message,state: FSMContext):
	id = message.from_user.id
	Likk = message.text
	await state.update_data(
		{"Likk": Likk}
	)
	try:
		kiriti = int(Likk)
		if kiriti >= 50:
			balansg = open(f"balans/balans{id}.txt", "r")
			likt = open("insta/liket.txt","r")
			sumasi = int(likt.read())
			hisobi = float(balansg.read())
		
			donasi = sumasi / 1000
			hisobk = kiriti * donasi
			balansg.close()
			likt.close()
		if hisobi >= hisobk:
			await message.answer(f"<b>📸 Instagram Post Linkini kiriting👇\n\n✅ Masalan: https://www.instagram.com/p/CP22a0jFSsW/?igshid=YmMyMTA2M2Y=\n\n🔐 Profil ochiq bo'lishi kerak</b>",reply_markup=Torqaga)
			await Instas.Likkl.set()
		else:
			await message.answer(f"<b>💰Hisobingizda yetarli mablag' mavjud emas!</b>")
	except:
		await message.answer("<b>🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 30000 ta\n\n👇 Marhamat kerakli miqdorni kiriting.</b>")

@dp.message_handler(state=Instas.Likkl)
async def Likklsl(message: types.Message, state: FSMContext):
	Likkl = message.text
	await state.update_data(
        {"Likkl": Likkl}
	)
	data = await state.get_data()
	Likk = data.get("Likk")
	Likkl = data.get("Likkl")
	likt = open("insta/liket.txt","r")
	natija = int(likt.read())
	instai = int(Likk)
	snatija = natija / 1000
	onatija = snatija * instai
	natijalar = "%.2f" % onatija
	msg = f"<b>📇 Malumotlar to'g'riligini tekshring👇\n\n🗞 Buyurtma soni - {Likk} ta\n🖇 Link - {Likkl}\n💰 Buyurtma narxi - {natijalar}₽</b>"
	likt.close()
	await Instas.next()
	await message.answer(msg,reply_markup=confirmation_keyboardL)


@dp.callback_query_handler(post_callbackL.filter(actionL="postL"), state=Instas.Likkc)
async def confirm_Lik(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        Likk = data.get("Likk")
        Likkl = data.get("Likkl")
        id = call.message.chat.id
        aslbalans = open(f"balans/balans{id}.txt", "r")
        likt = open("insta/liket.txt","r")
        innarxi = int(likt.read())
        sonib = int(Likk)
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
        likt.close()
        mykey = "badcfb3366718f41450ead89cf954878"
        url = f'https://wiq.ru/api/?key={mykey}&action=create&service=31&quantity={sonib}&link={Likkl}'
        respons = requests.get(url).json()
        resnatija = (respons["order"])
        
        msg = f"<b>📇Yangi buyurtma ID - {resnatija}\n📌Soni - {sonib} ta\n🖇Linki- {Likkl}\n💰Narxi - {natijalar1}₽\n\n✅@NakrutkaiBot</b>"
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>📇Buyurtmangiz qabul qilindi✅\n\n🕐Tez orada buyurtmangiz to'liq bajariladi✅</b>",reply_markup=Menu)
    await bot.send_message(ADMINS[0],msg, parse_mode="HTML")
		
@dp.callback_query_handler(post_callbackL.filter(actionL="cancelL"), state=Instas.Likkc)
async def cancel_Lik(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>Buyurtmalar bekor qilindi 🛑</b>",reply_markup=Menu)
    
@dp.message_handler(state=Instas.Likkc)
async def enter_Lik(message: Message, state: FSMContext):
   await message.answer("<b>👆👆👆Quyidagi buyurtmangizni\n✅Tasdiqlang Yoki ❌Rad eting Bo'lmasa Botagi boshqa tugmalar ishlamaydi🔐</b>")
	