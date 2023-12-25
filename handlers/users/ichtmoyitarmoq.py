from aiogram.dispatcher import FSMContext
from aiogram import types
from keyboards.default.adminKeyboard import asosiymenu, bekor, tarmoqlar,  instagramuchun, instaobunachi, bekorqilish, instaPRosm, bekorqilishP, instaLike, bekorqilishL, VKuchun, VKOI, VKLe, VKPR, TGuchun, TGobunachilar, bekorqilishTG, TGprosm, LEuchun, LEobunachi, LEprosmotr, LElike, bekorqilishLE, TRuchun, TRprosmotr, bekorqilishTR, TKuchun, TKobunachi, TKprosmotr, TKlike, bekorqilishTK, YEuchun, YEprosmotr, YElike, bekorqilishYE
from data.config import ADMINS
from loader import dp, db, bot
from states.instaaddmoney import instaaddMoney

#tarmoqlar
@dp.message_handler(text="📈 NARXLAR", user_id=ADMINS)
async def tarmoqi(message: types.Message):
	await message.answer("<b>Marhamat keraklisini tanlang👇</b>",reply_markup=tarmoqlar)

@dp.message_handler(text="⤵️ Orqaga", user_id=ADMINS)
async def tarmoqio(message: types.Message):
	await message.answer("<b>🤖Bosh Menudasiz✅</b>",reply_markup=asosiymenu)

#instagram Menu
@dp.message_handler(text="📸 Instagram", user_id=ADMINS)
async def instacat(message: types.Message):
	await message.answer("<b>Marhamat keraklisini tanlang👇</b>",reply_markup=instagramuchun)

@dp.message_handler(text="📸 Orqaga", user_id=ADMINS)
async def instacato(message: types.Message):
	await message.answer("<b>🤖Bosh Menudasiz✅</b>",reply_markup=tarmoqlar)

#instagram obunachilar menusi
@dp.message_handler(text="👤Obunachi", user_id=ADMINS)
async def instacatoi(message: types.Message):
	await message.answer("<b>Marhamat keraklisini tanlang👇</b>",reply_markup=instaobunachi)

@dp.message_handler(text="Orqaga 📸", user_id=ADMINS)
async def instacatori(message: types.Message):
	await message.answer("<b>🤖Bosh Menudasiz✅</b>",reply_markup=instagramuchun)

#instagram add money1
@dp.message_handler(text="📸 Bekor qilish",state=instaaddMoney,user_id=ADMINS)
async def inst_ko(message: types.Message, state: FSMContext):
	await state.finish()
	await message.answer("<b>🤖Bosh Menudasiz✅</b>",reply_markup=instaobunachi)

@dp.message_handler(text="1⃣Obunachi", user_id=ADMINS)
async def kurs_insta1(message: types.Message):
    await message.answer("<b>Marhamat Narxni Kiriting👇</b>",reply_markup=bekorqilish)
    await instaaddMoney.instaadd1.set()
    
@dp.message_handler(state=instaaddMoney.instaadd1)
async def insta_narx1(message: types.Message, state: FSMContext):
    instanarx1 = message.text
    instanarxi1 = open("insta/instanarx1.txt","w")
    instanarxi1.write(instanarx1)
    instanarxi1.close()
    await message.answer("<b>📊Narxi O'zgartirildi✅</b>",reply_markup=instaobunachi)
    await state.finish()

@dp.message_handler(text="2⃣Obunachi", user_id=ADMINS)
async def kurs_insta2(message: types.Message):
    await message.answer("<b>Marhamat Narxni Kiriting👇</b>",reply_markup=bekorqilish)
    await instaaddMoney.instaadd2.set()
    
@dp.message_handler(state=instaaddMoney.instaadd2)
async def insta_narx2(message: types.Message, state: FSMContext):
    instanarx2 = message.text
    instanarxi2 = open("insta/instanarx2.txt","w")
    instanarxi2.write(instanarx2)
    instanarxi2.close()
    await message.answer("<b>📊Narxi O'zgartirildi✅</b>",reply_markup=instaobunachi)
    await state.finish()

@dp.message_handler(text="3⃣Obunachi", user_id=ADMINS)
async def kurs_insta3(message: types.Message):
    await message.answer("<b>Marhamat Narxni Kiriting👇</b>",reply_markup=bekorqilish)
    await instaaddMoney.instaadd3.set()
    
