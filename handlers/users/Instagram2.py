from aiogram import types
from loader import dp, bot
from keyboards.default.tarmoq import Torqaga
from aiogram.types import Message, CallbackQuery
from states.instas import Instas
from aiogram.dispatcher import FSMContext
from keyboards.inline.instak2 import confirmation_keyboardi2, post_callbacki2
import requests
import json
from data.config import ADMINS
from keyboards.default.menu import Menu
	
@dp.callback_query_handler(text_contains="mixkuzatuvchi")
async def mixkuzatuvchi(call: CallbackQuery):
	instanarxi3 = open("insta/instanarx3.txt","r")
	instanarxis3 = int(instanarxi3.read())
	instanarxi3.close()
	await call.message.answer(f"<b>👤 1000 ta obunachi narxi: {instanarxis3}₽\n\n🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 200000 ta\n🔴 Nakrutka Tezligi - Tez\n🚀 Joriy tezlik - (~12180) soatiga\n\n👇 Marhamat kerakli miqdorni kiriting.</b>",reply_markup=Torqaga)
	await call.message.delete()
	await call.answer(cache_time=60)
	await Instas.inst2.set()

@dp.message_handler(state=Instas.inst2)
async def insta2(message: Message,state: FSMContext):
	id = message.from_user.id
	inst2 = message.text
	await state.update_data(
		{"inst2": inst2}
	)
	try:
		kiriti = int(inst2)
		if kiriti >= 50:
			balansg = open(f"balans/balans{id}.txt", "r")
			instanarxi3 = open("insta/instanarx3.txt","r")
			sumasi = int(instanarxi3.read())
			hisobi = float(balansg.read())
		
			donasi = sumasi / 1000
			hisobk = kiriti * donasi
			balansg.close()
			instanarxi3.close()
		if hisobi >= hisobk:
			await message.answer(f"<b>📸 Instagram proflingizni kiriting👇\n\n✅ Masalan: 1.we_wolf\n\n🔐 Profil ochiq bo'lishi kerak</b>",reply_markup=Torqaga)
			await Instas.userl2.set()
		else:
			await message.answer(f"<b>💰Hisobingizda yetarli mablag' mavjud emas!</b>")
	except:
		await message.answer("<b>🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 200000 ta\n\n👇 Marhamat kerakli miqdorni kiriting.</b>")

@dp.message_handler(state=Instas.userl2)
async def linku2(message: types.Message, state: FSMContext):
	userl2 = message.text
	await state.update_data(
        {"userl2": userl2}
	)
	data = await state.get_data()
	inst2 = data.get("inst2")
	userl2 = data.get("userl2")
	instanarxi3 = open("insta/instanarx3.txt","r")
	natija = int(instanarxi3.read())
	instai = int(inst2)
	snatija = natija / 1000
	onatija = snatija * instai
	natijalar = "%.2f" % onatija
	msg = f"<b>📇 Malumotlar to'g'riligini tekshring👇\n\n🗞 Buyurtma soni - {inst2} ta\n👤 Profil - {userl2}\n💰 Buyurtma narxi - {natijalar}₽</b>"
	instanarxi3.close()
	await Instas.next()
	await message.answer(msg,reply_markup=confirmation_keyboardi2)


@dp.callback_query_handler(post_callbacki2.filter(actioni2="posti2"), state=Instas.confin2)
async def confirm_insta3(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        inst2 = data.get("inst2")
        userl2 = data.get("userl2")
        id = call.message.chat.id
        aslbalans = open(f"balans/balans{id}.txt", "r")
        instanarxi3 = open("insta/instanarx3.txt","r")
        innarxi = int(instanarxi3.read())
        sonib = int(inst2)
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
        instanarxi3.close()
        mykey = "badcfb3366718f41450ead89cf954878"
        url = f'https://wiq.ru/api/?key={mykey}&action=create&service=69&quantity={sonib}&link=https://www.instagram.com/{userl2}/'
        respons = requests.get(url).json()
        resnatija = (respons["order"])
        
        msg = f"<b>📇Yangi buyurtma ID - {resnatija}\n📌Soni - {sonib} ta\n🖇Profili - {userl2}\n💰Narxi - {natijalar1}₽\n\n✅@NakrutkaiBot</b>"
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>📇Buyurtmangiz qabul qilindi✅\n\n🕐Tez orada buyurtmangiz to'liq bajariladi✅</b>",reply_markup=Menu)
    await bot.send_message(ADMINS[0],msg, parse_mode="HTML")
		
@dp.callback_query_handler(post_callbacki2.filter(actioni2="canceli2"), state=Instas.confin2)
async def cancel_insta3(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>Buyurtmalar bekor qilindi 🛑</b>",reply_markup=Menu)
    
@dp.message_handler(state=Instas.confin2)
async def enter_insta3(message: Message, state: FSMContext):
   await message.answer("<b>👆👆👆Quyidagi buyurtmangizni\n✅Tasdiqlang Yoki ❌Rad eting Bo'lmasa Botagi boshqa tugmalar ishlamaydi🔐</b>")
	