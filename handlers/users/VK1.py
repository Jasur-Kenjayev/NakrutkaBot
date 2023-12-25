from aiogram import types
from loader import dp, bot
from keyboards.default.tarmoq import Tarmoq, Torqaga
from keyboards.inline.vkcat import categoryVKLike
from aiogram.types import Message, CallbackQuery
from states.instas import Instas
from aiogram.dispatcher import FSMContext
from keyboards.inline.VKKey1 import confirmation_keyboardVK1, post_callbackVK1
import requests
import json
from data.config import ADMINS
from keyboards.default.menu import Menu

@dp.callback_query_handler(text_contains="vklikep")
async def vklikeb(call: CallbackQuery):
	await call.message.answer("<b>📇Marhamat keraklisini tanlang👇</b>",reply_markup=categoryVKLike)
	await call.message.delete()
	await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains="vklayk")
async def vkpodpischik(call: CallbackQuery):
	VKobunachi1 = open("insta/VKobunachi1.txt","r")
	VKobunachisi1 = int(VKobunachi1.read())
	VKobunachi1.close()
	await call.message.answer(f"<b>❤️ 1000 ta like narxi: {VKobunachisi1}₽\n\n🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 35000 ta\n🔴 Nakrutka Tezligi - Tez\n🚀 Joriy tezlik - (~1055) soatiga\n\n👇 Marhamat kerakli miqdorni kiriting.</b>",reply_markup=Torqaga)
	await call.message.delete()
	await call.answer(cache_time=60)
	await Instas.vkin1.set()

@dp.message_handler(state=Instas.vkin1)
async def vkinput1(message: Message,state: FSMContext):
	id = message.from_user.id
	vkin1 = message.text
	await state.update_data(
		{"vkin1": vkin1}
	)
	try:
		kiriti = int(vkin1)
		if kiriti >= 50:
			balansg = open(f"balans/balans{id}.txt", "r")
			VKobunachi1 = open("insta/VKobunachi1.txt","r")
			sumasi = int(VKobunachi1.read())
			hisobi = float(balansg.read())
		
			donasi = sumasi / 1000
			hisobk = kiriti * donasi
			balansg.close()
			VKobunachi1.close()
		if hisobi >= hisobk:
			await message.answer(f"<b>💬 VKontakte Post linkni kiriting👇\n\n✅ Masalan: https://m.vk.com/wall718916597_1</b>",reply_markup=Torqaga)
			await Instas.vklink1.set()
		else:
			await message.answer(f"<b>💰Hisobingizda yetarli mablag' mavjud emas!</b>")
	except:
		await message.answer("<b>🔥 Minimal buyurtma: 50 ta\n⚡️ Maksimal buyurtma: 35000 ta\n\n👇 Marhamat kerakli miqdorni kiriting.</b>")

@dp.message_handler(state=Instas.vklink1)
async def vklinki1(message: types.Message, state: FSMContext):
	vklink1 = message.text
	await state.update_data(
        {"vklink1": vklink1}
	)
	data = await state.get_data()
	vkin1 = data.get("vkin1")
	vklink1 = data.get("vklink1")
	VKobunachi1 = open("insta/VKobunachi1.txt","r")
	natija = int(VKobunachi1.read())
	instai = int(vkin1)
	snatija = natija / 1000
	onatija = snatija * instai
	natijalar = "%.2f" % onatija
	msg = f"<b>📇 Malumotlar to'g'riligini tekshring👇\n\n🗞 Buyurtma soni - {vkin1} ta\n🖇 Link - {vklink1}\n💰 Buyurtma narxi - {natijalar}₽</b>"
	VKobunachi1.close()
	await Instas.next()
	await message.answer(msg,reply_markup=confirmation_keyboardVK1)


@dp.callback_query_handler(post_callbackVK1.filter(actionVK1="postVK1"), state=Instas.vkcon1)
async def confirm_VK1(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        vkin1 = data.get("vkin1")
        vklink1 = data.get("vklink1")
        id = call.message.chat.id
        aslbalans = open(f"balans/balans{id}.txt", "r")
        VKobunachi1 = open("insta/VKobunachi1.txt","r")
        innarxi = int(VKobunachi1.read())
        sonib = int(vkin1)
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
        VKobunachi1.close()
        mykey = "badcfb3366718f41450ead89cf954878"
        url = f'https://wiq.ru/api/?key={mykey}&action=create&service=351&quantity={sonib}&link={vklink1}'
        respons = requests.get(url).json()
        resnatija = (respons["order"])
        msg = f"<b>📇Yangi buyurtma ID - {resnatija}\n📌Soni - {sonib} ta\n🖇Link - {vklink1}\n💰Narxi - {natijalar1}₽\n\n✅@NakrutkaiBot</b>"
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>📇Buyurtmangiz qabul qilindi✅\n\n🕐Tez orada buyurtmangiz to'liq bajariladi✅</b>",reply_markup=Menu)
    await bot.send_message(ADMINS[0],msg, parse_mode="HTML")
		
@dp.callback_query_handler(post_callbackVK1.filter(actionVK1="cancelVK1"), state=Instas.vkcon1)
async def cancel_VK1(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>Buyurtmalar bekor qilindi 🛑</b>",reply_markup=Menu)
    
@dp.message_handler(state=Instas.vkcon1)
async def enter_VK1(message: Message, state: FSMContext):
   await message.answer("<b>👆👆👆Quyidagi buyurtmangizni\n✅Tasdiqlang Yoki ❌Rad eting Bo'lmasa Botagi boshqa tugmalar ishlamaydi🔐</b>")
	