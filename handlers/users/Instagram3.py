from aiogram import types
from loader import dp, bot
from keyboards.default.tarmoq import Torqaga
from aiogram.types import Message, CallbackQuery
from states.instas import Instas
from aiogram.dispatcher import FSMContext
from keyboards.inline.instak3 import confirmation_keyboardi3, post_callbacki3
import requests
import json
from data.config import ADMINS
from keyboards.default.menu import Menu
	
@dp.callback_query_handler(text_contains="realluxeo")
async def realluxeo(call: CallbackQuery):
	instanarxi4 = open("insta/instanarx4.txt","r")
	instanarxis4 = int(instanarxi4.read())
	instanarxi4.close()
	await call.message.answer(f"<b>👤 1000 ta obunachi narxi: {instanarxis4}₽\n\n🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 300000 ta\n🔴 Nakrutka Tezligi - Tez\n🚀 Joriy tezlik -  (~8051-15844) soatiga\n\n👇 Marhamat kerakli miqdorni kiriting.</b>",reply_markup=Torqaga)
	await call.message.delete()
	await call.answer(cache_time=60)
	await Instas.inst3.set()

@dp.message_handler(state=Instas.inst3)
async def insta3(message: Message,state: FSMContext):
	id = message.from_user.id
	inst3 = message.text
	await state.update_data(
		{"inst3": inst3}
	)
	try:
		kiriti = int(inst3)
		if kiriti >= 50:
			balansg = open(f"balans/balans{id}.txt", "r")
			instanarxi4 = open("insta/instanarx4.txt","r")
			sumasi = int(instanarxi4.read())
			hisobi = float(balansg.read())
		
			donasi = sumasi / 1000
			hisobk = kiriti * donasi
			balansg.close()
			instanarxi4.close()
		if hisobi >= hisobk:
			await message.answer(f"<b>📸 Instagram proflingizni kiriting👇\n\n✅ Masalan: 1.we_wolf\n\n🔐 Profil ochiq bo'lishi kerak</b>",reply_markup=Torqaga)
			await Instas.userl3.set()
		else:
			await message.answer(f"<b>💰Hisobingizda yetarli mablag' mavjud emas!</b>")
	except:
		await message.answer("<b>🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 300000 ta\n\n👇 Marhamat kerakli miqdorni kiriting.</b>")

@dp.message_handler(state=Instas.userl3)
async def linku3(message: types.Message, state: FSMContext):
	userl3 = message.text
	await state.update_data(
        {"userl3": userl3}
	)
	data = await state.get_data()
	inst3 = data.get("inst3")
	userl3 = data.get("userl3")
	instanarxi4 = open("insta/instanarx4.txt","r")
	natija = int(instanarxi4.read())
	instai = int(inst3)
	snatija = natija / 1000
	onatija = snatija * instai
	natijalar = "%.2f" % onatija
	msg = f"<b>📇 Malumotlar to'g'riligini tekshring👇\n\n🗞 Buyurtma soni - {inst3} ta\n👤 Profil - {userl3}\n💰 Buyurtma narxi - {natijalar}₽</b>"
	instanarxi4.close()
	await Instas.next()
	await message.answer(msg,reply_markup=confirmation_keyboardi3)


@dp.callback_query_handler(post_callbacki3.filter(actioni3="posti3"), state=Instas.confin3)
async def confirm_insta4(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        inst3 = data.get("inst3")
        userl3 = data.get("userl3")
        id = call.message.chat.id
        aslbalans = open(f"balans/balans{id}.txt", "r")
        instanarxi4 = open("insta/instanarx4.txt","r")
        innarxi = int(instanarxi4.read())
        sonib = int(inst3)
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
        instanarxi4.close()
        mykey = "badcfb3366718f41450ead89cf954878"
        url = f'https://wiq.ru/api/?key={mykey}&action=create&service=20&quantity={sonib}&link=https://www.instagram.com/{userl3}/'
        respons = requests.get(url).json()
        resnatija = (respons["order"])
        
        msg = f"<b>📇Yangi buyurtma ID - {resnatija}\n📌Soni - {sonib} ta\n🖇Profili - {userl3}\n💰Narxi - {natijalar1}₽\n\n✅@NakrutkaiBot</b>"
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>📇Buyurtmangiz qabul qilindi✅\n\n🕐Tez orada buyurtmangiz to'liq bajariladi✅</b>",reply_markup=Menu)
    await bot.send_message(ADMINS[0],msg, parse_mode="HTML")
		
@dp.callback_query_handler(post_callbacki3.filter(actioni3="canceli3"), state=Instas.confin3)
async def cancel_insta4(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>Buyurtmalar bekor qilindi 🛑</b>",reply_markup=Menu)
    
@dp.message_handler(state=Instas.confin3)
async def enter_insta4(message: Message, state: FSMContext):
   await message.answer("<b>👆👆👆Quyidagi buyurtmangizni\n✅Tasdiqlang Yoki ❌Rad eting Bo'lmasa Botagi boshqa tugmalar ishlamaydi🔐</b>")
	