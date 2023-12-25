from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

Tarmoq = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔴 Instagram"),
        ],
       [
       	KeyboardButton(text="🟣 VKontakte"),
       	KeyboardButton(text="🔵 Telegram"),
       ],
      [
      	KeyboardButton(text="🟠 Likee"), 		  KeyboardButton(text="🟢 Twitter"),
       ],
       [
       	KeyboardButton(text="⚫ TikTok"),
       	KeyboardButton(text="🟤 YouTube"),
       ],
       [
      	KeyboardButton(text="🔚 Orqaga"),
       ],
    ],
    resize_keyboard=True,
)

Torqaga = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔙 Orqaga"),
         ],
    ],
    resize_keyboard=True,
)