@dp.message_handler(state=instaaddMoney.instaadd3)
async def insta_narx3(message: types.Message, state: FSMContext):
    instanarx3 = message.text
    instanarxi3 = open("insta/instanarx3.txt","w")
    instanarxi3.write(instanarx3)
    instanarxi3.close()
    await message.answer("<b>📊Narxi O'zgartirildi✅</b>",reply_markup=instaobunachi)
    await state.finish()

@dp.message_handler(text="4⃣Obunachi", user_id=ADMINS)
async def kurs_insta4(message: types.Message):
    await message.answer("<b>Marhamat Narxni Kiriting👇</b>",reply_markup=bekorqilish)
    await instaaddMoney.instaadd4.set()
    
@dp.message_handler(state=instaaddMoney.instaadd4)
async def insta_narx4(message: types.Message, state: FSMContext):
    instanarx4 = message.text
    instanarxi4 = open("insta/instanarx4.txt","w")
    instanarxi4.write(instanarx4)
    instanarxi4.close()
    await message.answer("<b>📊Narxi O'zgartirildi✅</b>",reply_markup=instaobunachi)
    await state.finish()

@dp.message_handler(text="5⃣Obunachi", user_id=ADMINS)
async def kurs_insta5(message: types.Message):
    await message.answer("<b>Marhamat Narxni Kiriting👇</b>",reply_markup=bekorqilish)
    await instaaddMoney.instaadd5.set()
    
@dp.message_handler(state=instaaddMoney.instaadd5)
async def insta_narx5(message: types.Message, state: FSMContext):
    instanarx5 = message.text
    instanarxi5 = open("insta/instanarx5.txt","w")
    instanarxi5.write(instanarx5)
    instanarxi5.close()
    await message.answer("<b>📊Narxi O'zgartirildi✅</b>",reply_markup=instaobunachi)
    await state.finish()

@dp.message_handler(text="6⃣Obunachi", user_id=ADMINS)
async def kurs_insta6(message: types.Message):
    await message.answer("<b>Marhamat Narxni Kiriting👇</b>",reply_markup=bekorqilish)
    await instaaddMoney.instaadd6.set()
    
@dp.message_handler(state=instaaddMoney.instaadd6)
async def insta_narx6(message: types.Message, state: FSMContext):
    instanarx6 = message.text
    instanarxi6 = open("insta/instanarx6.txt","w")
    instanarxi6.write(instanarx6)
    instanarxi6.close()
    await message.answer("<b>📊Narxi O'zgartirildi✅</b>",reply_markup=instaobunachi)
    await state.finish()
    
@dp.message_handler(text="7⃣Obunachi", user_id=ADMINS)
async def kurs_insta7(message: types.Message):
    await message.answer("<b>Marhamat Narxni Kiriting👇</b>",reply_markup=bekorqilish)
    await instaaddMoney.instaadd7.set()
    
@dp.message_handler(state=instaaddMoney.instaadd7)
async def insta_narx7(message: types.Message, state: FSMContext):
    instanarx7 = message.text
    instanarxi7 = open("insta/instanarx7.txt","w")
    instanarxi7.write(instanarx7)
    instanarxi7.close()
    await message.answer("<b>📊Narxi O'zgartirildi✅</b>",reply_markup=instaobunachi)
    await state.finish()

#instagram Prosmotr Menusi

@dp.message_handler(text="👁Prosmotr", user_id=ADMINS)
async def instaPcat(message: types.Message):
	await message.answer("<b>Marhamat keraklisini tanlang👇</b>",reply_markup=instaPRosm)

@dp.message_handler(text="👁Bekor qilish",state=instaaddMoney,user_id=ADMINS)
async def insta_po(message: types.Message, state: FSMContext):
	await state.finish()
	await message.answer("<b>🤖Bosh Menudasiz✅</b>",reply_markup=instaPRosm)
	
@dp.message_handler(text="1⃣Prosmotr", user_id=ADMINS)
async def insta_Pro(message: types.Message):
    await message.answer("<b>Marhamat Narxni Kiriting👇</b>",reply_markup=bekorqilishP)
    await instaaddMoney.instaPros.set()
    
@dp.message_handler(state=instaaddMoney.instaPros)
async def insta_Pro1(message: types.Message, state: FSMContext):
    instaP = message.text
    instaPr = open("insta/instaPr.txt","w")
    instaPr.write(instaP)
    instaPr.close()
    await message.answer("<b>📊Narxi O'zgartirildi✅</b>",reply_markup=instaPRosm)
    await state.finish()


