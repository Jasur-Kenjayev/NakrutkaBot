from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callbackLE1 = CallbackData("create_post", "actionLE1")

confirmation_keyboardLE1 = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅ Tastiqlash", callback_data=post_callbackLE1.new(actionLE1="postLE1")),
        ],
        [
        InlineKeyboardButton(text="Rad etish 🚫", callback_data=post_callbackLE1.new(actionLE1="cancelLE1")),
    ]]
)

