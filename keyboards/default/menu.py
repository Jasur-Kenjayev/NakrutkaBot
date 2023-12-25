from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

Menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="❤️ Nakrutka"),
        ],
       [
       	KeyboardButton(text="💰Balans"),
       	KeyboardButton(text="💳 To'ldirish")
       ],
      [
      	KeyboardButton(text="💬 Yordam"),
       ],
    ],
    resize_keyboard=True,
)

PayAdd = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💳 HUMO"),
        ],
       [
      	KeyboardButton(text="↩️ Orqaga"),
       ],
    ],
    resize_keyboard=True,
)
