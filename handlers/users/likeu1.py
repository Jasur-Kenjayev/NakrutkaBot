from aiogram import types
from loader import dp, bot
from keyboards.default.tarmoq import Torqaga
from aiogram.types import Message, CallbackQuery
from states.instas import Instas
from aiogram.dispatcher import FSMContext
from keyboards.inline.inLike1 import confirmation_keyboardL1, post_callbackL1
import requests
import json
from data.config import ADMINS
from keyboards.default.menu import Menu

@dp.callback_query_handler(text_contains="JvoyL")
async def Likbe1(call: CallbackQuery):
	likt1 = open("insta/liket1.txt","r")
	liktt1 = int(likt1.read())
	likt1.close()
	await call.message.answer(f"<b>❤️ 1000 ta like narxi: {liktt1}₽\n\n🔥 Minimal buyurtma: 100 ta\n⚡️ Maksimal buyurtma: 50000 ta\n🔴 Nakrutka Tezligi - Juda Tez\n🚀 Joriy tezlik - (~967-2901)  soatiga\n\n👇 Marhamat kerakli miqdorni kiriting.</b>",reply_markup=Torqaga)
	await call.message.delete()
	await call.answer(cache_time=60)
	await Instas.Likk1.set()

@dp.message_handler(state=Instas.Likk1)
async def insLik1(message: Message,state: FSMContext):
	id = message.from_user.id
	Likk1 = message.text
	await state.update_data(
		{"Likk1": Likk1}
	)
	try:
		kiriti = int(Likk1)
		if kiriti >= 100:
			balansg = open(f"balans/balans{id}.txt", "r")
			likt1 = open("insta/liket1.txt","r")
			sumasi = int(likt1.read())
			hisobi = float(balansg.read())
		
			donasi = sumasi / 1000
			hisobk = kiriti * donasi
			balansg.close()
			likt1.close()
		if hisobi >= hisobk:
			await message.answer(f"<b>📸 Instagram Post Linkini kiriting👇\n\n✅ Masalan: https://www.instagram.com/p/CP22a0jFSsW/?igshid=YmMyMTA2M2Y=\n\n🔐 Profil ochiq bo'lishi kerak</b>",reply_markup=Torqaga)
			await Instas.Likkl1.set()
		else:
			await message.answer(f"<b>💰Hisobingizda yetarli mablag' mavjud emas!</b>")
	except:
		await message.answer("<b>🔥 Minimal buyurtma: 100 ta\n⚡️ Maksimal buyurtma: 50000 ta\n\n👇 Marhamat kerakli miqdorni kiriting.</b>")

@dp.message_handler(state=Instas.Likkl1)
async def Likkls1l(message: types.Message, state: FSMContext):
	Likkl1 = message.text
	await state.update_data(
        {"Likkl1": Likkl1}
	)
	data = await state.get_data()
	Likk1 = data.get("Likk1")
	Likkl1 = data.get("Likkl1")
	likt1 = open("insta/liket1.txt","r")
	natija = int(likt1.read())
	instai = int(Likk1)
	snatija = natija / 1000
	onatija = snatija * instai
	natijalar = "%.2f" % onatija
	msg = f"<b>📇 Malumotlar to'g'riligini tekshring👇\n\n🗞 Buyurtma soni - {Likk1} ta\n🖇 Link - {Likkl1}\n💰 Buyurtma narxi - {natijalar}₽</b>"
	likt1.close()
	await Instas.next()
	await message.answer(msg,reply_markup=confirmation_keyboardL1)


@dp.callback_query_handler(post_callbackL1.filter(actionL1="postL1"), state=Instas.Likkc1)
async def confirm_Lik1(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        Likk1 = data.get("Likk1")
        Likkl1 = data.get("Likkl1")
        id = call.message.chat.id
        aslbalans = open(f"balans/balans{id}.txt", "r")
        likt1 = open("insta/liket1.txt","r")
        innarxi = int(likt1.read())
        sonib = int(Likk1)
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
        likt1.close()
        mykey = "badcfb3366718f41450ead89cf954878"
        url = f'https://wiq.ru/api/?key={mykey}&action=create&service=122&quantity={sonib}&link={Likkl1}'
        respons = requests.get(url).json()
        resnatija = (respons["order"])
        
        msg = f"<b>📇Yangi buyurtma ID - {resnatija}\n📌Soni - {sonib} ta\n🖇Linki- {Likkl1}\n💰Narxi - {natijalar1}₽\n\n✅@NakrutkaiBot</b>"
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>📇Buyurtmangiz qabul qilindi✅\n\n🕐Tez orada buyurtmangiz to'liq bajariladi✅</b>",reply_markup=Menu)
    await bot.send_message(ADMINS[0],msg, parse_mode="HTML")
		
@dp.callback_query_handler(post_callbackL1.filter(actionL1="cancelL1"), state=Instas.Likkc1)
async def cancel_Lik1(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>Buyurtmalar bekor qilindi 🛑</b>",reply_markup=Menu)
    
@dp.message_handler(state=Instas.Likkc1)
async def enter_Lik1(message: Message, state: FSMContext):
   await message.answer("<b>👆👆👆Quyidagi buyurtmangizni\n✅Tasdiqlang Yoki ❌Rad eting Bo'lmasa Botagi boshqa tugmalar ishlamaydi🔐</b>")
	