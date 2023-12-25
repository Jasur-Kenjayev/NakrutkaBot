from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callbackTK1 = CallbackData("create_post", "actionTK1")

confirmation_keyboardTK1 = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅ Tastiqlash", callback_data=post_callbackTK1.new(actionTK1="postTK1")),
        ],
        [
        InlineKeyboardButton(text="Rad etish 🚫", callback_data=post_callbackTK1.new(actionTK1="cancelTK1")),
    ]]
)

