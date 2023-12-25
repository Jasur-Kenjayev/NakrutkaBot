from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callbacki6 = CallbackData("create_post", "actioni6")

confirmation_keyboardi6 = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅ Tastiqlash", callback_data=post_callbacki6.new(actioni6="posti6")),
        ],
        [
        InlineKeyboardButton(text="Rad etish 🚫", callback_data=post_callbacki6.new(actioni6="canceli6")),
    ]]
)

