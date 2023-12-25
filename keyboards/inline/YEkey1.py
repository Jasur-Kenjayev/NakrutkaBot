from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callbackYE1 = CallbackData("create_post", "actionYE1")

confirmation_keyboardYE1 = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅ Tastiqlash", callback_data=post_callbackYE1.new(actionYE1="postYE1")),
        ],
        [
        InlineKeyboardButton(text="Rad etish 🚫", callback_data=post_callbackYE1.new(actionYE1="cancelYE1")),
    ]]
)

