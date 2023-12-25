from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callbackTK2 = CallbackData("create_post", "actionTK2")

confirmation_keyboardTK2 = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅ Tastiqlash", callback_data=post_callbackTK2.new(actionTK2="postTK2")),
        ],
        [
        InlineKeyboardButton(text="Rad etish 🚫", callback_data=post_callbackTK2.new(actionTK2="cancelTK2")),
    ]]
)

