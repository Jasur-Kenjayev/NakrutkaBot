from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callbackP3 = CallbackData("create_post", "actionP3")

confirmation_keyboardP3 = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅ Tastiqlash", callback_data=post_callbackP3.new(actionP3="postP3")),
        ],
        [
        InlineKeyboardButton(text="Rad etish 🚫", callback_data=post_callbackP3.new(actionP3="cancelP3")),
    ]]
)

