from aiogram import types
from loader import dp, bot
from keyboards.default.tarmoq import Tarmoq, Torqaga
from keyboards.inline.Youtubecat import categoryYEpros
from aiogram.types import Message, CallbackQuery
from states.instas import Instas
from aiogram.dispatcher import FSMContext
from keyboards.inline.YEkey import confirmation_keyboardYE, post_callbackYE
import requests
import json
from data.config import ADMINS
from keyboards.default.menu import Menu
from keyboards.inline.instatanlash import YETan

@dp.message_handler(text="🟤 YouTube")
async def YE(message:
	types.Message):
	await message.answer("<b>📲 Kerakli xizmat turini tanlang</b>",reply_markup=YETan)
	
@dp.callback_query_handler(text_contains="YEpProsmo")
async def YEprosmotr(call: CallbackQuery):
	await call.message.answer("<b>📇Marhamat keraklisini tanlang👇</b>",reply_markup=categoryYEpros)
	await call.message.delete()
	await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains="YElayk")
async def YEprosmotr(call: CallbackQuery):
	YouTube = open("insta/YouTube.txt","r")
	YouTubee = int(YouTube.read())
	YouTube.close()
	await call.message.answer(f"<b>👁 1000 ta prosmotr narxi: {YouTubee}₽\n\n🔥 Minimal buyurtma: 500 ta\n⚡️ Maksimal buyurtma: 10000000 ta\n🔴 Nakrutka Tezligi - Tez\n🚀 Joriy tezlik - (~287-336) Soatiga\n\n👇 Marhamat kerakli miqdorni kiriting.</b>",reply_markup=Torqaga)
	await call.message.delete()
	await call.answer(cache_time=60)
	await Instas.yeint.set()

@dp.message_handler(state=Instas.yeint)
async def yeinput(message: Message,state: FSMContext):
	id = message.from_user.id
	yeint = message.text
	await state.update_data(
		{"yeint": yeint}
	)
	try:
		kiriti = int(yeint)
		if kiriti >= 500:
			balansg = open(f"balans/balans{id}.txt", "r")
			YouTube = open("insta/YouTube.txt","r")
			sumasi = int(YouTube.read())
			hisobi = float(balansg.read())
			
			donasi = sumasi / 1000
			hisobk = kiriti * donasi
			balansg.close()
			YouTube.close()
		if hisobi >= hisobk:
			await message.answer(f"<b>🎞 YouTube video linkini kiriting👇\n\n✅ Masalan: https://youtu.be/vqLoGp1u76w</b>",reply_markup=Torqaga)
			await Instas.yelink.set()
		else:
			await message.answer(f"<b>💰Hisobingizda yetarli mablag' mavjud emas!</b>")
	except:
		await message.answer("<b>🔥 Minimal buyurtma: 500 ta\n⚡️ Maksimal buyurtma: 10000000 ta\n\n👇 Marhamat kerakli miqdorni kiriting.</b>")

@dp.message_handler(state=Instas.yelink)
async def YElinki(message: types.Message, state: FSMContext):
	yelink = message.text
	await state.update_data(
        {"yelink": yelink}
	)
	data = await state.get_data()
	yeint = data.get("yeint")
	yelink = data.get("yelink")
	YouTube = open("insta/YouTube.txt","r")
	natija = int(YouTube.read())
	instai = int(yeint)
	snatija = natija / 1000
	onatija = snatija * instai
	natijalar = "%.2f" % onatija
	msg = f"<b>📇 Malumotlar to'g'riligini tekshring👇\n\n🗞 Buyurtma soni - {yeint} ta\n🖇 Link - {yelink}\n💰 Buyurtma narxi - {natijalar}₽</b>"
	YouTube.close()
	await Instas.next()
	await message.answer(msg,reply_markup=confirmation_keyboardYE)


@dp.callback_query_handler(post_callbackYE.filter(actionYE="postYE"), state=Instas.yecon)
async def confirm_YE(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        yeint = data.get("yeint")
        yelink = data.get("yelink")
        id = call.message.chat.id
        aslbalans = open(f"balans/balans{id}.txt", "r")
        YouTube = open("insta/YouTube.txt","r")
        innarxi = int(YouTube.read())
        sonib = int(yeint)
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
        YouTube.close()
        mykey = "badcfb3366718f41450ead89cf954878"
        url = f'https://wiq.ru/api/?key={mykey}&action=create&service=227&quantity={sonib}&link={yelink}'
        respons = requests.get(url).json()
        resnatija = (respons["order"])
        msg = f"<b>📇Yangi buyurtma ID - {resnatija}\n📌Soni - {sonib} ta\n🖇Link - {yelink}\n💰Narxi - {natijalar1}₽\n\n✅@NakrutkaiBot</b>"
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>📇Buyurtmangiz qabul qilindi✅\n\n🕐Tez orada buyurtmangiz to'liq bajariladi✅</b>",reply_markup=Menu)
    await bot.send_message(ADMINS[0],msg, parse_mode="HTML")
		
@dp.callback_query_handler(post_callbackYE.filter(actionYE="cancelYE"), state=Instas.yecon)
async def cancel_YE(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>Buyurtmalar bekor qilindi 🛑</b>",reply_markup=Menu)
    
@dp.message_handler(state=Instas.yecon)
async def enter_YE(message: Message, state: FSMContext):
   await message.answer("<b>👆👆👆Quyidagi buyurtmangizni\n✅Tasdiqlang Yoki ❌Rad eting Bo'lmasa Botagi boshqa tugmalar ishlamaydi🔐</b>")
	