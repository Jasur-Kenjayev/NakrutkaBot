from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callbackTG3 = CallbackData("create_post", "actionTG3")

confirmation_keyboardTG3 = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅ Tastiqlash", callback_data=post_callbackTG3.new(actionTG3="postTG3")),
        ],
        [
        InlineKeyboardButton(text="Rad etish 🚫", callback_data=post_callbackTG3.new(actionTG3="cancelTG3")),
    ]]
)

