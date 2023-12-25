from aiogram import types
from loader import dp, bot
from keyboards.default.tarmoq import Tarmoq, Torqaga
from keyboards.inline.vkcat import categoryVKProsmotr
from aiogram.types import Message, CallbackQuery
from states.instas import Instas
from aiogram.dispatcher import FSMContext
from keyboards.inline.VKKey2 import confirmation_keyboardVK2, post_callbackVK2
import requests
import json
from data.config import ADMINS
from keyboards.default.menu import Menu

@dp.callback_query_handler(text_contains="vkprosmotro")
async def vklikeb1(call: CallbackQuery):
	await call.message.answer("<b>📇Marhamat keraklisini tanlang👇</b>",reply_markup=categoryVKProsmotr)
	await call.message.delete()
	await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains="VKprosmotri")
async def vkpro1(call: CallbackQuery):
	VKobunachi2 = open("insta/VKobunachi2.txt","r")
	VKobunachisi2 = int(VKobunachi2.read())
	VKobunachi2.close()
	await call.message.answer(f"<b>👁 1000 ta prosmotr narxi {VKobunachisi2}₽\n\n🔥 Minimal buyurtma: 100 ta\n⚡️ Maksimal buyurtma: 500000 ta\n🔴 Nakrutka Tezligi - Tez\n🚀 Joriy tezlik - (~2-404) soatiga\n\n👇 Marhamat kerakli miqdorni kiriting.</b>",reply_markup=Torqaga)
	await call.message.delete()
	await call.answer(cache_time=60)
	await Instas.vkin2.set()

@dp.message_handler(state=Instas.vkin2)
async def vkinput2(message: Message,state: FSMContext):
	id = message.from_user.id
	vkin2 = message.text
	await state.update_data(
		{"vkin2": vkin2}
	)
	try:
		kiriti = int(vkin2)
		if kiriti >= 100:
			balansg = open(f"balans/balans{id}.txt", "r")
			VKobunachi2 = open("insta/VKobunachi2.txt","r")
			sumasi = int(VKobunachi2.read())
			hisobi = float(balansg.read())
		
			donasi = sumasi / 1000
			hisobk = kiriti * donasi
			balansg.close()
			VKobunachi2.close()
		if hisobi >= hisobk:
			await message.answer(f"<b>💬 VKontakte Post linkni kiriting👇\n\n✅ Masalan: https://m.vk.com/wall718916597_1</b>",reply_markup=Torqaga)
			await Instas.vklink2.set()
		else:
			await message.answer(f"<b>💰Hisobingizda yetarli mablag' mavjud emas!</b>")
	except:
		await message.answer("<b>🔥 Minimal buyurtma: 100 ta\n⚡️ Maksimal buyurtma: 500000 ta\n\n👇 Marhamat kerakli miqdorni kiriting.</b>")

@dp.message_handler(state=Instas.vklink2)
async def vklinki2(message: types.Message, state: FSMContext):
	vklink2 = message.text
	await state.update_data(
        {"vklink2": vklink2}
	)
	data = await state.get_data()
	vkin2 = data.get("vkin2")
	vklink2 = data.get("vklink2")
	VKobunachi2 = open("insta/VKobunachi2.txt","r")
	natija = int(VKobunachi2.read())
	instai = int(vkin2)
	snatija = natija / 1000
	onatija = snatija * instai
	natijalar = "%.2f" % onatija
	msg = f"<b>📇 Malumotlar to'g'riligini tekshring👇\n\n🗞 Buyurtma soni - {vkin2} ta\n🖇 Link - {vklink2}\n💰 Buyurtma narxi - {natijalar}₽</b>"
	VKobunachi2.close()
	await Instas.next()
	await message.answer(msg,reply_markup=confirmation_keyboardVK2)


@dp.callback_query_handler(post_callbackVK2.filter(actionVK2="postVK2"), state=Instas.vkcon2)
async def confirm_VK2(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        vkin2 = data.get("vkin2")
        vklink2 = data.get("vklink2")
        id = call.message.chat.id
        aslbalans = open(f"balans/balans{id}.txt", "r")
        VKobunachi2 = open("insta/VKobunachi2.txt","r")
        innarxi = int(VKobunachi2.read())
        sonib = int(vkin2)
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
        VKobunachi2.close()
        mykey = "badcfb3366718f41450ead89cf954878"
        url = f'https://wiq.ru/api/?key={mykey}&action=create&service=154&quantity={sonib}&link={vklink2}'
        respons = requests.get(url).json()
        resnatija = (respons["order"])
        msg = f"<b>📇Yangi buyurtma ID - {resnatija}\n📌Soni - {sonib} ta\n🖇Link - {vklink2}\n💰Narxi - {natijalar1}₽\n\n✅@NakrutkaiBot</b>"
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>📇Buyurtmangiz qabul qilindi✅\n\n🕐Tez orada buyurtmangiz to'liq bajariladi✅</b>",reply_markup=Menu)
    await bot.send_message(ADMINS[0],msg, parse_mode="HTML")
		
@dp.callback_query_handler(post_callbackVK2.filter(actionVK2="cancelVK2"), state=Instas.vkcon2)
async def cancel_VK2(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>Buyurtmalar bekor qilindi 🛑</b>",reply_markup=Menu)
    
@dp.message_handler(state=Instas.vkcon2)
async def enter_VK2(message: Message, state: FSMContext):
   await message.answer("<b>👆👆👆Quyidagi buyurtmangizni\n✅Tasdiqlang Yoki ❌Rad eting Bo'lmasa Botagi boshqa tugmalar ishlamaydi🔐</b>")
	