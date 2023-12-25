from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callbacki = CallbackData("create_post", "actioni")

confirmation_keyboardi = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅ Tastiqlash", callback_data=post_callbacki.new(actioni="posti")),
        ],
        [
        InlineKeyboardButton(text="Rad etish 🚫", callback_data=post_callbacki.new(actioni="canceli")),
    ]]
)

