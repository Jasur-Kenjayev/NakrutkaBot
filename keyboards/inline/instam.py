from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
    [
    InlineKeyboardButton(text="👤 Obunachilar", callback_data="bezga"),
    ],
    [
        InlineKeyboardButton(text="👤 Obunachilar (REAL)", callback_data="realobuna"),
    ],
    [
    InlineKeyboardButton(text="👤 Obunachilar MIX (Yuqori sifat)", callback_data="mixkuzatuvchi"),
    ],
    [
    	InlineKeyboardButton(text="👤 Obunachilar (REAL-LUXE)", callback_data="realluxeo"),
    ],
    [
    InlineKeyboardButton(text="👤 Haqiqiy obunachilar", callback_data="Ar60obun"),
    ],
    [
    InlineKeyboardButton(text="👤 Kafolatli obunachilar", callback_data="KafolatR"),
    ],
    [
    InlineKeyboardButton(text="👤 Obunachilar (obunani bekor qilish yo'q)", callback_data="realbekorqi"),
    ],
])