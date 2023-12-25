from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callbackP = CallbackData("create_post", "actionP")

confirmation_keyboardP = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅ Tastiqlash", callback_data=post_callbackP.new(actionP="postP")),
        ],
        [
        InlineKeyboardButton(text="Rad etish 🚫", callback_data=post_callbackP.new(actionP="cancelP")),
    ]]
)

