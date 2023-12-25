from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callbackTG5 = CallbackData("create_post", "actionTG5")

confirmation_keyboardTG5 = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅ Tastiqlash", callback_data=post_callbackTG5.new(actionTG5="postTG5")),
        ],
        [
        InlineKeyboardButton(text="Rad etish 🚫", callback_data=post_callbackTG5.new(actionTG5="cancelTG5")),
    ]]
)

