from aiogram import types
from loader import dp, bot
from keyboards.default.tarmoq import Torqaga
from aiogram.types import Message, CallbackQuery
from states.instas import Instas
from aiogram.dispatcher import FSMContext
from keyboards.inline.Prinsta2 import confirmation_keyboardP2, post_callbackP2
import requests
import json
from data.config import ADMINS
from keyboards.default.menu import Menu

@dp.callback_query_handler(text_contains="PR2")
async def PR2(call: CallbackQuery):
	instaPr2 = open("insta/instaPr2.txt","r")
	instaPrsi2 = int(instaPr2.read())
	instaPr2.close()
	await call.message.answer(f"<b>👁 1000 ta prosmotr narxi: {instaPrsi2}₽\n\n🔥 Minimal buyurtma: 500 ta\n⚡️ Maksimal buyurtma: 200000 ta\n🔴 Nakrutka Tezligi - Juda Tez\n🚀 Joriy tezlik - (~9104) soatiga\n✅ Realni\n\n👇 Marhamat kerakli miqdorni kiriting.</b>",reply_markup=Torqaga)
	await call.message.delete()
	await call.answer(cache_time=60)
	await Instas.instaPrsi2.set()

@dp.message_handler(state=Instas.instaPrsi2)
async def PR2(message: Message,state: FSMContext):
	id = message.from_user.id
	instaPrsi2 = message.text
	await state.update_data(
		{"instaPrsi2": instaPrsi2}
	)
	try:
		kiriti = int(instaPrsi2)
		if kiriti >= 500:
			balansg = open(f"balans/balans{id}.txt", "r")
			instaPr2 = open("insta/instaPr2.txt","r")
			sumasi = int(instaPr2.read())
			hisobi = float(balansg.read())
		
			donasi = sumasi / 1000
			hisobk = kiriti * donasi
			balansg.close()
			instaPr2.close()
		if hisobi >= hisobk:
			await message.answer(f"<b>📸 Instagram Video + REELS + IGTV Linkini kiriting👇\n\n✅ Masalan: https://www.instagram.com/tv/CcLDnydKPlj/?utm_source=ig_web_copy_link\n\n🔐 Profil ochiq bo'lishi kerak</b>",reply_markup=Torqaga)
			await Instas.instaPrsl2.set()
		else:
			await message.answer(f"<b>💰Hisobingizda yetarli mablag' mavjud emas!</b>")
	except:
		await message.answer("<b>🔥 Minimal buyurtma: 500 ta\n⚡️ Maksimal buyurtma: 200000 ta\n\n👇 Marhamat kerakli miqdorni kiriting.</b>")

@dp.message_handler(state=Instas.instaPrsl2)
async def instaPrs2(message: types.Message, state: FSMContext):
	instaPrsl2 = message.text
	await state.update_data(
        {"instaPrsl2": instaPrsl2}
	)
	data = await state.get_data()
	instaPrsi2 = data.get("instaPrsi2")
	instaPrsl2 = data.get("instaPrsl2")
	instaPr2 = open("insta/instaPr2.txt","r")
	natija = int(instaPr2.read())
	instai = int(instaPrsi2)
	snatija = natija / 1000
	onatija = snatija * instai
	natijalar = "%.2f" % onatija
	msg = f"<b>📇 Malumotlar to'g'riligini tekshring👇\n\n🗞 Buyurtma soni - {instaPrsi2} ta\n🖇 Link - {instaPrsl2}\n💰 Buyurtma narxi - {natijalar}₽</b>"
	instaPr2.close()
	await Instas.next()
	await message.answer(msg,reply_markup=confirmation_keyboardP2)


@dp.callback_query_handler(post_callbackP2.filter(actionP2="postP2"), state=Instas.instapCon2)
async def confirm_Pr2(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        instaPrsi2 = data.get("instaPrsi2")
        instaPrsl2 = data.get("instaPrsl2")
        id = call.message.chat.id
        aslbalans = open(f"balans/balans{id}.txt", "r")
        instaPr2 = open("insta/instaPr2.txt","r")
        innarxi = int(instaPr2.read())
        sonib = int(instaPrsi2)
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
        instaPr2.close()
        mykey = "badcfb3366718f41450ead89cf954878"
        url = f'https://wiq.ru/api/?key={mykey}&action=create&service=145&quantity={sonib}&link={instaPrsl2}'
        respons = requests.get(url).json()
        resnatija = (respons["order"])
        
        msg = f"<b>📇Yangi buyurtma ID - {resnatija}\n📌Soni - {sonib} ta\n🖇Linki- {instaPrsl2}\n💰Narxi - {natijalar1}₽\n\n✅@NakrutkaiBot</b>"
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>📇Buyurtmangiz qabul qilindi✅\n\n🕐Tez orada buyurtmangiz to'liq bajariladi✅</b>",reply_markup=Menu)
    await bot.send_message(ADMINS[0],msg, parse_mode="HTML")
		
@dp.callback_query_handler(post_callbackP2.filter(actionP2="cancelP2"), state=Instas.instapCon2)
async def cancel_Pr2(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>Buyurtmalar bekor qilindi 🛑</b>",reply_markup=Menu)
    
@dp.message_handler(state=Instas.instapCon2)
async def enter_Pr2(message: Message, state: FSMContext):
   await message.answer("<b>👆👆👆Quyidagi buyurtmangizni\n✅Tasdiqlang Yoki ❌Rad eting Bo'lmasa Botagi boshqa tugmalar ishlamaydi🔐</b>")
	