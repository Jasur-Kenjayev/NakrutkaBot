from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callbackTG2 = CallbackData("create_post", "actionTG2")

confirmation_keyboardTG2 = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅ Tastiqlash", callback_data=post_callbackTG2.new(actionTG2="postTG2")),
        ],
        [
        InlineKeyboardButton(text="Rad etish 🚫", callback_data=post_callbackTG2.new(actionTG2="cancelTG2")),
    ]]
)

