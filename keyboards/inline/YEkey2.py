from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callbackYE2 = CallbackData("create_post", "actionYE2")

confirmation_keyboardYE2 = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅ Tastiqlash", callback_data=post_callbackYE2.new(actionYE2="postYE2")),
        ],
        [
        InlineKeyboardButton(text="Rad etish 🚫", callback_data=post_callbackYE2.new(actionYE2="cancelYE2")),
    ]]
)

