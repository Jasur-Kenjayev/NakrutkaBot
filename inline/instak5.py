from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callbacki5 = CallbackData("create_post", "actioni5")

confirmation_keyboardi5 = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅ Tastiqlash", callback_data=post_callbacki5.new(actioni5="posti5")),
        ],
        [
        InlineKeyboardButton(text="Rad etish 🚫", callback_data=post_callbacki5.new(actioni5="canceli5")),
    ]]
)

