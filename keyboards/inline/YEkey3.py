from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callbackYE3 = CallbackData("create_post", "actionYE3")

confirmation_keyboardYE3 = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅ Tastiqlash", callback_data=post_callbackYE3.new(actionYE3="postYE3")),
        ],
        [
        InlineKeyboardButton(text="Rad etish 🚫", callback_data=post_callbackYE3.new(actionYE3="cancelYE3")),
    ]]
)

