from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callbackLE = CallbackData("create_post", "actionLE")

confirmation_keyboardLE = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅ Tastiqlash", callback_data=post_callbackLE.new(actionLE="postLE")),
        ],
        [
        InlineKeyboardButton(text="Rad etish 🚫", callback_data=post_callbackLE.new(actionLE="cancelLE")),
    ]]
)

