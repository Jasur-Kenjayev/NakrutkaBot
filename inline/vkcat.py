from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

categoryVK = InlineKeyboardMarkup(
    inline_keyboard=[
    [
    InlineKeyboardButton(text="👥 Obunachilar", callback_data="vkpodpischik"),
    ],
])

categoryVKProsmotr = InlineKeyboardMarkup(
    inline_keyboard=[
    [
    InlineKeyboardButton(text="🔎 Prosmotr (Ko'zlar)", callback_data="VKprosmotri"),
    ],
])

categoryVKLike = InlineKeyboardMarkup(
    inline_keyboard=[
    [
    InlineKeyboardButton(text="❤️ Like tezkor VK", callback_data="vklayk"),
    ],
])