@dp.message_handler(text="2⃣Prosmotr", user_id=ADMINS)
async def insta_PS(message: types.Message):
    await message.answer("<b>Marhamat Narxni Kiriting👇</b>",reply_markup=bekorqilishP)
    await instaaddMoney.instaPros1.set()
    
@dp.message_handler(state=instaaddMoney.instaPros1)
async def insta_PS(message: types.Message, state: FSMContext):
    instaP1 = message.text
    instaPr1 = open("insta/instaPr1.txt","w")
    instaPr1.write(instaP1)
    instaPr1.close()
    await message.answer("<b>📊Narxi O'zgartirildi✅</b>",reply_markup=instaPRosm)
    await state.finish()

@dp.message_handler(text="3⃣Prosmotr", user_id=ADMINS)
async def insta_PR2(message: types.Message):
    await message.answer("<b>Marhamat Narxni Kiriting👇</b>",reply_markup=bekorqilishP)
    await instaaddMoney.instaPros2.set()
    
@dp.message_handler(state=instaaddMoney.instaPros2)
async def insta_PR2(message: types.Message, state: FSMContext):
    instaP2 = message.text
    instaPr2 = open("insta/instaPr2.txt","w")
    instaPr2.write(instaP2)
    instaPr2.close()
    await message.answer("<b>📊Narxi O'zgartirildi✅</b>",reply_markup=instaPRosm)
    await state.finish()
    
@dp.message_handler(text="4⃣Prosmotr", user_id=ADMINS)
async def insta_PR3(message: types.Message):
    await message.answer("<b>Marhamat Narxni Kiriting👇</b>",reply_markup=bekorqilishP)
    await instaaddMoney.instaPros3.set()
    
@dp.message_handler(state=instaaddMoney.instaPros3)
async def insta_PR3(message: types.Message, state: FSMContext):
    instaP3 = message.text
    instaPr3 = open("insta/instaPr3.txt","w")
    instaPr3.write(instaP3)
    instaPr3.close()
    await message.answer("<b>📊Narxi O'zgartirildi✅</b>",reply_markup=instaPRosm)
    await state.finish()

#instagram Like
@dp.message_handler(text="❤️Like", user_id=ADMINS)
async def insli(message: types.Message):
	await message.answer("<b>Marhamat keraklisini tanlang👇</b>",reply_markup=instaLike)

@dp.message_handler(text="❤️Bekor qilish",state=instaaddMoney,user_id=ADMINS)
async def insta_lik(message: types.Message, state: FSMContext):
	await state.finish()
	await message.answer("<b>🤖Bosh Menudasiz✅</b>",reply_markup=instaLike)
	
@dp.message_handler(text="1⃣Like", user_id=ADMINS)
async def insta_Liki(message: types.Message):
    await message.answer("<b>Marhamat Narxni Kiriting👇</b>",reply_markup=bekorqilishL)
    await instaaddMoney.likes.set()
    
@dp.message_handler(state=instaaddMoney.likes)
async def instaa_Liki(message: types.Message, state: FSMContext):
    likei = message.text
    likt = open("insta/liket.txt","w")
    likt.write(likei)
    likt.close()
    await message.answer("<b>📊Narxi O'zgartirildi✅</b>",reply_markup=instaLike)
    await state.finish()

@dp.message_handler(text="2⃣Like", user_id=ADMINS)
async def insta_Liki2(message: types.Message):
    await message.answer("<b>Marhamat Narxni Kiriting👇</b>",reply_markup=bekorqilishL)
    await instaaddMoney.likes1.set()
    
@dp.message_handler(state=instaaddMoney.likes1)
async def instaa_Liki2(message: types.Message, state: FSMContext):
    likei1 = message.text
    likt1 = open("insta/liket1.txt","w")
    likt1.write(likei1)
    likt1.close()
    await message.answer("<b>📊Narxi O'zgartirildi✅</b>",reply_markup=instaLike)
    await state.finish()

#VKONTAKT
@dp.message_handler(text="💬 VKontakte", user_id=ADMINS)
async def VKcate(message: types.Message):
	await message.answer("<b>Marhamat keraklisini tanlang👇</b>",reply_markup=VKuchun)

#VK OBUNACHI
@dp.message_handler(text="👤ObunachiVK", user_id=ADMINS)
async def VKobunachi(message: types.Message):
	await message.answer("<b>Marhamat keraklisini tanlang👇</b>",reply_markup=VKOI)

