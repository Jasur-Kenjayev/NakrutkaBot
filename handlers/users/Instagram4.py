from aiogram import types
from loader import dp, bot
from keyboards.default.tarmoq import Torqaga
from aiogram.types import Message, CallbackQuery
from states.instas import Instas
from aiogram.dispatcher import FSMContext
from keyboards.inline.instak4 import confirmation_keyboardi4, post_callbacki4
import requests
import json
from data.config import ADMINS
from keyboards.default.menu import Menu
	
@dp.callback_query_handler(text_contains="Ar60obun")
async def Ar60obun(call: CallbackQuery):
	instanarxi5 = open("insta/instanarx5.txt","r")
	instanarxis5 = int(instanarxi5.read())
	instanarxi5.close()
	await call.message.answer(f"<b>👤 1000 ta obunachi narxi: {instanarxis5}₽\n\n🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 500000 ta\n🔴 Nakrutka Tezligi - Sekin\n🚀 Joriy tezlik - Mavjud emas\n✅ Yuqori sifatli\n\n👇 Marhamat kerakli miqdorni kiriting.</b>",reply_markup=Torqaga)
	await call.message.delete()
	await call.answer(cache_time=60)
	await Instas.inst4.set()

@dp.message_handler(state=Instas.inst4)
async def insta4(message: Message,state: FSMContext):
	id = message.from_user.id
	inst4 = message.text
	await state.update_data(
		{"inst4": inst4}
	)
	try:
		kiriti = int(inst4)
		if kiriti >= 50:
			balansg = open(f"balans/balans{id}.txt", "r")
			instanarxi5 = open("insta/instanarx5.txt","r")
			sumasi = int(instanarxi5.read())
			hisobi = float(balansg.read())
		
			donasi = sumasi / 1000
			hisobk = kiriti * donasi
			balansg.close()
			instanarxi5.close()
		if hisobi >= hisobk:
			await message.answer(f"<b>📸 Instagram proflingizni kiriting👇\n\n✅ Masalan: 1.we_wolf\n\n🔐 Profil ochiq bo'lishi kerak</b>",reply_markup=Torqaga)
			await Instas.userl4.set()
		else:
			await message.answer(f"<b>💰Hisobingizda yetarli mablag' mavjud emas!</b>")
	except:
		await message.answer("<b>🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 300000 ta\n\n👇 Marhamat kerakli miqdorni kiriting.</b>")

@dp.message_handler(state=Instas.userl4)
async def linku4(message: types.Message, state: FSMContext):
	userl4 = message.text
	await state.update_data(
        {"userl4": userl4}
	)
	data = await state.get_data()
	inst4 = data.get("inst4")
	userl4 = data.get("userl4")
	instanarxi5 = open("insta/instanarx5.txt","r")
	natija = int(instanarxi5.read())
	instai = int(inst4)
	snatija = natija / 1000
	onatija = snatija * instai
	natijalar = "%.2f" % onatija
	msg = f"<b>📇 Malumotlar to'g'riligini tekshring👇\n\n🗞 Buyurtma soni - {inst4} ta\n👤 Profil - {userl4}\n💰 Buyurtma narxi - {natijalar}₽</b>"
	instanarxi5.close()
	await Instas.next()
	await message.answer(msg,reply_markup=confirmation_keyboardi4)


@dp.callback_query_handler(post_callbacki4.filter(actioni4="posti4"), state=Instas.confin4)
async def confirm_insta5(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        inst4 = data.get("inst4")
        userl4 = data.get("userl4")
        id = call.message.chat.id
        aslbalans = open(f"balans/balans{id}.txt", "r")
        instanarxi5 = open("insta/instanarx5.txt","r")
        innarxi = int(instanarxi5.read())
        sonib = int(inst4)
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
        instanarxi5.close()
        mykey = "badcfb3366718f41450ead89cf954878"
        url = f'https://wiq.ru/api/?key={mykey}&action=create&service=70&quantity={sonib}&link=https://www.instagram.com/{userl4}/'
        respons = requests.get(url).json()
        resnatija = (respons["order"])
        
        msg = f"<b>📇Yangi buyurtma ID - {resnatija}\n📌Soni - {sonib} ta\n🖇Profili - {userl4}\n💰Narxi - {natijalar1}₽\n\n✅@NakrutkaiBot</b>"
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>📇Buyurtmangiz qabul qilindi✅\n\n🕐Tez orada buyurtmangiz to'liq bajariladi✅</b>",reply_markup=Menu)
    await bot.send_message(ADMINS[0],msg, parse_mode="HTML")
		
@dp.callback_query_handler(post_callbacki4.filter(actioni4="canceli4"), state=Instas.confin4)
async def cancel_insta5(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>Buyurtmalar bekor qilindi 🛑</b>",reply_markup=Menu)
    
@dp.message_handler(state=Instas.confin4)
async def enter_insta5(message: Message, state: FSMContext):
   await message.answer("<b>👆👆👆Quyidagi buyurtmangizni\n✅Tasdiqlang Yoki ❌Rad eting Bo'lmasa Botagi boshqa tugmalar ishlamaydi🔐</b>")
	