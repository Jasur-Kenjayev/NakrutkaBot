from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callbackTK3 = CallbackData("create_post", "actionTK3")

confirmation_keyboardTK3 = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅ Tastiqlash", callback_data=post_callbackTK3.new(actionTK3="postTK3")),
        ],
        [
        InlineKeyboardButton(text="Rad etish 🚫", callback_data=post_callbackTK3.new(actionTK3="cancelTK3")),
    ]]
)

