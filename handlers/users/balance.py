from aiogram import types
from loader import dp, bot
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from keyboards.default.adminKeyboard import asosiymenu, adbalans 
from states.balansstat import BalansS
from data.config import ADMINS
from keyboards.inline.idsendb import confirmation_keyboard, post_callback
from keyboards.inline.qolabquvatlash import balansadd 
from aiogram.types import ParseMode
from keyboards.default.menu import PayAdd

@dp.message_handler(text="💰Balans")
async def create_balans(message: Message):
	try:
		id = message.from_user.id
		balansi = open(f"balans/balans{id}.txt", "r")
		await message.answer(f"*👤 Ismingiz: {message.from_user.full_name}\n🔑 ID raqamingiz: {id}\n💵 Hisobingiz: {balansi.read()}₽*",parse_mode=ParseMode.MARKDOWN,reply_markup=balansadd)
		balansi.close()
	except:
		balans = open(f"balans/balans{id}.txt", "w")
		baci = ('0')
		balans.write(baci)
		balans.close()
		
		balansi = open(f"balans/balans{id}.txt", "r")
		await message.answer(f"*👤 Ismingiz: {message.from_user.full_name}\n🔑 ID raqamingiz: {id}\n💵 Hisobingiz: {balansi.read()}₽*",parse_mode=ParseMode.MARKDOWN,reply_markup=balansadd)
		balansi.close()
		
@dp.message_handler(text= "💰Orqaga",state=BalansS,user_id=ADMINS)
async def bal_or(message:
	types.Message, state: FSMContext):
	await state.finish()
	await message.answer("<b>🤖Orqaga Muvafaqiyatli qaytdingiz✅</b>",reply_markup=asosiymenu)

#send message user
@dp.message_handler(text="💸 ADD MONEY",user_id=ADMINS)
async def create_ball(message: Message):
    await message.answer("<b>👤 foydalanuvchi id ni kiriting👇</b>",reply_markup=adbalans)
    await BalansS.mball.set()

@dp.message_handler(state=BalansS.mball)
async def enter_ball(message: Message, state: FSMContext):
	mball = message.text
	await state.update_data(
		{"mball": mball}
	)
	balansu = open(f"balans/balans{mball}.txt", "r")
	await message.answer(f"<b>👤 foydalanuvchi balansi {balansu.read()}₽\n\n✏️ Yubormoqchi bo'lgan miqdorni kiriting👇</b>",reply_markup=adbalans)
	balansu.close()
	await BalansS.next()

@dp.message_handler(state=BalansS.oball)
async def iball(message: types.Message, state: FSMContext):
	oball = message.text
	await state.update_data(
        {"oball": oball}
	)
	data = await state.get_data()
	oball = data.get("oball")
	msg = f"<b>👤 foydalanuvchi balansiga {oball}₽ qo'shilsinmi?</b>"
	await BalansS.next()
	await message.answer(msg,reply_markup=confirmation_keyboard)
	
@dp.callback_query_handler(post_callback.filter(action="post"), state=BalansS.baConfirm)
async def confirm_postidb(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        mball = data.get("mball")
        oball  = data.get("oball")
        balans = open(f"balans/balans{mball}.txt", "w")
        balans.write(oball)
        balans.close()
        #msg = f"<b>💰Hisobingiz - {oball}₽ ga to'ldirildi✅</b>"
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>💸Hisob To'ldirildi✅</b>",reply_markup=asosiymenu)
    #await bot.send_message(mball,msg, parse_mode="HTML")
		
@dp.callback_query_handler(post_callback.filter(action="cancel"), state=BalansS.baConfirm)
async def cancel_postidb(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>Malumotlaringiz rad etildi 🛑</b>",reply_markup=asosiymenu)
    
@dp.message_handler(state=BalansS.baConfirm)
async def enter_finshitidb(message: Message, state: FSMContext):
   await message.answer("<b>👆👆👆Quyidagi Kiritgan Malumotlaringizni\n✅Tasdiqlang Yoki ❌Rad eting Bo'lmasa Botagi boshqa tugmalar ishlamaydi🔐</b>")
 
@dp.callback_query_handler(text_contains="hisobtoldrish")
async def popolni(call: CallbackQuery):
	await call.message.answer("<b>📲 Botdagi hisobingizni to'ldirish usulini tanlang👇</b>",reply_markup=PayAdd)
	await call.message.delete()
	await call.answer(cache_time=60)
	