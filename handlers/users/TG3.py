from aiogram import types
from loader import dp, bot
from keyboards.default.tarmoq import Tarmoq, Torqaga
from aiogram.types import Message, CallbackQuery
from states.instas import Instas
from aiogram.dispatcher import FSMContext
from keyboards.inline.TGkey3 import confirmation_keyboardTG3, post_callbackTG3
import requests
import json
from data.config import ADMINS
from keyboards.default.menu import Menu

@dp.callback_query_handler(text_contains="tgobunach4")
async def tgobunachii4(call: CallbackQuery):
	TGobunachif3 = open("insta/TGobunachi3.txt","r")
	TGobunachisi3 = int(TGobunachif3.read())
	TGobunachif3.close()
	await call.message.answer(f"<b>👤 1000 ta obunachi narxi: {TGobunachisi3}₽\n\n🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 30000 ta\n🔴 Nakrutka Tezligi - Tez\n🚀 Joriy tezlik - (~3380-3623) soatiga\n\n👇 Marhamat kerakli miqdorni kiriting.</b>",reply_markup=Torqaga)
	await call.message.delete()
	await call.answer(cache_time=60)
	await Instas.tgint3.set()

@dp.message_handler(state=Instas.tgint3)
async def tginput3(message: Message,state: FSMContext):
	id = message.from_user.id
	tgint3 = message.text
	await state.update_data(
		{"tgint3": tgint3}
	)
	try:
		kiriti = int(tgint3)
		if kiriti >= 50:
			balansg = open(f"balans/balans{id}.txt", "r")
			TGobunachif3 = open("insta/TGobunachi3.txt","r")
			sumasi = int(TGobunachif3.read())
			hisobi = float(balansg.read())
		
			donasi = sumasi / 1000
			hisobk = kiriti * donasi
			balansg.close()
			TGobunachif3.close()
		if hisobi >= hisobk:
			await message.answer(f"<b>🔵 Telegram kanal yoki grupa linkni kiriting👇\n\n✅ Masalan: https://t.me/Python_Koderuz</b>",reply_markup=Torqaga)
			await Instas.tglink3.set()
		else:
			await message.answer(f"<b>💰Hisobingizda yetarli mablag' mavjud emas!</b>")
	except:
		await message.answer("<b>🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 30000 ta\n\n👇 Marhamat kerakli miqdorni kiriting.</b>")

@dp.message_handler(state=Instas.tglink3)
async def tglinki3(message: types.Message, state: FSMContext):
	tglink3 = message.text
	await state.update_data(
        {"tglink3": tglink3}
	)
	data = await state.get_data()
	tgint3 = data.get("tgint3")
	tglink3 = data.get("tglink3")
	TGobunachif3 = open("insta/TGobunachi3.txt","r")
	natija = int(TGobunachif3.read())
	instai = int(tgint3)
	snatija = natija / 1000
	onatija = snatija * instai
	natijalar = "%.2f" % onatija
	msg = f"<b>📇 Malumotlar to'g'riligini tekshring👇\n\n🗞 Buyurtma soni - {tgint3} ta\n🖇 Link - {tglink3}\n💰 Buyurtma narxi - {natijalar}₽</b>"
	TGobunachif3.close()
	await Instas.next()
	await message.answer(msg,reply_markup=confirmation_keyboardTG3)


@dp.callback_query_handler(post_callbackTG3.filter(actionTG3="postTG3"), state=Instas.tgcon3)
async def confirm_TG3(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        tgint3 = data.get("tgint3")
        tglink3 = data.get("tglink3")
        id = call.message.chat.id
        aslbalans = open(f"balans/balans{id}.txt", "r")
        TGobunachif3 = open("insta/TGobunachi3.txt","r")
        innarxi = int(TGobunachif3.read())
        sonib = int(tgint3)
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
        TGobunachif3.close()
        mykey = "badcfb3366718f41450ead89cf954878"
        url = f'https://wiq.ru/api/?key={mykey}&action=create&service=405&quantity={sonib}&link={tglink3}'
        respons = requests.get(url).json()
        resnatija = (respons["order"])
        msg = f"<b>📇Yangi buyurtma ID - {resnatija}\n📌Soni - {sonib} ta\n🖇Link - {tglink3}\n💰Narxi - {natijalar1}₽\n\n✅@NakrutkaiBot</b>"
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>📇Buyurtmangiz qabul qilindi✅\n\n🕐Tez orada buyurtmangiz to'liq bajariladi✅</b>",reply_markup=Menu)
    await bot.send_message(ADMINS[0],msg, parse_mode="HTML")
		
@dp.callback_query_handler(post_callbackTG3.filter(actionTG3="cancelTG3"), state=Instas.tgcon3)
async def cancel_TG3(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>Buyurtmalar bekor qilindi 🛑</b>",reply_markup=Menu)
    
@dp.message_handler(state=Instas.tgcon3)
async def enter_TG3(message: Message, state: FSMContext):
   await message.answer("<b>👆👆👆Quyidagi buyurtmangizni\n✅Tasdiqlang Yoki ❌Rad eting Bo'lmasa Botagi boshqa tugmalar ishlamaydi🔐</b>")
	