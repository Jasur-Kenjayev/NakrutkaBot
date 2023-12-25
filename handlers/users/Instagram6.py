from aiogram import types
from loader import dp, bot
from keyboards.default.tarmoq import Torqaga
from aiogram.types import Message, CallbackQuery
from states.instas import Instas
from aiogram.dispatcher import FSMContext
from keyboards.inline.instak6 import confirmation_keyboardi6, post_callbacki6
import requests
import json
from data.config import ADMINS
from keyboards.default.menu import Menu
	
@dp.callback_query_handler(text_contains="realbekorqi")
async def realbekorqi(call: CallbackQuery):
	instanarxi7 = open("insta/instanarx7.txt","r")
	instanarxis7 = int(instanarxi7.read())
	instanarxi7.close()
	await call.message.answer(f"<b>👤 1000 ta obunachi narxi: {instanarxis7}₽\n\n🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 20000 ta\n🔴 Nakrutka Tezligi - Juda Tez\n🚀 Joriy tezlik - (~462) soat\n✅ Yuqori sifatli\n🛡 Kafolatlangan\n\n👇 Marhamat kerakli miqdorni kiriting.</b>",reply_markup=Torqaga)
	await call.message.delete()
	await call.answer(cache_time=60)
	await Instas.inst6.set()

@dp.message_handler(state=Instas.inst6)
async def insta6(message: Message,state: FSMContext):
	id = message.from_user.id
	inst6 = message.text
	await state.update_data(
		{"inst6": inst6}
	)
	try:
		kiriti = int(inst6)
		if kiriti >= 50:
			balansg = open(f"balans/balans{id}.txt", "r")
			instanarxi7 = open("insta/instanarx7.txt","r")
			sumasi = int(instanarxi7.read())
			hisobi = float(balansg.read())
		
			donasi = sumasi / 1000
			hisobk = kiriti * donasi
			balansg.close()
			instanarxi7.close()
		if hisobi >= hisobk:
			await message.answer(f"<b>📸 Instagram proflingizni kiriting👇\n\n✅ Masalan: 1.we_wolf\n\n🔐 Profil ochiq bo'lishi kerak</b>",reply_markup=Torqaga)
			await Instas.userl6.set()
		else:
			await message.answer(f"<b>💰Hisobingizda yetarli mablag' mavjud emas!</b>")
	except:
		await message.answer("<b>🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 20000 ta\n\n👇 Marhamat kerakli miqdorni kiriting.</b>")

@dp.message_handler(state=Instas.userl6)
async def linku6(message: types.Message, state: FSMContext):
	userl6 = message.text
	await state.update_data(
        {"userl6": userl6}
	)
	data = await state.get_data()
	inst6 = data.get("inst6")
	userl6 = data.get("userl6")
	instanarxi7 = open("insta/instanarx7.txt","r")
	natija = int(instanarxi7.read())
	instai = int(inst6)
	snatija = natija / 1000
	onatija = snatija * instai
	natijalar = "%.2f" % onatija
	msg = f"<b>📇 Malumotlar to'g'riligini tekshring👇\n\n🗞 Buyurtma soni - {inst6} ta\n👤 Profil - {userl6}\n💰 Buyurtma narxi - {natijalar}₽</b>"
	instanarxi7.close()
	await Instas.next()
	await message.answer(msg,reply_markup=confirmation_keyboardi6)


@dp.callback_query_handler(post_callbacki6.filter(actioni6="posti6"), state=Instas.confin6)
async def confirm_insta7(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        inst6 = data.get("inst6")
        userl6 = data.get("userl6")
        id = call.message.chat.id
        aslbalans = open(f"balans/balans{id}.txt", "r")
        instanarxi7 = open("insta/instanarx7.txt","r")
        innarxi = int(instanarxi7.read())
        sonib = int(inst6)
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
        instanarxi7.close()
        mykey = "badcfb3366718f41450ead89cf954878"
        url = f'https://wiq.ru/api/?key={mykey}&action=create&service=62&quantity={sonib}&link=https://www.instagram.com/{userl6}/'
        respons = requests.get(url).json()
        resnatija = (respons["order"])
        
        msg = f"<b>📇Yangi buyurtma ID - {resnatija}\n📌Soni - {sonib} ta\n🖇Profili - {userl6}\n💰Narxi - {natijalar1}₽\n\n✅@NakrutkaiBot</b>"
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>📇Buyurtmangiz qabul qilindi✅\n\n🕐Tez orada buyurtmangiz to'liq bajariladi✅</b>",reply_markup=Menu)
    await bot.send_message(ADMINS[0],msg, parse_mode="HTML")
		
@dp.callback_query_handler(post_callbacki6.filter(actioni6="canceli6"), state=Instas.confin6)
async def cancel_insta7(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>Buyurtmalar bekor qilindi 🛑</b>",reply_markup=Menu)
    
@dp.message_handler(state=Instas.confin6)
async def enter_insta7(message: Message, state: FSMContext):
   await message.answer("<b>👆👆👆Quyidagi buyurtmangizni\n✅Tasdiqlang Yoki ❌Rad eting Bo'lmasa Botagi boshqa tugmalar ishlamaydi🔐</b>")
	