@dp.message_handler(text="❤️LikeVK", user_id=ADMINS)
async def VKLike(message: types.Message):
	await message.answer("<b>Marhamat keraklisini tanlang👇</b>",reply_markup=VKLe)

@dp.message_handler(text="👁ProsmotrVK", user_id=ADMINS)
async def VKPros(message: types.Message):
	await message.answer("<b>Marhamat keraklisini tanlang👇</b>",reply_markup=VKPR)

@dp.message_handler(text="1⃣ObunachiVK", user_id=ADMINS)
async def VK_Obun(message: types.Message):
    await message.answer("<b>Marhamat Narxni Kiriting👇</b>",reply_markup=bekorqilishL)
    await instaaddMoney.VKstet.set()
    
@dp.message_handler(state=instaaddMoney.VKstet)
async def VK_Obuns(message: types.Message, state: FSMContext):
    vksms = message.text
    VKobunachi = open("insta/VKobunachi.txt","w")
    VKobunachi.write(vksms)
    VKobunachi.close()
    await message.answer("<b>📊Narxi O'zgartirildi✅</b>",reply_markup=VKOI)
    await state.finish()

@dp.message_handler(text="1⃣LikeVK", user_id=ADMINS)
async def VK_Likes(message: types.Message):
    await message.answer("<b>Marhamat Narxni Kiriting👇</b>",reply_markup=bekorqilishL)
    await instaaddMoney.VKstet1.set()
    
@dp.message_handler(state=instaaddMoney.VKstet1)
async def VK_Liksh(message: types.Message, state: FSMContext):
    vkmsg = message.text
    VKobunachi1 = open("insta/VKobunachi1.txt","w")
    VKobunachi1.write(vkmsg)
    VKobunachi1.close()
    await message.answer("<b>📊Narxi O'zgartirildi✅</b>",reply_markup=VKLe)
    await state.finish()

@dp.message_handler(text="1⃣ProsmotrVK", user_id=ADMINS)
async def VK_Prosmotr(message: types.Message):
    await message.answer("<b>Marhamat Narxni Kiriting👇</b>",reply_markup=bekorqilishL)
    await instaaddMoney.VKstet2.set()
    
@dp.message_handler(state=instaaddMoney.VKstet2)
async def VK_Prosm(message: types.Message, state: FSMContext):
    vkmsg1 = message.text
    VKobunachi2 = open("insta/VKobunachi2.txt","w")
    VKobunachi2.write(vkmsg1)
    VKobunachi2.close()
    await message.answer("<b>📊Narxi O'zgartirildi✅</b>",reply_markup=VKPR)
    await state.finish()

#Telegram Menu
@dp.message_handler(text="🛩 Telegram", user_id=ADMINS)
async def TGMenu(message: types.Message):
	await message.answer("<b>Marhamat keraklisini tanlang👇</b>",reply_markup=
TGuchun)

#Telegram OBUNACHI
@dp.message_handler(text="👤ObunachiTG", user_id=ADMINS)
async def TGobunachi(message: types.Message):
	await message.answer("<b>Marhamat keraklisini tanlang👇</b>",reply_markup=TGobunachilar)

#Telegram Prosmotr

@dp.message_handler(text="👁ProsmotrTG", user_id=ADMINS)
async def TGprosmotri(message: types.Message):
	await message.answer("<b>Marhamat keraklisini tanlang👇</b>",reply_markup=TGprosm)
	
#Bekor qilish menusi
@dp.message_handler(text="🚫 Bekor qilishtg",state=instaaddMoney,user_id=ADMINS)
async def insta_lik(message: types.Message, state: FSMContext):
	await state.finish()
	await message.answer("<b>🤖Bosh Menudasiz✅</b>",reply_markup=TGobunachilar)
	
@dp.message_handler(text="1⃣ObunachiTG", user_id=ADMINS)
async def TG_obunachi1(message: types.Message):
    await message.answer("<b>Marhamat Narxni Kiriting👇</b>",reply_markup=bekorqilishTG)
    await instaaddMoney.telestet.set()
    
@dp.message_handler(state=instaaddMoney.telestet)
async def TG_Obunachi2(message: types.Message, state: FSMContext):
    TGmsg = message.text
    TGobunachif = open("insta/TGobunachi.txt","w")
    TGobunachif.write(TGmsg)
    TGobunachif.close()
    await message.answer("<b>📊Narxi O'zgartirildi✅</b>",reply_markup=TGuchun)
    await state.finish()

