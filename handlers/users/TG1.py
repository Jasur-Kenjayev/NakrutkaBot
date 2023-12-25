from aiogram import types
from loader import dp, bot
from keyboards.default.tarmoq import Tarmoq, Torqaga
from aiogram.types import Message, CallbackQuery
from states.instas import Instas
from aiogram.dispatcher import FSMContext
from keyboards.inline.TGkey1 import confirmation_keyboardTG1, post_callbackTG1
import requests
import json
from data.config import ADMINS
from keyboards.default.menu import Menu

@dp.callback_query_handler(text_contains="tgobunach2")
async def tgobunachii2(call: CallbackQuery):
	TGobunachif1 = open("insta/TGobunachi1.txt","r")
	TGobunachisi1 = int(TGobunachif1.read())
	TGobunachif1.close()
	await call.message.answer(f"<b>👤 1000 ta obunachi narxi: {TGobunachisi1}₽\n\n🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 60000 ta\n🔴 Nakrutka Tezligi - Tez\n🚀 Joriy tezlik - (~3012) soatiga\n\n👇 Marhamat kerakli miqdorni kiriting.</b>",reply_markup=Torqaga)
	await call.message.delete()
	await call.answer(cache_time=60)
	await Instas.tgint1.set()

@dp.message_handler(state=Instas.tgint1)
async def tginput1(message: Message,state: FSMContext):
	id = message.from_user.id
	tgint1 = message.text
	await state.update_data(
		{"tgint1": tgint1}
	)
	try:
		kiriti = int(tgint1)
		if kiriti >= 50:
			balansg = open(f"balans/balans{id}.txt", "r")
			TGobunachif1 = open("insta/TGobunachi1.txt","r")
			sumasi = int(TGobunachif1.read())
			hisobi = float(balansg.read())
		
			donasi = sumasi / 1000
			hisobk = kiriti * donasi
			balansg.close()
			TGobunachif1.close()
		if hisobi >= hisobk:
			await message.answer(f"<b>🔵 Telegram kanal yoki grupa linkni kiriting👇\n\n✅ Masalan: https://t.me/Python_Koderuz</b>",reply_markup=Torqaga)
			await Instas.tglink1.set()
		else:
			await message.answer(f"<b>💰Hisobingizda yetarli mablag' mavjud emas!</b>")
	except:
		await message.answer("<b>🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 60000 ta\n\n👇 Marhamat kerakli miqdorni kiriting.</b>")

@dp.message_handler(state=Instas.tglink1)
async def tglinki(message: types.Message, state: FSMContext):
	tglink1 = message.text
	await state.update_data(
        {"tglink1": tglink1}
	)
	data = await state.get_data()
	tgint1 = data.get("tgint1")
	tglink1 = data.get("tglink1")
	TGobunachif1 = open("insta/TGobunachi1.txt","r")
	natija = int(TGobunachif1.read())
	instai = int(tgint1)
	snatija = natija / 1000
	onatija = snatija * instai
	natijalar = "%.2f" % onatija
	msg = f"<b>📇 Malumotlar to'g'riligini tekshring👇\n\n🗞 Buyurtma soni - {tgint1} ta\n🖇 Link - {tglink1}\n💰 Buyurtma narxi - {natijalar}₽</b>"
	TGobunachif1.close()
	await Instas.next()
	await message.answer(msg,reply_markup=confirmation_keyboardTG1)


@dp.callback_query_handler(post_callbackTG1.filter(actionTG1="postTG1"), state=Instas.tgcon1)
async def confirm_TG1(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        tgint1 = data.get("tgint1")
        tglink1 = data.get("tglink1")
        id = call.message.chat.id
        aslbalans = open(f"balans/balans{id}.txt", "r")
        TGobunachif1 = open("insta/TGobunachi1.txt","r")
        innarxi = int(TGobunachif1.read())
        sonib = int(tgint1)
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
        TGobunachif1.close()
        mykey = "badcfb3366718f41450ead89cf954878"
        url = f'https://wiq.ru/api/?key={mykey}&action=create&service=415&quantity={sonib}&link={tglink1}'
        respons = requests.get(url).json()
        resnatija = (respons["order"])
        msg = f"<b>📇Yangi buyurtma ID - {resnatija}\n📌Soni - {sonib} ta\n🖇Link - {tglink1}\n💰Narxi - {natijalar1}₽\n\n✅@NakrutkaiBot</b>"
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>📇Buyurtmangiz qabul qilindi✅\n\n🕐Tez orada buyurtmangiz to'liq bajariladi✅</b>",reply_markup=Menu)
    await bot.send_message(ADMINS[0],msg, parse_mode="HTML")
		
@dp.callback_query_handler(post_callbackTG1.filter(actionTG1="cancelTG1"), state=Instas.tgcon1)
async def cancel_TG1(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>Buyurtmalar bekor qilindi 🛑</b>",reply_markup=Menu)
    
@dp.message_handler(state=Instas.tgcon1)
async def enter_TG1(message: Message, state: FSMContext):
   await message.answer("<b>👆👆👆Quyidagi buyurtmangizni\n✅Tasdiqlang Yoki ❌Rad eting Bo'lmasa Botagi boshqa tugmalar ishlamaydi🔐</b>")
	