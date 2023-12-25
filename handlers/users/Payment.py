from aiogram import types
from loader import dp
from keyboards.default.menu import Menu, PayAdd
from keyboards.inline.qolabquvatlash import qolabquvatla

@dp.message_handler(text="↩️ Orqaga")
async def boshmec(message:
	types.Message):
	await message.answer("<b>🖥 Asosiy menyuga qaytdingiz✅</b>",reply_markup=Menu)
	
@dp.message_handler(text="💳 To'ldirish")
async def toldrish(message:
	types.Message):
	await message.answer("<b>📲 Botdagi hisobingizni to'ldirish usulini tanlang👇</b>",reply_markup=PayAdd)

@dp.message_handler(text="💳 HUMO")
async def uzcard(message:
	types.Message):
	id = message.from_user.id
	KursRubl = open("insta/Kurs.txt","r")
	await message.answer(f"<b>💸 To'lov Tizimi: PAYME, CLICK, APELSIN, UPAY, OSON</b>\n\n<b>💳 Hamyon:</b> <code>9860600403919340</code>\n💬 <b>Izoh:</b> <code>{id}</code>\n\n🤖<i> Botdagi hisobingizni to'ldrish uchun quyidagi ko'rsatilgan </i><b>💳 HUMO Hamyon</b> <i>raqamiga kerakli pul miqdorini o'tqazing va pul o'tqazishda quyidagi</i> 💬<b> Izoh</b> <i>ni ham yozib yuboring.\n\n💰KARTA orqali to'langan So'm botdagi hisobingizga rubl bo'lib tushadi.</i>\n\n<b>💳 HUMO KARTADA TO'LDIRISH MINIMAL SUMMA 15000 SO'M</b>\n\n<b>📈 Kurs: 1₽ = {KursRubl.read()} So'm</b>\n\nℹ️ <i>To'lov qilishga tushunmasangiz. Qo'llab-Quvvatlashga murojat qiling!</i>",reply_markup=qolabquvatla)
	KursRubl.close()

@dp.message_handler(text="💬 Yordam")
async def yordam(message:
	types.Message):
	await message.answer("<b>ℹ️ Qo'llab-Quvvatlash xizmatiga savolingiz va taklifingiz bo'lsa yozib qoldrishingiz mumkun. Savol yo'lashda aniq va tushunarli yozib qoldiring\n\n📇 Nakrutka turuga qarab 5 daqiqadan 5 soat vaqt oralig'ida uriladi botmizda xar-xil turdagi nakrutka mavjud tez uriladigani va sekin uriladiganlari bor bu haqida nakrutka qilayotganingizda ko'rishingiz mumkun yozilgan to'liq barcha nakrutka xizmatlariga!\n\n🗞 Nakrutka bo'yicha Savolni Qo'llab-Quvvatlashga yozmang Sabirli bo'ling bas buyurtirgan nakrutkangiz albatta sizga boradi boshqaga ketib qolmaydi.</b>",reply_markup=qolabquvatla)
