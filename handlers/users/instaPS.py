from aiogram import types
from loader import dp, bot
from keyboards.default.tarmoq import Torqaga
from aiogram.types import Message, CallbackQuery
from states.instas import Instas
from aiogram.dispatcher import FSMContext
from keyboards.inline.Prinsta1 import confirmation_keyboardP1, post_callbackP1
import requests
import json
from data.config import ADMINS
from keyboards.default.menu import Menu

@dp.callback_query_handler(text_contains="PS1")
async def PS1(call: CallbackQuery):
	instaPr1 = open("insta/instaPr1.txt","r")
	instaPrsi1 = int(instaPr1.read())
	instaPr1.close()
	await call.message.answer(f"<b>👁 1000 ta prosmotr narxi: {instaPrsi1}₽\n\n🔥 Minimal buyurtma: 500 ta\n⚡️ Maksimal buyurtma: 5000 ta\n🔴 Nakrutka Tezligi - Juda Tez\n🚀 Joriy tezlik - (~528) soat\n\n👇 Marhamat kerakli miqdorni kiriting.</b>",reply_markup=Torqaga)
	await call.message.delete()
	await call.answer(cache_time=60)
	await Instas.instaPrsi1.set()

@dp.message_handler(state=Instas.instaPrsi1)
async def PSi(message: Message,state: FSMContext):
	id = message.from_user.id
	instaPrsi1 = message.text
	await state.update_data(
		{"instaPrsi1": instaPrsi1}
	)
	try:
		kiriti = int(instaPrsi1)
		if kiriti >= 500:
			balansg = open(f"balans/balans{id}.txt", "r")
			instaPr1 = open("insta/instaPr1.txt","r")
			sumasi = int(instaPr1.read())
			hisobi = float(balansg.read())
		
			donasi = sumasi / 1000
			hisobk = kiriti * donasi
			balansg.close()
			instaPr1.close()
		if hisobi >= hisobk:
			await message.answer(f"<b>📸 Instagram Stories Linkini kiriting👇\n\n✅ Masalan: https://instagram.com/stories/1.we_wolf/2813868150780458261?utm_source=ig_story_item_share&igshid=MDJmNzVkMjY=\n\n🔐 Profil ochiq bo'lishi kerak</b>",reply_markup=Torqaga)
			await Instas.instaPrsl1.set()
		else:
			await message.answer(f"<b>💰Hisobingizda yetarli mablag' mavjud emas!</b>")
	except:
		await message.answer("<b>🔥 Minimal buyurtma: 500 ta\n⚡️ Maksimal buyurtma: 5000 ta\n\n👇 Marhamat kerakli miqdorni kiriting.</b>")

@dp.message_handler(state=Instas.instaPrsl1)
async def instaPrsl1(message: types.Message, state: FSMContext):
	instaPrsl1 = message.text
	await state.update_data(
        {"instaPrsl1": instaPrsl1}
	)
	data = await state.get_data()
	instaPrsi1 = data.get("instaPrsi1")
	instaPrsl1 = data.get("instaPrsl1")
	instaPr1 = open("insta/instaPr1.txt","r")
	natija = int(instaPr1.read())
	instai = int(instaPrsi1)
	snatija = natija / 1000
	onatija = snatija * instai
	natijalar = "%.2f" % onatija
	msg = f"<b>📇 Malumotlar to'g'riligini tekshring👇\n\n🗞 Buyurtma soni - {instaPrsi1} ta\n🖇 Link - {instaPrsl1}\n💰 Buyurtma narxi - {natijalar}₽</b>"
	instaPr1.close()
	await Instas.next()
	await message.answer(msg,reply_markup=confirmation_keyboardP1)


@dp.callback_query_handler(post_callbackP1.filter(actionP1="postP1"), state=Instas.instapCon1)
async def confirm_Prs1(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        instaPrsi1 = data.get("instaPrsi1")
        instaPrsl1 = data.get("instaPrsl1")
        id = call.message.chat.id
        aslbalans = open(f"balans/balans{id}.txt", "r")
        instaPr1 = open("insta/instaPr1.txt","r")
        innarxi = int(instaPr1.read())
        sonib = int(instaPrsi1)
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
        instaPr1.close()
        mykey = "badcfb3366718f41450ead89cf954878"
        url = f'https://wiq.ru/api/?key={mykey}&action=create&service=74&quantity={sonib}&link={instaPrsl1}'
        respons = requests.get(url).json()
        resnatija = (respons["order"])
        
        msg = f"<b>📇Yangi buyurtma ID - {resnatija}\n📌Soni - {sonib} ta\n🖇Linki- {instaPrsl1}\n💰Narxi - {natijalar1}₽\n\n✅@NakrutkaiBot</b>"
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>📇Buyurtmangiz qabul qilindi✅\n\n🕐Tez orada buyurtmangiz to'liq bajariladi✅</b>",reply_markup=Menu)
    await bot.send_message(ADMINS[0],msg, parse_mode="HTML")
		
@dp.callback_query_handler(post_callbackP1.filter(actionP1="cancelP1"), state=Instas.instapCon1)
async def cancel_Pr1(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>Buyurtmalar bekor qilindi 🛑</b>",reply_markup=Menu)
    
@dp.message_handler(state=Instas.instapCon1)
async def enter_Pr1(message: Message, state: FSMContext):
   await message.answer("<b>👆👆👆Quyidagi buyurtmangizni\n✅Tasdiqlang Yoki ❌Rad eting Bo'lmasa Botagi boshqa tugmalar ishlamaydi🔐</b>")
	