@dp.message_handler(text="2⃣ObunachiTG", user_id=ADMINS)
async def TG_obunachi2(message: types.Message):
    await message.answer("<b>Marhamat Narxni Kiriting👇</b>",reply_markup=bekorqilishTG)
    await instaaddMoney.telestet1.set()
    
@dp.message_handler(state=instaaddMoney.telestet1)
async def TG_Obunachi3(message: types.Message, state: FSMContext):
    TGmsg1 = message.text
    TGobunachif1 = open("insta/TGobunachi1.txt","w")
    TGobunachif1.write(TGmsg1)
    TGobunachif1.close()
    await message.answer("<b>📊Narxi O'zgartirildi✅</b>",reply_markup=TGuchun)
    await state.finish()

@dp.message_handler(text="3⃣ObunachiTG", user_id=ADMINS)
async def TG_obunachi3(message: types.Message):
    await message.answer("<b>Marhamat Narxni Kiriting👇</b>",reply_markup=bekorqilishTG)
    await instaaddMoney.telestet2.set()
    
@dp.message_handler(state=instaaddMoney.telestet2)
async def TG_Obunachi4(message: types.Message, state: FSMContext):
    TGmsg2 = message.text
    TGobunachif2 = open("insta/TGobunachi2.txt","w")
    TGobunachif2.write(TGmsg2)
    TGobunachif2.close()
    await message.answer("<b>📊Narxi O'zgartirildi✅</b>",reply_markup=TGuchun)
    await state.finish()

@dp.message_handler(text="4⃣ObunachiTG", user_id=ADMINS)
async def TG_obunachi4(message: types.Message):
    await message.answer("<b>Marhamat Narxni Kiriting👇</b>",reply_markup=bekorqilishTG)
    await instaaddMoney.telestet3.set()
    
@dp.message_handler(state=instaaddMoney.telestet3)
async def TG_Obunachi5(message: types.Message, state: FSMContext):
    TGmsg3 = message.text
    TGobunachif3 = open("insta/TGobunachi3.txt","w")
    TGobunachif3.write(TGmsg3)
    TGobunachif3.close()
    await message.answer("<b>📊Narxi O'zgartirildi✅</b>",reply_markup=TGuchun)
    await state.finish()

@dp.message_handler(text="5⃣ObunachiTG", user_id=ADMINS)
async def TG_obunachi6(message: types.Message):
    await message.answer("<b>Marhamat Narxni Kiriting👇</b>",reply_markup=bekorqilishTG)
    await instaaddMoney.telestet5.set()
    
@dp.message_handler(state=instaaddMoney.telestet5)
async def TG_Obunachi6(message: types.Message, state: FSMContext):
    TGmsg4 = message.text
    TGobunachif4 = open("insta/TGobunachi4.txt","w")
    TGobunachif4.write(TGmsg4)
    TGobunachif4.close()
    await message.answer("<b>📊Narxi O'zgartirildi✅</b>",reply_markup=TGuchun)
    await state.finish()

@dp.message_handler(text="1⃣ProsmotrTG", user_id=ADMINS)
async def TG_obunachi5(message: types.Message):
    await message.answer("<b>Marhamat Narxni Kiriting👇</b>",reply_markup=bekorqilishTG)
    await instaaddMoney.telestet4.set()
    
@dp.message_handler(state=instaaddMoney.telestet4)
async def TG_Obunachi6(message: types.Message, state: FSMContext):
    TGmsg5 = message.text
    TGobunachif5 = open("insta/TGobunachi5.txt","w")
    TGobunachif5.write(TGmsg5)
    TGobunachif5.close()
    await message.answer("<b>📊Narxi O'zgartirildi✅</b>",reply_markup=TGprosm)
    await state.finish()

#Likee uchun

@dp.message_handler(text="❤️ Likee", user_id=ADMINS)
async def LEMenu(message: types.Message):
	await message.answer("<b>Marhamat keraklisini tanlang👇</b>",reply_markup=LEuchun)

@dp.message_handler(text="👤ObunachiLE", user_id=ADMINS)
async def LEobunachis(message: types.Message):
	await message.answer("<b>Marhamat keraklisini tanlang👇</b>",reply_markup=LEobunachi)

@dp.message_handler(text="👁ProsmotrLE", user_id=ADMINS)
async def LEprosmotri(message: types.Message):
	await message.answer("<b>Marhamat keraklisini tanlang👇</b>",reply_markup=LEprosmotr)

#Likee lik

