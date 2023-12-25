from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callbackTK = CallbackData("create_post", "actionTK")

confirmation_keyboardTK = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅ Tastiqlash", callback_data=post_callbackTK.new(actionTK="postTK")),
        ],
        [
        InlineKeyboardButton(text="Rad etish 🚫", callback_data=post_callbackTK.new(actionTK="cancelTK")),
    ]]
)

