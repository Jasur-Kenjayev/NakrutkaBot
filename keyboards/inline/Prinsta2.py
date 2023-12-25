from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callbackP2 = CallbackData("create_post", "actionP2")

confirmation_keyboardP2 = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅ Tastiqlash", callback_data=post_callbackP2.new(actionP2="postP2")),
        ],
        [
        InlineKeyboardButton(text="Rad etish 🚫", callback_data=post_callbackP2.new(actionP2="cancelP2")),
    ]]
)

