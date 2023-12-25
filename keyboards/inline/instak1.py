from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callbacki1 = CallbackData("create_post", "actioni1")

confirmation_keyboardi1 = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅ Tastiqlash", callback_data=post_callbacki1.new(actioni1="posti1")),
        ],
        [
        InlineKeyboardButton(text="Rad etish 🚫", callback_data=post_callbacki1.new(actioni1="canceli1")),
    ]]
)

