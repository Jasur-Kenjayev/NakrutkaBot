from aiogram import types
from loader import dp, bot
from keyboards.default.tarmoq import Tarmoq, Torqaga
from keyboards.inline.tiktokcat import categoryOTK
from aiogram.types import Message, CallbackQuery
from states.instas import Instas
from aiogram.dispatcher import FSMContext
from keyboards.inline.TKey import confirmation_keyboardTK, post_callbackTK
import requests
import json
from data.config import ADMINS
from keyboards.default.menu import Menu
from keyboards.inline.instatanlash import TKTan

@dp.message_handler(text="⚫ TikTok")
async def TK(message:
	types.Message):
	await message.answer("<b>📲 Kerakli xizmat turini tanlang</b>",reply_markup=TKTan)
	
@dp.callback_query_handler(text_contains="TKObun")
async def TKobunachi(call: CallbackQuery):
	await call.message.answer("<b>📇Marhamat keraklisini tanlang👇</b>",reply_markup=categoryOTK)
	await call.message.delete()
	await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains="TKpodpischik")
async def TKobunachi(call: CallbackQuery):
	tiktok = open("insta/tiktok.txt","r")
	tiktoki = int(tiktok.read())
	tiktok.close()
	await call.message.answer(f"<b>👤 1000 ta obunachi narxi: {tiktoki}₽\n\n🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 100000 ta\n🔴 Nakrutka Tezligi - Sekin\n🚀 Joriy tezlik - Mavjud emas.\n\n👇 Marhamat kerakli miqdorni kiriting.</b>",reply_markup=Torqaga)
	await call.message.delete()
	await call.answer(cache_time=60)
	await Instas.tkint.set()

@dp.message_handler(state=Instas.tkint)
async def tkinput(message: Message,state: FSMContext):
	id = message.from_user.id
	tkint = message.text
	await state.update_data(
		{"tkint": tkint}
	)
	try:
		kiriti = int(tkint)
		if kiriti >= 50:
			balansg = open(f"balans/balans{id}.txt", "r")
			tiktok = open("insta/tiktok.txt","r")
			sumasi = int(tiktok.read())
			hisobi = float(balansg.read())
			
			donasi = sumasi / 1000
			hisobk = kiriti * donasi
			balansg.close()
			tiktok.close()
		if hisobi >= hisobk:
			await message.answer(f"<b>⚫ TikTok profil linkini kiriting👇\n\n✅ Masalan: 1.we_wolf</b>",reply_markup=Torqaga)
			await Instas.tklink.set()
		else:
			await message.answer(f"<b>💰Hisobingizda yetarli mablag' mavjud emas!</b>")
	except:
		await message.answer("<b>🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 100000 ta\n\n👇 Marhamat kerakli miqdorni kiriting.</b>")

@dp.message_handler(state=Instas.tklink)
async def TKlinki(message: types.Message, state: FSMContext):
	tklink = message.text
	await state.update_data(
        {"tklink": tklink}
	)
	data = await state.get_data()
	tkint = data.get("tkint")
	tklink = data.get("tklink")
	tiktok = open("insta/tiktok.txt","r")
	natija = int(tiktok.read())
	instai = int(tkint)
	snatija = natija / 1000
	onatija = snatija * instai
	natijalar = "%.2f" % onatija
	msg = f"<b>📇 Malumotlar to'g'riligini tekshring👇\n\n🗞 Buyurtma soni - {tkint} ta\n🖇 Link - {tklink}\n💰 Buyurtma narxi - {natijalar}₽</b>"
	tiktok.close()
	await Instas.next()
	await message.answer(msg,reply_markup=confirmation_keyboardTK)


@dp.callback_query_handler(post_callbackTK.filter(actionTK="postTK"), state=Instas.tkcon)
async def confirm_TK(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        tkint = data.get("tkint")
        tklink = data.get("tklink")
        id = call.message.chat.id
        aslbalans = open(f"balans/balans{id}.txt", "r")
        tiktok = open("insta/tiktok.txt","r")
        innarxi = int(tiktok.read())
        sonib = int(tkint)
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
        tiktok.close()
        mykey = "badcfb3366718f41450ead89cf954878"
        url = f'https://wiq.ru/api/?key={mykey}&action=create&service=305&quantity={sonib}&link={tklink}'
        respons = requests.get(url).json()
        resnatija = (respons["order"])
        msg = f"<b>📇Yangi buyurtma ID - {resnatija}\n📌Soni - {sonib} ta\n🖇Link - {tklink}\n💰Narxi - {natijalar1}₽\n\n✅@NakrutkaiBot</b>"
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>📇Buyurtmangiz qabul qilindi✅\n\n🕐Tez orada buyurtmangiz to'liq bajariladi✅</b>",reply_markup=Menu)
    await bot.send_message(ADMINS[0],msg, parse_mode="HTML")
		
@dp.callback_query_handler(post_callbackTK.filter(actionTK="cancelTK"), state=Instas.tkcon)
async def cancel_TK(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>Buyurtmalar bekor qilindi 🛑</b>",reply_markup=Menu)
    
@dp.message_handler(state=Instas.tkcon)
async def enter_TK(message: Message, state: FSMContext):
   await message.answer("<b>👆👆👆Quyidagi buyurtmangizni\n✅Tasdiqlang Yoki ❌Rad eting Bo'lmasa Botagi boshqa tugmalar ishlamaydi🔐</b>")
	