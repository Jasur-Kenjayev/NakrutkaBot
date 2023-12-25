from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callbackTG1 = CallbackData("create_post", "actionTG1")

confirmation_keyboardTG1 = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅ Tastiqlash", callback_data=post_callbackTG1.new(actionTG1="postTG1")),
        ],
        [
        InlineKeyboardButton(text="Rad etish 🚫", callback_data=post_callbackTG1.new(actionTG1="cancelTG1")),
    ]]
)

