from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callbackTG4 = CallbackData("create_post", "actionTG4")

confirmation_keyboardTG4 = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅ Tastiqlash", callback_data=post_callbackTG4.new(actionTG4="postTG4")),
        ],
        [
        InlineKeyboardButton(text="Rad etish 🚫", callback_data=post_callbackTG4.new(actionTG4="cancelTG4")),
    ]]
)

