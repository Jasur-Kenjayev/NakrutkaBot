from aiogram import types
from loader import dp, bot
from keyboards.default.tarmoq import Tarmoq, Torqaga
from keyboards.inline.instam import categoryMenu
from keyboards.inline.instatanlash import instaTan
from aiogram.types import Message, CallbackQuery
from states.instas import Instas
from aiogram.dispatcher import FSMContext
from keyboards.inline.instake import confirmation_keyboardi, post_callbacki
import requests
import json
from data.config import ADMINS
from keyboards.default.menu import Menu

@dp.message_handler(text="🔙 Orqaga",state=Instas)
async def norqaga(message:
	types.Message, state: FSMContext):
	await state.finish()
	await message.answer("<b>📇Buyurtma bekor qilindi✅</b>",reply_markup=Tarmoq)
	
@dp.message_handler(text="🔴 Instagram")
async def insta(message:
	types.Message):
	await message.answer("<b>📲 Kerakli xizmat turini tanlang</b>",reply_markup=instaTan)

@dp.callback_query_handler(text_contains="instaObun")
async def instaobunachi(call: CallbackQuery):
	await call.message.answer("<b>📇Marhamat keraklisini tanlang👇</b>",reply_markup=categoryMenu)
	await call.message.delete()
	await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains="bezga")
async def bezga(call: CallbackQuery):
	instanarxi1 = open("insta/instanarx1.txt","r")
	instanarxis1 = int(instanarxi1.read())
	instanarxi1.close()
	await call.message.answer(f"<b>👤 1000 ta obunachi narxi: {instanarxis1}₽\n\n🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 50000 ta\n🔴 Nakrutka Tezligi - Sekin\n🚀 Joriy tezlik Soatiga - Mavjud emas\n\n👇 Marhamat kerakli miqdorni kiriting.</b>",reply_markup=Torqaga)
	await call.message.delete()
	await call.answer(cache_time=60)
	await Instas.inst.set()

@dp.message_handler(state=Instas.inst)
async def instast(message: Message,state: FSMContext):
	id = message.from_user.id
	inst = message.text
	await state.update_data(
		{"inst": inst}
	)
	try:
		kiriti = int(inst)
		if kiriti >= 50:
			balansg = open(f"balans/balans{id}.txt", "r")
			instan = open("insta/instanarx1.txt","r")
			sumasi = int(instan.read())
			hisobi = float(balansg.read())
			donasi = sumasi / 1000
			hisobk = kiriti * donasi
			balansg.close()
			instan.close()
		if hisobi >= hisobk:
			await message.answer(f"<b>📸 Instagram proflingizni kiriting👇\n\n✅ Masalan: 1.we_wolf\n\n🔐 Profil ochiq bo'lishi kerak</b>",reply_markup=Torqaga)
			await Instas.userl.set()
		else:
			await message.answer(f"<b>💰Hisobingizda yetarli mablag' mavjud emas!</b>")
	except:
		await message.answer("<b>🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 50000 ta\n\n👇 Marhamat kerakli miqdorni kiriting.</b>")

@dp.message_handler(state=Instas.userl)
async def linku(message: types.Message, state: FSMContext):
	userl = message.text
	await state.update_data(
        {"userl": userl}
	)
	data = await state.get_data()
	inst = data.get("inst")
	userl = data.get("userl")
	instan = open("insta/instanarx1.txt","r")
	natija = int(instan.read())
	instai = int(inst)
	snatija = natija / 1000
	onatija = snatija * instai
	natijalar = "%.2f" % onatija
	msg = f"<b>📇 Malumotlar to'g'riligini tekshring👇\n\n🗞 Buyurtma soni - {inst} ta\n👤 Profil - {userl}\n💰 Buyurtma narxi - {natijalar}₽</b>"
	instan.close()
	await Instas.next()
	await message.answer(msg,reply_markup=confirmation_keyboardi)


@dp.callback_query_handler(post_callbacki.filter(actioni="posti"), state=Instas.confin)
async def confirm_insta1(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        inst = data.get("inst")
        userl = data.get("userl")
        id = call.message.chat.id
        aslbalans = open(f"balans/balans{id}.txt", "r")
        instan = open("insta/instanarx1.txt","r")
        innarxi = int(instan.read())
        sonib = int(inst)
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
        instan.close()
        mykey = "badcfb3366718f41450ead89cf954878"
        url = f'https://wiq.ru/api/?key={mykey}&action=create&service=3&quantity={sonib}&link=https://www.instagram.com/{userl}/'
        respons = requests.get(url).json()
        resnatija = (respons["order"])
        msg = f"<b>📇Yangi buyurtma ID - {resnatija}\n📌Soni - {sonib} ta\n🖇Profili - {userl}\n💰Narxi - {natijalar1}₽\n\n✅@NakrutkaiBot</b>"
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>📇Buyurtmangiz qabul qilindi✅\n\n🕐Tez orada buyurtmangiz to'liq bajariladi✅</b>",reply_markup=Menu)
    await bot.send_message(ADMINS[0],msg, parse_mode="HTML")
		
@dp.callback_query_handler(post_callbacki.filter(actioni="canceli"), state=Instas.confin)
async def cancel_insta1(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>Buyurtmalar bekor qilindi 🛑</b>",reply_markup=Menu)
    
@dp.message_handler(state=Instas.confin)
async def enter_insta1f(message: Message, state: FSMContext):
   await message.answer("<b>👆👆👆Quyidagi buyurtmangizni\n✅Tasdiqlang Yoki ❌Rad eting Bo'lmasa Botagi boshqa tugmalar ishlamaydi🔐</b>")
	