@dp.message_handler(text="❤️LikeLE", user_id=ADMINS)
async def LElik(message: types.Message):
	await message.answer("<b>Marhamat keraklisini tanlang👇</b>",reply_markup=LElike)
	
	
#Bekor qilish menusi
@dp.message_handler(text="🚫 Bekor qilishle",state=instaaddMoney,user_id=ADMINS)
async def bekor_le(message: types.Message, state: FSMContext):
	await state.finish()
	await message.answer("<b>🤖Bosh Menudasiz✅</b>",reply_markup=LEuchun)
	
#stet

@dp.message_handler(text="1⃣ObunachiLE", user_id=ADMINS)
async def LE_obunachi(message: types.Message):
    await message.answer("<b>Marhamat Narxni Kiriting👇</b>",reply_markup=bekorqilishLE)
    await instaaddMoney.likestet.set()
    
@dp.message_handler(state=instaaddMoney.likestet)
async def le_obunachi(message: types.Message, state: FSMContext):
    lemsg = message.text
    likee = open("insta/likee.txt","w")
    likee.write(lemsg)
    likee.close()
    await message.answer("<b>📊Narxi O'zgartirildi✅</b>",reply_markup=LEobunachi)
    await state.finish()
#Prosmotr

@dp.message_handler(text="1⃣ProsmotrLE", user_id=ADMINS)
async def LE_prosmotr(message: types.Message):
    await message.answer("<b>Marhamat Narxni Kiriting👇</b>",reply_markup=bekorqilishLE)
    await instaaddMoney.likestet1.set()
    
@dp.message_handler(state=instaaddMoney.likestet1)
async def le_prosmotr(message: types.Message, state: FSMContext):
    lemsg1 = message.text
    likee1 = open("insta/likee1.txt","w")
    likee1.write(lemsg1)
    likee1.close()
    await message.answer("<b>📊Narxi O'zgartirildi✅</b>",reply_markup=LEprosmotr)
    await state.finish()

#Like

@dp.message_handler(text="1⃣LikeLE", user_id=ADMINS)
async def LE_Like(message: types.Message):
    await message.answer("<b>Marhamat Narxni Kiriting👇</b>",reply_markup=bekorqilishLE)
    await instaaddMoney.likestet2.set()
    
@dp.message_handler(state=instaaddMoney.likestet2)
async def le_like(message: types.Message, state: FSMContext):
    lemsg2 = message.text
    likee2 = open("insta/likee2.txt","w")
    likee2.write(lemsg2)
    likee2.close()
    await message.answer("<b>📊Narxi O'zgartirildi✅</b>",reply_markup=LElike)
    await state.finish()

#Twitter
@dp.message_handler(text="🕊 Twitter", user_id=ADMINS)
async def TRMenu(message: types.Message):
	await message.answer("<b>Marhamat keraklisini tanlang👇</b>",reply_markup=TRuchun)

@dp.message_handler(text="👁ProsmotrTR", user_id=ADMINS)
async def TRprosmotri(message: types.Message):
	await message.answer("<b>Marhamat keraklisini tanlang👇</b>",reply_markup=TRprosmotr)

@dp.message_handler(text="🚫 Bekor qilishtr",state=instaaddMoney,user_id=ADMINS)
async def bekor_le(message: types.Message, state: FSMContext):
	await state.finish()
	await message.answer("<b>🤖Bosh Menudasiz✅</b>",reply_markup=TRprosmotr)

@dp.message_handler(text="1⃣ProsmotrTR", user_id=ADMINS)
async def TR_prosmotr(message: types.Message):
    await message.answer("<b>Marhamat Narxni Kiriting👇</b>",reply_markup=bekorqilishTR)
    await instaaddMoney.trstet.set()
    
@dp.message_handler(state=instaaddMoney.trstet)
async def tr_prosmotr(message: types.Message, state: FSMContext):
    trm = message.text
    twitter = open("insta/twitter.txt","w")
    twitter.write(trm)
    twitter.close()
    await message.answer("<b>📊Narxi O'zgartirildi✅</b>",reply_markup=TRprosmotr)
    await state.finish()

#TikTok Menu

@dp.message_handler(text="🎶 TikTok", user_id=ADMINS)
async def TKMenu(message: types.Message):
	await message.answer("<b>Marhamat keraklisini tanlang👇</b>",reply_markup=TKuchun)

@dp.message_handler(text="🚫 Bekor qilishtk",state=instaaddMoney,user_id=ADMINS)
async def bekor_tk(message: types.Message, state: FSMContext):
	await state.finish()
	await message.answer("<b>🤖Bosh Menudasiz✅</b>",reply_markup=TKuchun)
	
