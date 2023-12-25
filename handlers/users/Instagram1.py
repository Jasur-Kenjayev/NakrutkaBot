from aiogram import types
from loader import dp, bot
from keyboards.default.tarmoq import Torqaga
from aiogram.types import Message, CallbackQuery
from states.instas import Instas
from aiogram.dispatcher import FSMContext
from keyboards.inline.instak1 import confirmation_keyboardi1, post_callbacki1
import requests
import json
from data.config import ADMINS
from keyboards.default.menu import Menu

@dp.callback_query_handler(text_contains="realobuna")
async def realobun(call: CallbackQuery):
	instanarxi2 = open("insta/instanarx2.txt","r")
	instanarxis2 = int(instanarxi2.read())
	instanarxi2.close()
	await call.message.answer(f"<b>👤 1000 ta obunachi narxi: {instanarxis2}₽\n\n🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 200000 ta\n🔴 Nakrutka Tezligi - O'rtacha\n🚀 Joriy tezlik - (~13466-64923) soatiga\n\n👇 Marhamat kerakli miqdorni kiriting.</b>",reply_markup=Torqaga)
	await call.message.delete()
	await call.answer(cache_time=60)
	await Instas.inst1.set()

@dp.message_handler(state=Instas.inst1)
async def insta1(message: Message,state: FSMContext):
	id = message.from_user.id
	inst1 = message.text
	await state.update_data(
		{"inst1": inst1}
	)
	try:
		kiriti = int(inst1)
		if kiriti >= 50:
			balansg = open(f"balans/balans{id}.txt", "r")
			instanarxi2 = open("insta/instanarx2.txt","r")
			sumasi = int(instanarxi2.read())
			hisobi = float(balansg.read())
			donasi = sumasi / 1000
			hisobk = kiriti * donasi
			balansg.close()
			instanarxi2.close()
		if hisobi >= hisobk:
			await message.answer(f"<b>📸 Instagram proflingizni kiriting👇\n\n✅ Masalan: 1.we_wolf\n\n🔐 Profil ochiq bo'lishi kerak</b>",reply_markup=Torqaga)
			await Instas.userl1.set()
		else:
			await message.answer(f"<b>💰Hisobingizda yetarli mablag' mavjud emas!</b>")
	except:
		await message.answer("<b>🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 200000 ta\n\n👇 Marhamat kerakli miqdorni kiriting.</b>")

@dp.message_handler(state=Instas.userl1)
async def linku1(message: types.Message, state: FSMContext):
	userl1 = message.text
	await state.update_data(
        {"userl1": userl1}
	)
	data = await state.get_data()
	inst1 = data.get("inst1")
	userl1 = data.get("userl1")
	instanarxi2 = open("insta/instanarx2.txt","r")
	natija = int(instanarxi2.read())
	instai = int(inst1)
	snatija = natija / 1000
	onatija = snatija * instai
	natijalar = "%.2f" % onatija
	msg = f"<b>📇 Malumotlar to'g'riligini tekshring👇\n\n🗞 Buyurtma soni - {inst1} ta\n👤 Profil - {userl1}\n💰 Buyurtma narxi - {natijalar}₽</b>"
	instanarxi2.close()
	await Instas.next()
	await message.answer(msg,reply_markup=confirmation_keyboardi1)


@dp.callback_query_handler(post_callbacki1.filter(actioni1="posti1"), state=Instas.confin1)
async def confirm_insta2(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        inst1 = data.get("inst1")
        userl1 = data.get("userl1")
        id = call.message.chat.id
        aslbalans = open(f"balans/balans{id}.txt", "r")
        instanarxi2 = open("insta/instanarx2.txt","r")
        innarxi = int(instanarxi2.read())
        sonib = int(inst1)
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
        instanarxi2.close()
        mykey = "badcfb3366718f41450ead89cf954878"
        url = f'https://wiq.ru/api/?key={mykey}&action=create&service=136&quantity={sonib}&link=https://www.instagram.com/{userl1}/'
        respons = requests.get(url).json()
        resnatija = (respons["order"])
        msg = f"<b>📇Yangi buyurtma ID - {resnatija}\n📌Soni - {sonib} ta\n🖇Profili - {userl1}\n💰Narxi - {natijalar1}₽\n\n✅@NakrutkaiBot</b>"
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>📇Buyurtmangiz qabul qilindi✅\n\n🕐Tez orada buyurtmangiz to'liq bajariladi✅</b>",reply_markup=Menu)
    await bot.send_message(ADMINS[0],msg, parse_mode="HTML")
		
@dp.callback_query_handler(post_callbacki1.filter(actioni1="canceli1"), state=Instas.confin1)
async def cancel_insta2(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>Buyurtmalar bekor qilindi 🛑</b>",reply_markup=Menu)
    
@dp.message_handler(state=Instas.confin1)
async def enter_insta2(message: Message, state: FSMContext):
   await message.answer("<b>👆👆👆Quyidagi buyurtmangizni\n✅Tasdiqlang Yoki ❌Rad eting Bo'lmasa Botagi boshqa tugmalar ishlamaydi🔐</b>")
	