from aiogram import types
from loader import dp, bot
from keyboards.default.tarmoq import Torqaga
from aiogram.types import Message, CallbackQuery
from states.instas import Instas
from aiogram.dispatcher import FSMContext
from keyboards.inline.Prinsta3 import confirmation_keyboardP3, post_callbackP3
import requests
import json
from data.config import ADMINS
from keyboards.default.menu import Menu

@dp.callback_query_handler(text_contains="PS2")
async def PS2(call: CallbackQuery):
	instaPr3 = open("insta/instaPr3.txt","r")
	instaPrsi3 = int(instaPr3.read())
	instaPr3.close()
	await call.message.answer(f"<b>👁 1000 ta prosmotr narxi: {instaPrsi3}₽\n\n🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 30000 ta\n🔴 Nakrutka Tezligi - sekin\n🚀 Joriy tezlik - Mavjud emas\n✅ Realni\n\n👇 Marhamat kerakli miqdorni kiriting.</b>",reply_markup=Torqaga)
	await call.message.delete()
	await call.answer(cache_time=60)
	await Instas.instaPrsi3.set()

@dp.message_handler(state=Instas.instaPrsi3)
async def PS2(message: Message,state: FSMContext):
	id = message.from_user.id
	instaPrsi3 = message.text
	await state.update_data(
		{"instaPrsi3": instaPrsi3}
	)
	try:
		kiriti = int(instaPrsi3)
		if kiriti >= 50:
			balansg = open(f"balans/balans{id}.txt", "r")
			instaPr3 = open("insta/instaPr3.txt","r")
			sumasi = int(instaPr3.read())
			hisobi = float(balansg.read())
		
			donasi = sumasi / 1000
			hisobk = kiriti * donasi
			balansg.close()
			instaPr3.close()
		if hisobi >= hisobk:
			await message.answer(f"<b>📸 Instagram Stories Linkini kiriting👇\n\n✅ Masalan: https://instagram.com/stories/1.we_wolf/2813868150780458261?utm_source=ig_story_item_share&igshid=MDJmNzVkMjY=\n\n🔐 Profil ochiq bo'lishi kerak</b>",reply_markup=Torqaga)
			await Instas.instaPrsl3.set()
		else:
			await message.answer(f"<b>💰Hisobingizda yetarli mablag' mavjud emas!</b>")
	except:
		await message.answer("<b>🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 30000 ta\n\n👇 Marhamat kerakli miqdorni kiriting.</b>")

@dp.message_handler(state=Instas.instaPrsl3)
async def instaPr3(message: types.Message, state: FSMContext):
	instaPrsl3 = message.text
	await state.update_data(
        {"instaPrsl3": instaPrsl3}
	)
	data = await state.get_data()
	instaPrsi3 = data.get("instaPrsi3")
	instaPrsl3 = data.get("instaPrsl3")
	instaPr3 = open("insta/instaPr3.txt","r")
	natija = int(instaPr3.read())
	instai = int(instaPrsi3)
	snatija = natija / 1000
	onatija = snatija * instai
	natijalar = "%.2f" % onatija
	msg = f"<b>📇 Malumotlar to'g'riligini tekshring👇\n\n🗞 Buyurtma soni - {instaPrsi3} ta\n🖇 Link - {instaPrsl3}\n💰 Buyurtma narxi - {natijalar}₽</b>"
	instaPr3.close()
	await Instas.next()
	await message.answer(msg,reply_markup=confirmation_keyboardP3)


@dp.callback_query_handler(post_callbackP3.filter(actionP3="postP3"), state=Instas.instapCon3)
async def confirm_PS3(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        instaPrsi3 = data.get("instaPrsi3")
        instaPrsl3 = data.get("instaPrsl3")
        id = call.message.chat.id
        aslbalans = open(f"balans/balans{id}.txt", "r")
        instaPr3 = open("insta/instaPr3.txt","r")
        innarxi = int(instaPr3.read())
        sonib = int(instaPrsi3)
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
        instaPr3.close()
        mykey = "badcfb3366718f41450ead89cf954878"
        url = f'https://wiq.ru/api/?key={mykey}&action=create&service=251&quantity={sonib}&link={instaPrsl3}'
        respons = requests.get(url).json()
        resnatija = (respons["order"])
        
        msg = f"<b>📇Yangi buyurtma ID - {resnatija}\n📌Soni - {sonib} ta\n🖇Linki- {instaPrsl3}\n💰Narxi - {natijalar1}₽\n\n✅@NakrutkaiBot</b>"
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>📇Buyurtmangiz qabul qilindi✅\n\n🕐Tez orada buyurtmangiz to'liq bajariladi✅</b>",reply_markup=Menu)
    await bot.send_message(ADMINS[0],msg, parse_mode="HTML")
		
@dp.callback_query_handler(post_callbackP3.filter(actionP3="cancelP3"), state=Instas.instapCon3)
async def cancel_PS3(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>Buyurtmalar bekor qilindi 🛑</b>",reply_markup=Menu)
    
@dp.message_handler(state=Instas.instapCon3)
async def enter_PS3(message: Message, state: FSMContext):
   await message.answer("<b>👆👆👆Quyidagi buyurtmangizni\n✅Tasdiqlang Yoki ❌Rad eting Bo'lmasa Botagi boshqa tugmalar ishlamaydi🔐</b>")
	