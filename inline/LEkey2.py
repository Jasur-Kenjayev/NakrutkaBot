from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callbackLE2 = CallbackData("create_post", "actionLE2")

confirmation_keyboardLE2 = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅ Tastiqlash", callback_data=post_callbackLE2.new(actionLE2="postLE2")),
        ],
        [
        InlineKeyboardButton(text="Rad etish 🚫", callback_data=post_callbackLE2.new(actionLE2="cancelLE2")),
    ]]
)

