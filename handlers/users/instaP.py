from aiogram import types
from loader import dp, bot
from keyboards.default.tarmoq import Torqaga
from aiogram.types import Message, CallbackQuery
from states.instas import Instas
from aiogram.dispatcher import FSMContext
from keyboards.inline.Prinsta import confirmation_keyboardP, post_callbackP
import requests
import json
from data.config import ADMINS
from keyboards.default.menu import Menu
from keyboards.inline.instaPR import categoryPros

@dp.callback_query_handler(text_contains="instaProsmo")
async def instaProsm(call: CallbackQuery):
	await call.message.answer("<b>📇Marhamat keraklisini tanlang👇</b>",reply_markup=categoryPros)
	await call.message.delete()
	await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains="PR1")
async def PR1(call: CallbackQuery):
	instaPr = open("insta/instaPr.txt","r")
	instaPrsi = int(instaPr.read())
	instaPr.close()
	await call.message.answer(f"<b>👁 1000 ta prosmotr narxi: {instaPrsi}₽\n\n🔥 Minimal buyurtma: 100 ta\n⚡️ Maksimal buyurtma: 5000000 ta\n🔴 Nakrutka Tezligi - Juda Tez\n🚀 Joriy tezlik - (~15828-18465) soatiga\n\n👇 Marhamat kerakli miqdorni kiriting.</b>",reply_markup=Torqaga)
	await call.message.delete()
	await call.answer(cache_time=60)
	await Instas.instaPrsi.set()

@dp.message_handler(state=Instas.instaPrsi)
async def insta6(message: Message,state: FSMContext):
	id = message.from_user.id
	instaPrsi = message.text
	await state.update_data(
		{"instaPrsi": instaPrsi}
	)
	try:
		kiriti = int(instaPrsi)
		if kiriti >= 100:
			balansg = open(f"balans/balans{id}.txt", "r")
			instaPr = open("insta/instaPr.txt","r")
			sumasi = int(instaPr.read())
			hisobi = float(balansg.read())
		
			donasi = sumasi / 1000
			hisobk = kiriti * donasi
			balansg.close()
			instaPr.close()
		if hisobi >= hisobk:
			await message.answer(f"<b>📸 Instagram Video + REELS + IGTV Linkini kiriting👇\n\n✅ Masalan: https://www.instagram.com/tv/CcLDnydKPlj/?utm_source=ig_web_copy_link\n\n🔐 Profil ochiq bo'lishi kerak</b>",reply_markup=Torqaga)
			await Instas.instaPrsl.set()
		else:
			await message.answer(f"<b>💰Hisobingizda yetarli mablag' mavjud emas!</b>")
	except:
		await message.answer("<b>🔥 Minimal buyurtma: 100 ta\n⚡️ Maksimal buyurtma: 5000000 ta\n\n👇 Marhamat kerakli miqdorni kiriting.</b>")

@dp.message_handler(state=Instas.instaPrsl)
async def instaPrsl(message: types.Message, state: FSMContext):
	instaPrsl = message.text
	await state.update_data(
        {"instaPrsl": instaPrsl}
	)
	data = await state.get_data()
	instaPrsi = data.get("instaPrsi")
	instaPrsl = data.get("instaPrsl")
	instaPr = open("insta/instaPr.txt","r")
	natija = int(instaPr.read())
	instai = int(instaPrsi)
	snatija = natija / 1000
	onatija = snatija * instai
	natijalar = "%.2f" % onatija
	msg = f"<b>📇 Malumotlar to'g'riligini tekshring👇\n\n🗞 Buyurtma soni - {instaPrsi} ta\n🖇 Link - {instaPrsl}\n💰 Buyurtma narxi - {natijalar}₽</b>"
	instaPr.close()
	await Instas.next()
	await message.answer(msg,reply_markup=confirmation_keyboardP)


@dp.callback_query_handler(post_callbackP.filter(actionP="postP"), state=Instas.instapCon)
async def confirm_Prs(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        instaPrsi = data.get("instaPrsi")
        instaPrsl = data.get("instaPrsl")
        id = call.message.chat.id
        aslbalans = open(f"balans/balans{id}.txt", "r")
        instaPr = open("insta/instaPr.txt","r")
        innarxi = int(instaPr.read())
        sonib = int(instaPrsi)
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
        instaPr.close()
        mykey = "badcfb3366718f41450ead89cf954878"
        url = f'https://wiq.ru/api/?key={mykey}&action=create&service=61&quantity={sonib}&link={instaPrsl}'
        respons = requests.get(url).json()
        resnatija = (respons["order"])
        
        msg = f"<b>📇Yangi buyurtma ID - {resnatija}\n📌Soni - {sonib} ta\n🖇Linki- {instaPrsl}\n💰Narxi - {natijalar1}₽\n\n✅@NakrutkaiBot</b>"
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>📇Buyurtmangiz qabul qilindi✅\n\n🕐Tez orada buyurtmangiz to'liq bajariladi✅</b>",reply_markup=Menu)
    await bot.send_message(ADMINS[0],msg, parse_mode="HTML")
		
@dp.callback_query_handler(post_callbackP.filter(actionP="cancelP"), state=Instas.instapCon)
async def cancel_Pr(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>Buyurtmalar bekor qilindi 🛑</b>",reply_markup=Menu)
    
@dp.message_handler(state=Instas.instapCon)
async def enter_Pr(message: Message, state: FSMContext):
   await message.answer("<b>👆👆👆Quyidagi buyurtmangizni\n✅Tasdiqlang Yoki ❌Rad eting Bo'lmasa Botagi boshqa tugmalar ishlamaydi🔐</b>")
	