from aiogram import types
from loader import dp, bot
from keyboards.default.tarmoq import Tarmoq, Torqaga
from aiogram.types import Message, CallbackQuery
from states.instas import Instas
from aiogram.dispatcher import FSMContext
from keyboards.inline.TGkey2 import confirmation_keyboardTG2, post_callbackTG2
import requests
import json
from data.config import ADMINS
from keyboards.default.menu import Menu

@dp.callback_query_handler(text_contains="tgobunach3")
async def tgobunachii3(call: CallbackQuery):
	TGobunachif2 = open("insta/TGobunachi2.txt","r")
	TGobunachisi2 = int(TGobunachif2.read())
	TGobunachif2.close()
	await call.message.answer(f"<b>👤 1000 ta obunachi narxi: {TGobunachisi2}₽\n\n🔥 Minimal buyurtma: 700 ta\n⚡️ Maksimal buyurtma: 40000 ta\n🔴 Nakrutka Tezligi - Tez\n🚀 Joriy tezlik -  (~3369-3939) soatiga\n\n👇 Marhamat kerakli miqdorni kiriting.</b>",reply_markup=Torqaga)
	await call.message.delete()
	await call.answer(cache_time=60)
	await Instas.tgint2.set()

@dp.message_handler(state=Instas.tgint2)
async def tginput2(message: Message,state: FSMContext):
	id = message.from_user.id
	tgint2 = message.text
	await state.update_data(
		{"tgint2": tgint2}
	)
	try:
		kiriti = int(tgint2)
		if kiriti >= 700:
			balansg = open(f"balans/balans{id}.txt", "r")
			TGobunachif2 = open("insta/TGobunachi2.txt","r")
			sumasi = int(TGobunachif2.read())
			hisobi = float(balansg.read())
		
			donasi = sumasi / 1000
			hisobk = kiriti * donasi
			balansg.close()
			TGobunachif2.close()
		if hisobi >= hisobk:
			await message.answer(f"<b>🔵 Telegram kanal yoki grupa linkni kiriting👇\n\n✅ Masalan: https://t.me/Python_Koderuz</b>",reply_markup=Torqaga)
			await Instas.tglink2.set()
		else:
			await message.answer(f"<b>💰Hisobingizda yetarli mablag' mavjud emas!</b>")
	except:
		await message.answer("<b>🔥 Minimal buyurtma: 700 ta\n⚡️ Maksimal buyurtma: 40000 ta\n\n👇 Marhamat kerakli miqdorni kiriting.</b>")

@dp.message_handler(state=Instas.tglink2)
async def tglinki(message: types.Message, state: FSMContext):
	tglink2 = message.text
	await state.update_data(
        {"tglink2": tglink2}
	)
	data = await state.get_data()
	tgint2 = data.get("tgint2")
	tglink2 = data.get("tglink2")
	TGobunachif2 = open("insta/TGobunachi2.txt","r")
	natija = int(TGobunachif2.read())
	instai = int(tgint2)
	snatija = natija / 1000
	onatija = snatija * instai
	natijalar = "%.2f" % onatija
	msg = f"<b>📇 Malumotlar to'g'riligini tekshring👇\n\n🗞 Buyurtma soni - {tgint2} ta\n🖇 Link - {tglink2}\n💰 Buyurtma narxi - {natijalar}₽</b>"
	TGobunachif2.close()
	await Instas.next()
	await message.answer(msg,reply_markup=confirmation_keyboardTG2)


@dp.callback_query_handler(post_callbackTG2.filter(actionTG2="postTG2"), state=Instas.tgcon2)
async def confirm_TG2(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        tgint2 = data.get("tgint2")
        tglink2 = data.get("tglink2")
        id = call.message.chat.id
        aslbalans = open(f"balans/balans{id}.txt", "r")
        TGobunachif2 = open("insta/TGobunachi2.txt","r")
        innarxi = int(TGobunachif2.read())
        sonib = int(tgint2)
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
        TGobunachif2.close()
        mykey = "badcfb3366718f41450ead89cf954878"
        url = f'https://wiq.ru/api/?key={mykey}&action=create&service=400&quantity={sonib}&link={tglink2}'
        respons = requests.get(url).json()
        resnatija = (respons["order"])
        msg = f"<b>📇Yangi buyurtma ID - {resnatija}\n📌Soni - {sonib} ta\n🖇Link - {tglink2}\n💰Narxi - {natijalar1}₽\n\n✅@NakrutkaiBot</b>"
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>📇Buyurtmangiz qabul qilindi✅\n\n🕐Tez orada buyurtmangiz to'liq bajariladi✅</b>",reply_markup=Menu)
    await bot.send_message(ADMINS[0],msg, parse_mode="HTML")
		
@dp.callback_query_handler(post_callbackTG2.filter(actionTG2="cancelTG2"), state=Instas.tgcon2)
async def cancel_TG2(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>Buyurtmalar bekor qilindi 🛑</b>",reply_markup=Menu)
    
@dp.message_handler(state=Instas.tgcon2)
async def enter_TG2(message: Message, state: FSMContext):
   await message.answer("<b>👆👆👆Quyidagi buyurtmangizni\n✅Tasdiqlang Yoki ❌Rad eting Bo'lmasa Botagi boshqa tugmalar ishlamaydi🔐</b>")
	