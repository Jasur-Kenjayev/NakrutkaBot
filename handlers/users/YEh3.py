from aiogram import types
from loader import dp, bot
from keyboards.default.tarmoq import Tarmoq, Torqaga
from aiogram.types import Message, CallbackQuery
from states.instas import Instas
from aiogram.dispatcher import FSMContext
from keyboards.inline.YEkey3 import confirmation_keyboardYE3, post_callbackYE3
import requests
import json
from data.config import ADMINS
from keyboards.default.menu import Menu
	
@dp.callback_query_handler(text_contains="YouLike")
async def yY3(call: CallbackQuery):
	YouTube3 = open("insta/YouTube3.txt","r")
	YouTube3e = int(YouTube3.read())
	YouTube3.close()
	await call.message.answer(f"<b>❤️ 1000 ta like narxi: {YouTube3e}₽\n\n🔥 Minimal buyurtma: 100 ta\n⚡️ Maksimal buyurtma: 100000 ta\n🔴 Nakrutka Tezligi - Tez\n🚀 Joriy tezlik - (~3047)  Soatiga\n\n👇 Marhamat kerakli miqdorni kiriting.</b>",reply_markup=Torqaga)
	await call.message.delete()
	await call.answer(cache_time=60)
	await Instas.yeint3.set()

@dp.message_handler(state=Instas.yeint3)
async def yeinput73(message: Message,state: FSMContext):
	id = message.from_user.id
	yeint3 = message.text
	await state.update_data(
		{"yeint3": yeint3}
	)
	try:
		kiriti = int(yeint3)
		if kiriti >= 100:
			balansg = open(f"balans/balans{id}.txt", "r")
			YouTube3 = open("insta/YouTube3.txt","r")
			sumasi = int(YouTube3.read())
			hisobi = float(balansg.read())
			
			donasi = sumasi / 1000
			hisobk = kiriti * donasi
			balansg.close()
			YouTube3.close()
		if hisobi >= hisobk:
			await message.answer(f"<b>🎞 YouTube video linkini kiriting👇\n\n✅ Masalan: https://youtu.be/vqLoGp1u76w</b>",reply_markup=Torqaga)
			await Instas.yelink3.set()
		else:
			await message.answer(f"<b>💰Hisobingizda yetarli mablag' mavjud emas!</b>")
	except:
		await message.answer("<b>🔥 Minimal buyurtma: 100 ta\n⚡️ Maksimal buyurtma: 100000 ta\n\n👇 Marhamat kerakli miqdorni kiriting.</b>")

@dp.message_handler(state=Instas.yelink3)
async def yelink3i(message: types.Message, state: FSMContext):
	yelink3 = message.text
	await state.update_data(
        {"yelink3": yelink3}
	)
	data = await state.get_data()
	yeint3 = data.get("yeint3")
	yelink3 = data.get("yelink3")
	YouTube3 = open("insta/YouTube3.txt","r")
	natija = int(YouTube3.read())
	instai = int(yeint3)
	snatija = natija / 1000
	onatija = snatija * instai
	natijalar = "%.2f" % onatija
	msg = f"<b>📇 Malumotlar to'g'riligini tekshring👇\n\n🗞 Buyurtma soni - {yeint3} ta\n🖇 Link - {yelink3}\n💰 Buyurtma narxi - {natijalar}₽</b>"
	YouTube3.close()
	await Instas.next()
	await message.answer(msg,reply_markup=confirmation_keyboardYE3)


@dp.callback_query_handler(post_callbackYE3.filter(actionYE3="postYE3"), state=Instas.yecon3)
async def confirm_YE3(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        yeint3 = data.get("yeint3")
        yelink3 = data.get("yelink3")
        id = call.message.chat.id
        aslbalans = open(f"balans/balans{id}.txt", "r")
        YouTube3 = open("insta/YouTube3.txt","r")
        innarxi = int(YouTube3.read())
        sonib = int(yeint3)
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
        YouTube3.close()
        mykey = "badcfb3366718f41450ead89cf954878"
        url = f'https://wiq.ru/api/?key={mykey}&action=create&service=509&quantity={sonib}&link={yelink3}'
        respons = requests.get(url).json()
        resnatija = (respons["order"])
        msg = f"<b>📇Yangi buyurtma ID - {resnatija}\n📌Soni - {sonib} ta\n🖇Link - {yelink3}\n💰Narxi - {natijalar1}₽\n\n✅@NakrutkaiBot</b>"
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>📇Buyurtmangiz qabul qilindi✅\n\n🕐Tez orada buyurtmangiz to'liq bajariladi✅</b>",reply_markup=Menu)
    await bot.send_message(ADMINS[0],msg, parse_mode="HTML")
		
@dp.callback_query_handler(post_callbackYE3.filter(actionYE3="cancelYE3"), state=Instas.yecon3)
async def cancel_YE3(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>Buyurtmalar bekor qilindi 🛑</b>",reply_markup=Menu)
    
@dp.message_handler(state=Instas.yecon3)
async def enter_YE3(message: Message, state: FSMContext):
   await message.answer("<b>👆👆👆Quyidagi buyurtmangizni\n✅Tasdiqlang Yoki ❌Rad eting Bo'lmasa Botagi boshqa tugmalar ishlamaydi🔐</b>")
	