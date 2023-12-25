from aiogram import types
from loader import dp, bot
from keyboards.default.tarmoq import Tarmoq, Torqaga
from keyboards.inline.telegramcat import categoryTG
from keyboards.inline.instatanlash import TGTan 
from aiogram.types import Message, CallbackQuery
from states.instas import Instas
from aiogram.dispatcher import FSMContext
from keyboards.inline.TGkey import confirmation_keyboardTG, post_callbackTG
import requests
import json
from data.config import ADMINS
from keyboards.default.menu import Menu

@dp.message_handler(text="🔵 Telegram")
async def TG(message:
	types.Message):
	await message.answer("<b>📲 Kerakli xizmat turini tanlang</b>",reply_markup=TGTan)

@dp.callback_query_handler(text_contains="tgobunachi")
async def tgobunach(call: CallbackQuery):
	await call.message.answer("<b>📇Marhamat keraklisini tanlang👇</b>",reply_markup=categoryTG)
	await call.message.delete()
	await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains="tgobunach1")
async def tgobunachii1(call: CallbackQuery):
	TGobunachif = open("insta/TGobunachi.txt","r")
	TGobunachisi = int(TGobunachif.read())
	TGobunachif.close()
	await call.message.answer(f"<b>👤 1000 ta obunachi narxi: {TGobunachisi}₽\n\n🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 50000 ta\n🔴 Nakrutka Tezligi - Tez\n🚀 Joriy tezlik -  (~1251-3453) soatiga\n\n👇 Marhamat kerakli miqdorni kiriting.</b>",reply_markup=Torqaga)
	await call.message.delete()
	await call.answer(cache_time=60)
	await Instas.tgint.set()

@dp.message_handler(state=Instas.tgint)
async def tginput(message: Message,state: FSMContext):
	id = message.from_user.id
	tgint = message.text
	await state.update_data(
		{"tgint": tgint}
	)
	try:
		kiriti = int(tgint)
		if kiriti >= 50:
			balansg = open(f"balans/balans{id}.txt", "r")
			TGobunachif = open("insta/TGobunachi.txt","r")
			sumasi = int(TGobunachif.read())
			hisobi = float(balansg.read())
		
			donasi = sumasi / 1000
			hisobk = kiriti * donasi
			balansg.close()
			TGobunachif.close()
		if hisobi >= hisobk:
			await message.answer(f"<b>🔵 Telegram kanal yoki grupa linkni kiriting👇\n\n✅ Masalan: https://t.me/Python_Koderuz</b>",reply_markup=Torqaga)
			await Instas.tglink.set()
		else:
			await message.answer(f"<b>💰Hisobingizda yetarli mablag' mavjud emas!</b>")
	except:
		await message.answer("<b>🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 50000 ta\n\n👇 Marhamat kerakli miqdorni kiriting.</b>")

@dp.message_handler(state=Instas.tglink)
async def tglinki(message: types.Message, state: FSMContext):
	tglink = message.text
	await state.update_data(
        {"tglink": tglink}
	)
	data = await state.get_data()
	tgint = data.get("tgint")
	tglink = data.get("tglink")
	TGobunachif = open("insta/TGobunachi.txt","r")
	natija = int(TGobunachif.read())
	instai = int(tgint)
	snatija = natija / 1000
	onatija = snatija * instai
	natijalar = "%.2f" % onatija
	msg = f"<b>📇 Malumotlar to'g'riligini tekshring👇\n\n🗞 Buyurtma soni - {tgint} ta\n🖇 Link - {tglink}\n💰 Buyurtma narxi - {natijalar}₽</b>"
	TGobunachif.close()
	await Instas.next()
	await message.answer(msg,reply_markup=confirmation_keyboardTG)


@dp.callback_query_handler(post_callbackTG.filter(actionTG="postTG"), state=Instas.tgcon)
async def confirm_TG(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        tgint = data.get("tgint")
        tglink = data.get("tglink")
        id = call.message.chat.id
        aslbalans = open(f"balans/balans{id}.txt", "r")
        TGobunachif = open("insta/TGobunachi.txt","r")
        innarxi = int(TGobunachif.read())
        sonib = int(tgint)
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
        TGobunachif.close()
        mykey = "badcfb3366718f41450ead89cf954878"
        url = f'https://wiq.ru/api/?key={mykey}&action=create&service=419&quantity={sonib}&link={tglink}'
        respons = requests.get(url).json()
        resnatija = (respons["order"])
        msg = f"<b>📇Yangi buyurtma ID - {resnatija}\n📌Soni - {sonib} ta\n🖇Link - {tglink}\n💰Narxi - {natijalar1}₽\n\n✅@NakrutkaiBot</b>"
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>📇Buyurtmangiz qabul qilindi✅\n\n🕐Tez orada buyurtmangiz to'liq bajariladi✅</b>",reply_markup=Menu)
    await bot.send_message(ADMINS[0],msg, parse_mode="HTML")
		
@dp.callback_query_handler(post_callbackTG.filter(actionTG="cancelTG"), state=Instas.tgcon)
async def cancel_TG(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>Buyurtmalar bekor qilindi 🛑</b>",reply_markup=Menu)
    
@dp.message_handler(state=Instas.tgcon)
async def enter_TG(message: Message, state: FSMContext):
   await message.answer("<b>👆👆👆Quyidagi buyurtmangizni\n✅Tasdiqlang Yoki ❌Rad eting Bo'lmasa Botagi boshqa tugmalar ishlamaydi🔐</b>")
	