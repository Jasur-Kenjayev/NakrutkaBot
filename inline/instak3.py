from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callbacki3 = CallbackData("create_post", "actioni3")

confirmation_keyboardi3 = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅ Tastiqlash", callback_data=post_callbacki3.new(actioni3="posti3")),
        ],
        [
        InlineKeyboardButton(text="Rad etish 🚫", callback_data=post_callbacki3.new(actioni3="canceli3")),
    ]]
)