@dp.message_handler(text="👤ObunachiTK", user_id=ADMINS)
async def TKobunachis(message: types.Message):
	await message.answer("<b>Marhamat keraklisini tanlang👇</b>",reply_markup=TKobunachi)
	
@dp.message_handler(text="👁ProsmotrTK", user_id=ADMINS)
async def TKprosmotri(message: types.Message):
	await message.answer("<b>Marhamat keraklisini tanlang👇</b>",reply_markup=TKprosmotr)

@dp.message_handler(text="❤️LikeTK", user_id=ADMINS)
async def TKlikei(message: types.Message):
	await message.answer("<b>Marhamat keraklisini tanlang👇</b>",reply_markup=TKlike)

#State tiktok

@dp.message_handler(text="1⃣ObunachiTK", user_id=ADMINS)
async def TK_obunachi(message: types.Message):
    await message.answer("<b>Marhamat Narxni Kiriting👇</b>",reply_markup=bekorqilishTK)
    await instaaddMoney.tkstet.set()
    
@dp.message_handler(state=instaaddMoney.tkstet)
async def TK_Obuna(message: types.Message, state: FSMContext):
    tkm = message.text
    tiktok = open("insta/tiktok.txt","w")
    tiktok.write(tkm)
    tiktok.close()
    await message.answer("<b>📊Narxi O'zgartirildi✅</b>",reply_markup=TKobunachi)
    await state.finish()

@dp.message_handler(text="2⃣ObunachiTK", user_id=ADMINS)
async def TK_obunachi1(message: types.Message):
    await message.answer("<b>Marhamat Narxni Kiriting👇</b>",reply_markup=bekorqilishTK)
    await instaaddMoney.tkstet1.set()
    
@dp.message_handler(state=instaaddMoney.tkstet1)
async def TK_Obuna1(message: types.Message, state: FSMContext):
    tkm1 = message.text
    tiktok1 = open("insta/tiktok1.txt","w")
    tiktok1.write(tkm1)
    tiktok1.close()
    await message.answer("<b>📊Narxi O'zgartirildi✅</b>",reply_markup=TKobunachi)
    await state.finish()

#Prosmotr

@dp.message_handler(text="1⃣ProsmotrTK", user_id=ADMINS)
async def TK_prosmotr(message: types.Message):
    await message.answer("<b>Marhamat Narxni Kiriting👇</b>",reply_markup=bekorqilishTK)
    await instaaddMoney.tkstet2.set()
    
@dp.message_handler(state=instaaddMoney.tkstet2)
async def TK_Pros(message: types.Message, state: FSMContext):
    tkm2 = message.text
    tiktok2 = open("insta/tiktok2.txt","w")
    tiktok2.write(tkm2)
    tiktok2.close()
    await message.answer("<b>📊Narxi O'zgartirildi✅</b>",reply_markup=TKprosmotr)
    await state.finish()

@dp.message_handler(text="2⃣ProsmotrTK", user_id=ADMINS)
async def TK_prosmotr1(message: types.Message):
    await message.answer("<b>Marhamat Narxni Kiriting👇</b>",reply_markup=bekorqilishTK)
    await instaaddMoney.tkstet3.set()
    
@dp.message_handler(state=instaaddMoney.tkstet3)
async def TK_Pros1(message: types.Message, state: FSMContext):
    tkm3 = message.text
    tiktok3 = open("insta/tiktok3.txt","w")
    tiktok3.write(tkm3)
    tiktok3.close()
    await message.answer("<b>📊Narxi O'zgartirildi✅</b>",reply_markup=TKprosmotr)
    await state.finish()

#Like

@dp.message_handler(text="1⃣LikeTK", user_id=ADMINS)
async def TK_Like(message: types.Message):
    await message.answer("<b>Marhamat Narxni Kiriting👇</b>",reply_markup=bekorqilishTK)
    await instaaddMoney.tkstet4.set()
    
@dp.message_handler(state=instaaddMoney.tkstet4)
async def TK_Lik(message: types.Message, state: FSMContext):
    tkm4 = message.text
    tiktok4 = open("insta/tiktok4.txt","w")
    tiktok4.write(tkm4)
    tiktok4.close()
    await message.answer("<b>📊Narxi O'zgartirildi✅</b>",reply_markup=TKlike)
    await state.finish()

