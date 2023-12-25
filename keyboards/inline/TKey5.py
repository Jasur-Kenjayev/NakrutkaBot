from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callbackTK5 = CallbackData("create_post", "actionTK5")

confirmation_keyboardTK5 = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅ Tastiqlash", callback_data=post_callbackTK5.new(actionTK5="postTK5")),
        ],
        [
        InlineKeyboardButton(text="Rad etish 🚫", callback_data=post_callbackTK5.new(actionTK5="cancelTK5")),
    ]]
)

