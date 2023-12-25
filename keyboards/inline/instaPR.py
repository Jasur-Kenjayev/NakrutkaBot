from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

categoryPros = InlineKeyboardMarkup(
    inline_keyboard=[
    [
    InlineKeyboardButton(text="🎥 Video ko'rishlar + RELS + IGTV", callback_data="PR1"),
    ],
    [
        InlineKeyboardButton(text="📖 Prosmotr (Stories)", callback_data="PS1"),
    ],
    [
    InlineKeyboardButton(text="🎥 🚨 Video ko'rishlar + RELS + IGTV", callback_data="PR2"),
    ],
    [
    	InlineKeyboardButton(text="📖 Prosmotr Kafolatli (Stories) ", callback_data="PS2"),
    ],
])