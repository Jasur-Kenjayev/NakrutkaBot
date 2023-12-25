from aiogram import types
from loader import dp, bot
from keyboards.default.tarmoq import Tarmoq, Torqaga
from keyboards.inline.telegramcat import categoryTGPR
from aiogram.types import Message, CallbackQuery
from states.instas import Instas
from aiogram.dispatcher import FSMContext
from keyboards.inline.TGkey5 import confirmation_keyboardTG5, post_callbackTG5
import requests
import json
from data.config import ADMINS
from keyboards.default.menu import Menu

@dp.callback_query_handler(text_contains="tgiprosmotro")
async def tgPros(call: CallbackQuery):
	await call.message.answer("<b>📇Marhamat keraklisini tanlang👇</b>",reply_markup=categoryTGPR)
	await call.message.delete()
	await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains="TGprosmotri")
async def tgobunachii5(call: CallbackQuery):
	TGobunachif5 = open("insta/TGobunachi5.txt","r")
	TGobunachisi5 = int(TGobunachif5.read())
	TGobunachif5.close()
	await call.message.answer(f"<b>👁 1000 ta prosmotr narxi: {TGobunachisi5}₽\n\n🔥 Minimal buyurtma: 500 ta\n⚡️ Maksimal buyurtma: 1000000 ta\n🔴 Nakrutka Tezligi - Tez\n🚀 Joriy tezlik - (~635-7127) soatiga\n\n👇 Marhamat kerakli miqdorni kiriting.</b>",reply_markup=Torqaga)
	await call.message.delete()
	await call.answer(cache_time=60)
	await Instas.tgint5.set()

@dp.message_handler(state=Instas.tgint5)
async def tginput6(message: Message,state: FSMContext):
	id = message.from_user.id
	tgint5 = message.text
	await state.update_data(
		{"tgint5": tgint5}
	)
	try:
		kiriti = int(tgint5)
		if kiriti >= 500:
			balansg = open(f"balans/balans{id}.txt", "r")
			TGobunachif5 = open("insta/TGobunachi5.txt","r")
			sumasi = int(TGobunachif5.read())
			hisobi = float(balansg.read())
		
			donasi = sumasi / 1000
			hisobk = kiriti * donasi
			balansg.close()
			TGobunachif5.close()
		if hisobi >= hisobk:
			await message.answer(f"<b>🔵 Telegram post linkni kiriting👇\n\n✅ Masalan: https://t.me/Python_Koderuz/50</b>",reply_markup=Torqaga)
			await Instas.tglink5.set()
		else:
			await message.answer(f"<b>💰Hisobingizda yetarli mablag' mavjud emas!</b>")
	except:
		await message.answer("<b>🔥 Minimal buyurtma: 500 ta\n⚡️ Maksimal buyurtma: 1000000 ta\n\n👇 Marhamat kerakli miqdorni kiriting.</b>")

@dp.message_handler(state=Instas.tglink5)
async def tglink6i(message: types.Message, state: FSMContext):
	tglink5 = message.text
	await state.update_data(
        {"tglink5": tglink5}
	)
	data = await state.get_data()
	tgint5 = data.get("tgint5")
	tglink5 = data.get("tglink5")
	TGobunachif5 = open("insta/TGobunachi5.txt","r")
	natija = int(TGobunachif5.read())
	instai = int(tgint5)
	snatija = natija / 1000
	onatija = snatija * instai
	natijalar = "%.2f" % onatija
	msg = f"<b>📇 Malumotlar to'g'riligini tekshring👇\n\n🗞 Buyurtma soni - {tgint5} ta\n🖇 Link - {tglink5}\n💰 Buyurtma narxi - {natijalar}₽</b>"
	TGobunachif5.close()
	await Instas.next()
	await message.answer(msg,reply_markup=confirmation_keyboardTG5)


@dp.callback_query_handler(post_callbackTG5.filter(actionTG5="postTG5"), state=Instas.tgcon5)
async def confirm_TG7(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        tgint5 = data.get("tgint5")
        tglink5 = data.get("tglink5")
        id = call.message.chat.id
        aslbalans = open(f"balans/balans{id}.txt", "r")
        TGobunachif5 = open("insta/TGobunachi5.txt","r")
        innarxi = int(TGobunachif5.read())
        sonib = int(tgint5)
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
        TGobunachif5.close()
        mykey = "badcfb3366718f41450ead89cf954878"
        url = f'https://wiq.ru/api/?key={mykey}&action=create&service=2191&quantity={sonib}&link={tglink5}'
        respons = requests.get(url).json()
        resnatija = (respons["order"])
        msg = f"<b>📇Yangi buyurtma ID - {resnatija}\n📌Soni - {sonib} ta\n🖇Link - {tglink5}\n💰Narxi - {natijalar1}₽\n\n✅@NakrutkaiBot</b>"
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>📇Buyurtmangiz qabul qilindi✅\n\n🕐Tez orada buyurtmangiz to'liq bajariladi✅</b>",reply_markup=Menu)
    await bot.send_message(ADMINS[0],msg, parse_mode="HTML")
		
@dp.callback_query_handler(post_callbackTG5.filter(actionTG5="cancelTG5"), state=Instas.tgcon5)
async def cancel_TG7(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>Buyurtmalar bekor qilindi 🛑</b>",reply_markup=Menu)
    
@dp.message_handler(state=Instas.tgcon5)
async def enter_TG7(message: Message, state: FSMContext):
   await message.answer("<b>👆👆👆Quyidagi buyurtmangizni\n✅Tasdiqlang Yoki ❌Rad eting Bo'lmasa Botagi boshqa tugmalar ishlamaydi🔐</b>")
	