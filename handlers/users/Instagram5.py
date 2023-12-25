from aiogram import types
from loader import dp, bot
from keyboards.default.tarmoq import Torqaga
from aiogram.types import Message, CallbackQuery
from states.instas import Instas
from aiogram.dispatcher import FSMContext
from keyboards.inline.instak5 import confirmation_keyboardi5, post_callbacki5
import requests
import json
from data.config import ADMINS
from keyboards.default.menu import Menu
	
@dp.callback_query_handler(text_contains="KafolatR")
async def KafolatR(call: CallbackQuery):
	instanarxi6 = open("insta/instanarx6.txt","r")
	instanarxis6 = int(instanarxi6.read())
	instanarxi6.close()
	await call.message.answer(f"<b>👤 1000 ta obunachi narxi: {instanarxis6}₽\n\n🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 300000 ta\n🔴 Nakrutka Tezligi - Juda Tez\n🚀 Joriy tezlik - (~49918) soatiga\n✅ Yuqori sifatli\n🛡 Kafolatlangan\n\n👇 Marhamat kerakli miqdorni kiriting.</b>",reply_markup=Torqaga)
	await call.message.delete()
	await call.answer(cache_time=60)
	await Instas.inst5.set()

@dp.message_handler(state=Instas.inst5)
async def insta5(message: Message,state: FSMContext):
	id = message.from_user.id
	inst5 = message.text
	await state.update_data(
		{"inst5": inst5}
	)
	try:
		kiriti = int(inst5)
		if kiriti >= 50:
			balansg = open(f"balans/balans{id}.txt", "r")
			instanarxi6 = open("insta/instanarx6.txt","r")
			sumasi = int(instanarxi6.read())
			hisobi = float(balansg.read())
		
			donasi = sumasi / 1000
			hisobk = kiriti * donasi
			balansg.close()
			instanarxi6.close()
		if hisobi >= hisobk:
			await message.answer(f"<b>📸 Instagram proflingizni kiriting👇\n\n✅ Masalan: 1.we_wolf\n\n🔐 Profil ochiq bo'lishi kerak</b>",reply_markup=Torqaga)
			await Instas.userl5.set()
		else:
			await message.answer(f"<b>💰Hisobingizda yetarli mablag' mavjud emas!</b>")
	except:
		await message.answer("<b>🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 300000 ta\n\n👇 Marhamat kerakli miqdorni kiriting.</b>")

@dp.message_handler(state=Instas.userl5)
async def linku5(message: types.Message, state: FSMContext):
	userl5 = message.text
	await state.update_data(
        {"userl5": userl5}
	)
	data = await state.get_data()
	inst5 = data.get("inst5")
	userl5 = data.get("userl5")
	instanarxi6 = open("insta/instanarx6.txt","r")
	natija = int(instanarxi6.read())
	instai = int(inst5)
	snatija = natija / 1000
	onatija = snatija * instai
	natijalar = "%.2f" % onatija
	msg = f"<b>📇 Malumotlar to'g'riligini tekshring👇\n\n🗞 Buyurtma soni - {inst5} ta\n👤 Profil - {userl5}\n💰 Buyurtma narxi - {natijalar}₽</b>"
	instanarxi6.close()
	await Instas.next()
	await message.answer(msg,reply_markup=confirmation_keyboardi5)


@dp.callback_query_handler(post_callbacki5.filter(actioni5="posti5"), state=Instas.confin5)
async def confirm_insta6(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        inst5 = data.get("inst5")
        userl5 = data.get("userl5")
        id = call.message.chat.id
        aslbalans = open(f"balans/balans{id}.txt", "r")
        instanarxi6 = open("insta/instanarx6.txt","r")
        innarxi = int(instanarxi6.read())
        sonib = int(inst5)
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
        instanarxi6.close()
        mykey = "badcfb3366718f41450ead89cf954878"
        url = f'https://wiq.ru/api/?key={mykey}&action=create&service=53&quantity={sonib}&link=https://www.instagram.com/{userl5}/'
        respons = requests.get(url).json()
        resnatija = (respons["order"])
        
        msg = f"<b>📇Yangi buyurtma ID - {resnatija}\n📌Soni - {sonib} ta\n🖇Profili - {userl5}\n💰Narxi - {natijalar1}₽\n\n✅@NakrutkaiBot</b>"
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>📇Buyurtmangiz qabul qilindi✅\n\n🕐Tez orada buyurtmangiz to'liq bajariladi✅</b>",reply_markup=Menu)
    await bot.send_message(ADMINS[0],msg, parse_mode="HTML")
		
@dp.callback_query_handler(post_callbacki5.filter(actioni5="canceli5"), state=Instas.confin5)
async def cancel_insta6(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>Buyurtmalar bekor qilindi 🛑</b>",reply_markup=Menu)
    
@dp.message_handler(state=Instas.confin5)
async def enter_insta6(message: Message, state: FSMContext):
   await message.answer("<b>👆👆👆Quyidagi buyurtmangizni\n✅Tasdiqlang Yoki ❌Rad eting Bo'lmasa Botagi boshqa tugmalar ishlamaydi🔐</b>")
	