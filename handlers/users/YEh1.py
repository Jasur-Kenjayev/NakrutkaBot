from aiogram import types
from loader import dp, bot
from keyboards.default.tarmoq import Tarmoq, Torqaga
from aiogram.types import Message, CallbackQuery
from states.instas import Instas
from aiogram.dispatcher import FSMContext
from keyboards.inline.YEkey1 import confirmation_keyboardYE1, post_callbackYE1
import requests
import json
from data.config import ADMINS
from keyboards.default.menu import Menu

@dp.callback_query_handler(text_contains="YEklayk")
async def YEprosmotr1(call: CallbackQuery):
	YouTube1 = open("insta/YouTube1.txt","r")
	YouTube1e = int(YouTube1.read())
	YouTube1.close()
	await call.message.answer(f"<b>👁 1000 ta prosmotr narxi: {YouTube1e}₽\n\n🔥 Minimal buyurtma: 500 ta\n⚡️ Maksimal buyurtma: 100000000 ta\n🔴 Nakrutka Tezligi - Sekin\n🚀 Joriy tezlik - Mavjud emas\n✅ Kafolatlangan\n\n👇 Marhamat kerakli miqdorni kiriting.</b>",reply_markup=Torqaga)
	await call.message.delete()
	await call.answer(cache_time=60)
	await Instas.yeint1.set()

@dp.message_handler(state=Instas.yeint1)
async def yeinput1(message: Message,state: FSMContext):
	id = message.from_user.id
	yeint1 = message.text
	await state.update_data(
		{"yeint1": yeint1}
	)
	try:
		kiriti = int(yeint1)
		if kiriti >= 500:
			balansg = open(f"balans/balans{id}.txt", "r")
			YouTube1 = open("insta/YouTube1.txt","r")
			sumasi = int(YouTube1.read())
			hisobi = float(balansg.read())
			
			donasi = sumasi / 1000
			hisobk = kiriti * donasi
			balansg.close()
			YouTube1.close()
		if hisobi >= hisobk:
			await message.answer(f"<b>🎞 YouTube video linkini kiriting👇\n\n✅ Masalan: https://youtu.be/vqLoGp1u76w</b>",reply_markup=Torqaga)
			await Instas.yelink1.set()
		else:
			await message.answer(f"<b>💰Hisobingizda yetarli mablag' mavjud emas!</b>")
	except:
		await message.answer("<b>🔥 Minimal buyurtma: 500 ta\n⚡️ Maksimal buyurtma: 100000000 ta\n\n👇 Marhamat kerakli miqdorni kiriting.</b>")

@dp.message_handler(state=Instas.yelink1)
async def yelink1i(message: types.Message, state: FSMContext):
	yelink1 = message.text
	await state.update_data(
        {"yelink1": yelink1}
	)
	data = await state.get_data()
	yeint1 = data.get("yeint1")
	yelink1 = data.get("yelink1")
	YouTube1 = open("insta/YouTube1.txt","r")
	natija = int(YouTube1.read())
	instai = int(yeint1)
	snatija = natija / 1000
	onatija = snatija * instai
	natijalar = "%.2f" % onatija
	msg = f"<b>📇 Malumotlar to'g'riligini tekshring👇\n\n🗞 Buyurtma soni - {yeint1} ta\n🖇 Link - {yelink1}\n💰 Buyurtma narxi - {natijalar}₽</b>"
	YouTube1.close()
	await Instas.next()
	await message.answer(msg,reply_markup=confirmation_keyboardYE1)


@dp.callback_query_handler(post_callbackYE1.filter(actionYE1="postYE1"), state=Instas.yecon1)
async def confirm_YE(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        yeint1 = data.get("yeint1")
        yelink1 = data.get("yelink1")
        id = call.message.chat.id
        aslbalans = open(f"balans/balans{id}.txt", "r")
        YouTube1 = open("insta/YouTube1.txt","r")
        innarxi = int(YouTube1.read())
        sonib = int(yeint1)
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
        YouTube1.close()
        mykey = "badcfb3366718f41450ead89cf954878"
        url = f'https://wiq.ru/api/?key={mykey}&action=create&service=506&quantity={sonib}&link={yelink1}'
        respons = requests.get(url).json()
        resnatija = (respons["order"])
        msg = f"<b>📇Yangi buyurtma ID - {resnatija}\n📌Soni - {sonib} ta\n🖇Link - {yelink1}\n💰Narxi - {natijalar1}₽\n\n✅@NakrutkaiBot</b>"
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>📇Buyurtmangiz qabul qilindi✅\n\n🕐Tez orada buyurtmangiz to'liq bajariladi✅</b>",reply_markup=Menu)
    await bot.send_message(ADMINS[0],msg, parse_mode="HTML")
		
@dp.callback_query_handler(post_callbackYE1.filter(actionYE1="cancelYE1"), state=Instas.yecon1)
async def cancel_YE1(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>Buyurtmalar bekor qilindi 🛑</b>",reply_markup=Menu)
    
@dp.message_handler(state=Instas.yecon1)
async def enter_YE1(message: Message, state: FSMContext):
   await message.answer("<b>👆👆👆Quyidagi buyurtmangizni\n✅Tasdiqlang Yoki ❌Rad eting Bo'lmasa Botagi boshqa tugmalar ishlamaydi🔐</b>")
	