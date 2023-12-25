from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callbackP1 = CallbackData("create_post", "actionP1")

confirmation_keyboardP1 = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅ Tastiqlash", callback_data=post_callbackP1.new(actionP1="postP1")),
        ],
        [
        InlineKeyboardButton(text="Rad etish 🚫", callback_data=post_callbackP1.new(actionP1="cancelP1")),
    ]]
)

