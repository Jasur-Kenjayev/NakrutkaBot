from aiogram import types
from loader import dp, bot
from keyboards.default.tarmoq import Tarmoq, Torqaga
from keyboards.inline.vkcat import categoryVK
from keyboards.inline.instatanlash import vkTan 
from aiogram.types import Message, CallbackQuery
from states.instas import Instas
from aiogram.dispatcher import FSMContext
from keyboards.inline.VKKey import confirmation_keyboardVK, post_callbackVK
import requests
import json
from data.config import ADMINS
from keyboards.default.menu import Menu

@dp.message_handler(text="🟣 VKontakte")
async def Vk(message:
	types.Message):
	await message.answer("<b>📲 Kerakli xizmat turini tanlang</b>",reply_markup=vkTan)

@dp.callback_query_handler(text_contains="vkobunachi")
async def vkobunachi(call: CallbackQuery):
	await call.message.answer("<b>📇Marhamat keraklisini tanlang👇</b>",reply_markup=categoryVK)
	await call.message.delete()
	await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains="vkpodpischik")
async def vkpodpischik(call: CallbackQuery):
	VKobunachi = open("insta/VKobunachi.txt","r")
	VKobunachisi = int(VKobunachi.read())
	VKobunachi.close()
	await call.message.answer(f"<b>👤 1000 ta obunachi narxi: {VKobunachisi}₽\n\n🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 35000 ta\n🔴 Nakrutka Tezligi - Tez\n🚀 Joriy tezlik - (~3145-3388) soatiga\n\n👇 Marhamat kerakli miqdorni kiriting.</b>",reply_markup=Torqaga)
	await call.message.delete()
	await call.answer(cache_time=60)
	await Instas.vkin.set()

@dp.message_handler(state=Instas.vkin)
async def vkinput(message: Message,state: FSMContext):
	id = message.from_user.id
	vkin = message.text
	await state.update_data(
		{"vkin": vkin}
	)
	try:
		kiriti = int(vkin)
		if kiriti >= 50:
			balansg = open(f"balans/balans{id}.txt", "r")
			VKobunachi = open("insta/VKobunachi.txt","r")
			sumasi = int(VKobunachi.read())
			hisobi = float(balansg.read())
		
			donasi = sumasi / 1000
			hisobk = kiriti * donasi
			balansg.close()
			VKobunachi.close()
		if hisobi >= hisobk:
			await message.answer(f"<b>💬 VKontakte proflingizni kiriting👇\n\n✅ Masalan: https://m.vk.com/id718916597</b>",reply_markup=Torqaga)
			await Instas.vklink.set()
		else:
			await message.answer(f"<b>💰Hisobingizda yetarli mablag' mavjud emas!</b>")
	except:
		await message.answer("<b>🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 35000 ta\n\n👇 Marhamat kerakli miqdorni kiriting.</b>")

@dp.message_handler(state=Instas.vklink)
async def vklinki(message: types.Message, state: FSMContext):
	vklink = message.text
	await state.update_data(
        {"vklink": vklink}
	)
	data = await state.get_data()
	vkin = data.get("vkin")
	vklink = data.get("vklink")
	VKobunachi = open("insta/VKobunachi.txt","r")
	natija = int(VKobunachi.read())
	instai = int(vkin)
	snatija = natija / 1000
	onatija = snatija * instai
	natijalar = "%.2f" % onatija
	msg = f"<b>📇 Malumotlar to'g'riligini tekshring👇\n\n🗞 Buyurtma soni - {vkin} ta\n👤 Profil - {vklink}\n💰 Buyurtma narxi - {natijalar}₽</b>"
	VKobunachi.close()
	await Instas.next()
	await message.answer(msg,reply_markup=confirmation_keyboardVK)


@dp.callback_query_handler(post_callbackVK.filter(actionVK="postVK"), state=Instas.vkcon)
async def confirm_VK(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        vkin = data.get("vkin")
        vklink = data.get("vklink")
        id = call.message.chat.id
        aslbalans = open(f"balans/balans{id}.txt", "r")
        VKobunachi = open("insta/VKobunachi.txt","r")
        innarxi = int(VKobunachi.read())
        sonib = int(vkin)
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
        VKobunachi.close()
        mykey = "badcfb3366718f41450ead89cf954878"
        url = f'https://wiq.ru/api/?key={mykey}&action=create&service=350&quantity={sonib}&link={vklink}'
        respons = requests.get(url).json()
        resnatija = (respons["order"])
        msg = f"<b>📇Yangi buyurtma ID - {resnatija}\n📌Soni - {sonib} ta\n🖇Profili - {vklink}\n💰Narxi - {natijalar1}₽\n\n✅@NakrutkaiBot</b>"
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>📇Buyurtmangiz qabul qilindi✅\n\n🕐Tez orada buyurtmangiz to'liq bajariladi✅</b>",reply_markup=Menu)
    await bot.send_message(ADMINS[0],msg, parse_mode="HTML")
		
@dp.callback_query_handler(post_callbackVK.filter(actionVK="cancelVK"), state=Instas.vkcon)
async def cancel_VK(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>Buyurtmalar bekor qilindi 🛑</b>",reply_markup=Menu)
    
@dp.message_handler(state=Instas.vkcon)
async def enter_VK(message: Message, state: FSMContext):
   await message.answer("<b>👆👆👆Quyidagi buyurtmangizni\n✅Tasdiqlang Yoki ❌Rad eting Bo'lmasa Botagi boshqa tugmalar ishlamaydi🔐</b>")
	