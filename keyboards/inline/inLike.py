from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callbackL = CallbackData("create_post", "actionL")

confirmation_keyboardL = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅ Tastiqlash", callback_data=post_callbackL.new(actionL="postL")),
        ],
        [
        InlineKeyboardButton(text="Rad etish 🚫", callback_data=post_callbackL.new(actionL="cancelL")),
    ]]
)