@dp.message_handler(text="2⃣LikeTK", user_id=ADMINS)
async def TK_Like1(message: types.Message):
    await message.answer("<b>Marhamat Narxni Kiriting👇</b>",reply_markup=bekorqilishTK)
    await instaaddMoney.tkstet5.set()
    
@dp.message_handler(state=instaaddMoney.tkstet5)
async def TK_Lik1(message: types.Message, state: FSMContext):
    tkm5 = message.text
    tiktok5 = open("insta/tiktok5.txt","w")
    tiktok5.write(tkm5)
    tiktok5.close()
    await message.answer("<b>📊Narxi O'zgartirildi✅</b>",reply_markup=TKlike)
    await state.finish()

#YouTube Menu

@dp.message_handler(text="🎥 YouTube", user_id=ADMINS)
async def YEMenu(message: types.Message):
	await message.answer("<b>Marhamat keraklisini tanlang👇</b>",reply_markup=YEuchun)

@dp.message_handler(text="🚫 Bekor qilishye",state=instaaddMoney,user_id=ADMINS)
async def bekor_ye(message: types.Message, state: FSMContext):
	await state.finish()
	await message.answer("<b>🤖Bosh Menudasiz✅</b>",reply_markup=YEuchun)

@dp.message_handler(text="👁ProsmotrYE", user_id=ADMINS)
async def YEprosmotri(message: types.Message):
	await message.answer("<b>Marhamat keraklisini tanlang👇</b>",reply_markup=YEprosmotr)

@dp.message_handler(text="❤️LikeYE", user_id=ADMINS)
async def YElikei(message: types.Message):
	await message.answer("<b>Marhamat keraklisini tanlang👇</b>",reply_markup=YElike)

#State

@dp.message_handler(text="1⃣ProsmotrYE", user_id=ADMINS)
async def YE_prosmotr(message: types.Message):
    await message.answer("<b>Marhamat Narxni Kiriting👇</b>",reply_markup=bekorqilishYE)
    await instaaddMoney.yestet.set()
    
@dp.message_handler(state=instaaddMoney.yestet)
async def YE_Pros(message: types.Message, state: FSMContext):
    yem = message.text
    YouTube = open("insta/YouTube.txt","w")
    YouTube.write(yem)
    YouTube.close()
    await message.answer("<b>📊Narxi O'zgartirildi✅</b>",reply_markup=YEprosmotr)
    await state.finish()
   
@dp.message_handler(text="2⃣ProsmotrYE", user_id=ADMINS)
async def YE_prosmotr1(message: types.Message):
    await message.answer("<b>Marhamat Narxni Kiriting👇</b>",reply_markup=bekorqilishYE)
    await instaaddMoney.yestet1.set()
    
@dp.message_handler(state=instaaddMoney.yestet1)
async def YE_Pros1(message: types.Message, state: FSMContext):
    yem1 = message.text
    YouTube1 = open("insta/YouTube1.txt","w")
    YouTube1.write(yem1)
    YouTube1.close()
    await message.answer("<b>📊Narxi O'zgartirildi✅</b>",reply_markup=YEprosmotr)
    await state.finish()

#Like

@dp.message_handler(text="1⃣LikeYE", user_id=ADMINS)
async def YE_Like(message: types.Message):
    await message.answer("<b>Marhamat Narxni Kiriting👇</b>",reply_markup=bekorqilishYE)
    await instaaddMoney.yestet2.set()
    
@dp.message_handler(state=instaaddMoney.yestet2)
async def YE_Lik(message: types.Message, state: FSMContext):
    yeml = message.text
    YouTube2 = open("insta/YouTube2.txt","w")
    YouTube2.write(yeml)
    YouTube2.close()
    await message.answer("<b>📊Narxi O'zgartirildi✅</b>",reply_markup=YElike)
    await state.finish()

@dp.message_handler(text="2⃣LikeYE", user_id=ADMINS)
async def YE_Like81(message: types.Message):
    await message.answer("<b>Marhamat Narxni Kiriting👇</b>",reply_markup=bekorqilishYE)
    await instaaddMoney.yestet3.set()
    
@dp.message_handler(state=instaaddMoney.yestet3)
async def YE_Lik18(message: types.Message, state: FSMContext):
    yemli = message.text
    YouTube3 = open("insta/YouTube3.txt","w")
    YouTube3.write(yemli)
    YouTube3.close()
    await message.answer("<b>📊Narxi O'zgartirildi✅</b>",reply_markup=YElike)
    await state.finish()

